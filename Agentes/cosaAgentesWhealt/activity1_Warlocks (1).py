#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 20:56:46 2024

@author: maximepariente
"""

import agentpy as ap
import numpy as np
import seaborn as sns
import random
import pandas as pd
import matplotlib.pyplot as plt

# base agent
class BaseWealthAgent(ap.Agent):
    """ Base agent with wealth """
    def setup(self):
        self.wealth = 1
        self.strategy_name = "Base"
    
    def wealth_transfer(self):
        pass

# Only transfers if units > 2
class ConservativeAgent(BaseWealthAgent):
    def setup(self):
        super().setup()
        self.strategy_name = "Conservative"
        self.wealth = 2  
    
    def wealth_transfer(self):
        if self.wealth > 2:
            partner = list(self.model.agents.random(n=1))[0]
            partner.wealth += 1
            self.wealth -= 1

# only transfers to richer
class GreedyAgent(BaseWealthAgent):
    def setup(self):
        super().setup()
        self.strategy_name = "Greedy"
    
    def wealth_transfer(self):
        if self.wealth > 0:
            richer_partners = [agent for agent in self.model.agents if agent.wealth > self.wealth]
            if richer_partners:
                partner = random.choice(richer_partners)
                partner.wealth += 1
                self.wealth -= 1

# only to poorer
class CharitableAgent(BaseWealthAgent):
    def setup(self):
        super().setup()
        self.strategy_name = "Charitable"
    
    def wealth_transfer(self):
        if self.wealth > 0:
            poorest = min(self.model.agents, key=lambda x: x.wealth)
            if poorest.wealth < self.wealth:
                poorest.wealth += 1
                self.wealth -= 1

# multiple transfer if possible
class RiskTakingAgent(BaseWealthAgent):
    def setup(self):
        super().setup()
        self.strategy_name = "RiskTaker"
        self.wealth = 4  
    
    def wealth_transfer(self):
        if self.wealth > 2:
            partner = list(self.model.agents.random(n=1))[0]
            transfer = min(self.wealth - 1, 3)  
            partner.wealth += transfer
            self.wealth -= transfer

# Agent all-or-nothing
class AllOrNothingAgent(BaseWealthAgent):
    def setup(self):
        super().setup()
        self.strategy_name = "AllOrNothing"
        self.wealth = 100
    
    def wealth_transfer(self):
        if self.wealth > 0:
            partner = list(self.model.agents.random(n=1))[0]
            a = partner.wealth
            partner.wealth -= a
            self.wealth += a

# Gini function
def gini(x):
    """ Calculate Gini Coefficient """
    x = np.array(x)
    mad = np.abs(np.subtract.outer(x, x)).mean()  
    rmad = mad / np.mean(x)  
    return 0.5 * rmad

# Transfer Model
class WealthModel(ap.Model):
    """ A model of wealth transfers between different agent strategies """
    
    def setup(self):
        
        self.agents = ap.AgentList(self, self.p.agents['Base'], BaseWealthAgent) + \
                      ap.AgentList(self, self.p.agents['Conservative'], ConservativeAgent) + \
                      ap.AgentList(self, self.p.agents['Greedy'], GreedyAgent) + \
                      ap.AgentList(self, self.p.agents['Charitable'], CharitableAgent) + \
                      ap.AgentList(self, self.p.agents['RiskTaker'], RiskTakingAgent) + \
                      ap.AgentList(self, self.p.agents['AllOrNothing'], AllOrNothingAgent)

    def step(self):
        self.agents.wealth_transfer()  # each agent does 1 transfer

    def update(self):
        # Gini calculate
        wealths = [agent.wealth for agent in self.agents]
        self.record('Gini Coefficient', gini(wealths))

    def end(self):
        
        self.agents.record('wealth')

# Hyper-parameters
parameters = {
    'agents': {
        'Base': 10,
        'Conservative': 20,
        'Greedy': 20,
        'Charitable': 20,
        'RiskTaker': 15,
        'AllOrNothing': 0
    },
    'steps': 100,
    'seed': 42,
}


model = WealthModel(parameters)
results = model.run()

data = results.variables.WealthModel
ax = data.plot()

# Extraire les données de richesse et le type d'agent pour chaque agent après la simulation
agent_data = [(agent.strategy_name, agent.wealth) for agent in model.agents]
df = pd.DataFrame(agent_data, columns=["Agent Type", "Wealth"])


# Créer un histogramme de la répartition de la richesse pour chaque type d'agent
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Wealth", hue="Agent Type", multiple="dodge", binwidth=1)
plt.title("Distribution of Wealth by Agent Type")
plt.xlabel("Wealth")
plt.ylabel("Count of Agents")
plt.savefig('plot.png')

plt.show()


# A grandes rasgos nos gustaría dicir que el modelo de simulación de agentes sobre 
# la transferencia de riqueza revela que las diferentes estrategias de los agentes,
# como los caritativos, codiciosos y arriesgados, impactan significativamente la 
# distribución de la riqueza. Por ejemplo, los agentes caritativos tienden a 
# reducir la desigualdad al transferir riqueza a los más pobres, mientras que los 
# codiciosos concentran la riqueza entre los más ricos. El coeficiente de Gini, 
# que mide la desigualdad, puede indicar una mayor concentración de riqueza en 
# poblaciones con muchos agentes codiciosos.


