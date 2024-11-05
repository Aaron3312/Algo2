


import agentpy as ap
import numpy as np
import seaborn as sns
import random
import pandas as pd
import matplotlib.pyplot as plt

# [Previous agent classes and model definitions remain exactly the same until the plotting section]

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

# Modified GreedyAgent with utility tracking
class GreedyAgent(ap.Agent):
    def setup(self):
        self.strategy_name = "Greedy"
        self.wealth = 1
        self.previous_wealth = 1
        self.state_utility = 0  # Utility based on state changes
        self.cumulative_utility = 1  # Utility based on total wealth
        
    def wealth_transfer(self):
        self.previous_wealth = self.wealth
        if self.wealth > 0:
            richer_partners = [agent for agent in self.model.agents if agent.wealth > self.wealth]
            if richer_partners:
                partner = random.choice(richer_partners)
                partner.wealth += 1
                self.wealth -= 1
        
        # Calculate utilities
        # State utility: +1 if wealth increased, -1 if decreased, 0 if unchanged
        wealth_change = self.wealth - self.previous_wealth
        if wealth_change > 0:
            self.state_utility += 1
        elif wealth_change < 0:
            self.state_utility -= 1
            
        # Cumulative utility is just the current wealth
        self.cumulative_utility = self.wealth


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
        self.wealth = 10
    
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

class WealthModel(ap.Model):
    def setup(self):
        self.agents = ap.AgentList(self, self.p.agents['Base'], BaseWealthAgent) + \
                     ap.AgentList(self, self.p.agents['Conservative'], ConservativeAgent) + \
                     ap.AgentList(self, self.p.agents['Greedy'], GreedyAgent) + \
                     ap.AgentList(self, self.p.agents['Charitable'], CharitableAgent) + \
                     ap.AgentList(self, self.p.agents['RiskTaker'], RiskTakingAgent) + \
                     ap.AgentList(self, self.p.agents['AllOrNothing'], AllOrNothingAgent)
        
        # Initialize lists to store utility history
        self.state_utility_history = []
        self.cumulative_utility_history = []
        
    def step(self):
        self.agents.wealth_transfer()
        
        # Record utilities of Greedy agents
        greedy_agents = [agent for agent in self.agents if agent.strategy_name == "Greedy"]
        state_utilities = [agent.state_utility for agent in greedy_agents]
        cumulative_utilities = [agent.cumulative_utility for agent in greedy_agents]
        
        self.state_utility_history.append(state_utilities)
        self.cumulative_utility_history.append(cumulative_utilities)

    def update(self):
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

# Run model
model = WealthModel(parameters)
results = model.run()

# Create DataFrames for plotting
steps = range(parameters['steps'])

# Process state utility data
state_df = pd.DataFrame()
for agent_idx in range(len(model.state_utility_history[0])):
    agent_utility = [step_utility[agent_idx] for step_utility in model.state_utility_history]
    state_df[f'Agent {agent_idx+1}'] = agent_utility
state_df['Average'] = state_df.mean(axis=1)

# Process cumulative utility data
cumulative_df = pd.DataFrame()
for agent_idx in range(len(model.cumulative_utility_history[0])):
    agent_utility = [step_utility[agent_idx] for step_utility in model.cumulative_utility_history]
    cumulative_df[f'Agent {agent_idx+1}'] = agent_utility
cumulative_df['Average'] = cumulative_df.mean(axis=1)

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Plot state-based utility
for column in state_df.columns[:-1]:
    ax1.plot(steps, state_df[column], alpha=0.3, color='gray', linewidth=1)
ax1.plot(steps, state_df['Average'], color='red', linewidth=2, label='Average State Utility')
ax1.set_title('State-Based Utility Over Time (Greedy Agents)')
ax1.set_xlabel('Time Steps')
ax1.set_ylabel('State Utility\n(+1 for gain, -1 for loss)')
ax1.grid(True, alpha=0.3)
ax1.legend()

# Plot cumulative utility
for column in cumulative_df.columns[:-1]:
    ax2.plot(steps, cumulative_df[column], alpha=0.3, color='gray', linewidth=1)
ax2.plot(steps, cumulative_df['Average'], color='blue', linewidth=2, label='Average Cumulative Utility')
ax2.set_title('Cumulative Utility Over Time (Greedy Agents)')
ax2.set_xlabel('Time Steps')
ax2.set_ylabel('Cumulative Utility\n(Total Wealth)')
ax2.grid(True, alpha=0.3)
ax2.legend()

# Add final statistics
final_state_mean = state_df['Average'].iloc[-1]
final_cumulative_mean = cumulative_df['Average'].iloc[-1]

stats_text = f'Final Statistics:\n'
stats_text += f'Avg State Utility: {final_state_mean:.2f}\n'
stats_text += f'Avg Cumulative Utility: {final_cumulative_mean:.2f}'

plt.figtext(0.02, 0.02, stats_text,
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig('greedy_agents_utility.png')
plt.show()

# Print summary statistics
print("\nFinal Utility Statistics for Greedy Agents:")
print(f"Average State Utility: {final_state_mean:.2f}")
print(f"Average Cumulative Utility: {final_cumulative_mean:.2f}")