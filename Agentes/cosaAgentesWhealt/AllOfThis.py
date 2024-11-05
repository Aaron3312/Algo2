import agentpy as ap
import numpy as np
import seaborn as sns
import random
import pandas as pd
import matplotlib.pyplot as plt


class BaseWealthAgent(ap.Agent):
    """ Base agent with wealth """
    def setup(self):
        self.wealth = 1
        self.strategy_name = "Base"
        self.previous_wealth = 1
        self.state_utility = 0
        self.cumulative_utility = 1
    
    def wealth_transfer(self):
        self.previous_wealth = self.wealth
        # Base agents don't transfer, but still track utility
        # For base agents, utility is just wealth preservation
        wealth_change = self.wealth - self.previous_wealth
        self.state_utility += 1 if wealth_change >= 0 else -1
        self.cumulative_utility = self.wealth

class ConservativeAgent(BaseWealthAgent):
    def setup(self):
        self.strategy_name = "Conservative"
        self.wealth = 2
        self.previous_wealth = 2
        self.state_utility = 0
        self.cumulative_utility = 2
        self.safety_threshold = 2  # Track if we maintain safety threshold
    
    def wealth_transfer(self):
        self.previous_wealth = self.wealth
        if self.wealth > 2:
            partner = list(self.model.agents.random(n=1))[0]
            partner.wealth += 1
            self.wealth -= 1
        
        # Conservative utility: +2 if above safety threshold, -2 if below
        if self.wealth >= self.safety_threshold:
            self.state_utility += 2
        else:
            self.state_utility -= 2
            
        # Cumulative utility weighs safety more than total wealth
        self.cumulative_utility = self.wealth * (1.5 if self.wealth >= self.safety_threshold else 0.5)

class GreedyAgent(ap.Agent):
    def setup(self):
        self.strategy_name = "Greedy"
        self.wealth = 1
        self.previous_wealth = 1
        self.state_utility = 0
        self.cumulative_utility = 1
        
    def wealth_transfer(self):
        self.previous_wealth = self.wealth
        if self.wealth > 0:
            richer_partners = [agent for agent in self.model.agents if agent.wealth > self.wealth]
            if richer_partners:
                partner = random.choice(richer_partners)
                partner.wealth += 1
                self.wealth -= 1
        
        wealth_change = self.wealth - self.previous_wealth
        if wealth_change > 0:
            self.state_utility += 1
        elif wealth_change < 0:
            self.state_utility -= 1
            
        self.cumulative_utility = self.wealth

class CharitableAgent(BaseWealthAgent):
    def setup(self):
        self.strategy_name = "Charitable"
        self.wealth = 1
        self.previous_wealth = 1
        self.state_utility = 0
        self.cumulative_utility = 1
        self.donations_made = 0  # Track number of successful donations
        self.previous_donations_made = 0  # Añadido esta línea



    def wealth_transfer(self):
        self.previous_wealth = self.wealth
        if self.wealth > 0:
            poorest = min(self.model.agents, key=lambda x: x.wealth)
            if poorest.wealth < self.wealth:
                poorest.wealth += 1
                self.wealth -= 1
                self.donations_made += 1
        
        # Charitable utility: based on donations and helping others
        # +2 for successful donation, -1 for having more wealth than needed
        if self.donations_made > self.previous_donations_made:
            self.state_utility += 2
        elif self.wealth > 2:  # Penalty for hoarding
            self.state_utility -= 1
            
        self.previous_donations_made = self.donations_made
        # Cumulative utility factors in both donations and current wealth
        self.cumulative_utility = (self.donations_made * 2) + self.wealth

class RiskTakingAgent(BaseWealthAgent):
    def setup(self):
        self.strategy_name = "RiskTaker"
        self.wealth = 4
        self.previous_wealth = 4
        self.state_utility = 0
        self.cumulative_utility = 4
        self.successful_risks = 0  # Track successful large transfers
    
    def wealth_transfer(self):
        self.previous_wealth = self.wealth
        if self.wealth > 2:
            partner = list(self.model.agents.random(n=1))[0]
            transfer = min(self.wealth - 1, 3)
            partner.wealth += transfer
            self.wealth -= transfer
            if transfer >= 2:  # Consider it a successful risk if transfer is large
                self.successful_risks += 1
        
        # Risk taker utility: rewards big swings in wealth
        wealth_change = abs(self.wealth - self.previous_wealth)
        self.state_utility += wealth_change  # Higher utility for bigger changes
        
        # Cumulative utility factors in both wealth and successful risks
        self.cumulative_utility = self.wealth + (self.successful_risks * 2)

class AllOrNothingAgent(BaseWealthAgent):
    def setup(self):
        self.strategy_name = "AllOrNothing"
        self.wealth = 10
        self.previous_wealth = 10
        self.state_utility = 0
        self.cumulative_utility = 10
        self.big_wins = 0  # Track number of large gains
    
    def wealth_transfer(self):
        self.previous_wealth = self.wealth
        if self.wealth > 0:
            partner = list(self.model.agents.random(n=1))[0]
            a = partner.wealth
            partner.wealth -= a
            self.wealth += a
            
            # Track big wins (gaining more than 5 units)
            if (self.wealth - self.previous_wealth) > 5:
                self.big_wins += 1
        
        # All or Nothing utility: extreme rewards for big gains, big penalties for losses
        wealth_change = self.wealth - self.previous_wealth
        if wealth_change > 5:
            self.state_utility += 5  # Big reward for big gains
        elif wealth_change < -5:
            self.state_utility -= 5  # Big penalty for big losses
        
        # Cumulative utility heavily weights big wins
        self.cumulative_utility = self.wealth + (self.big_wins * 5)


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
                # Initialize a DataFrame to record wealth over time
        self.wealth_history = pd.DataFrame()
        self.step_count = 0  # Initialize step counter
        self.initial_wealth = [agent.wealth for agent in self.agents]  # Wealth at the beginning

        
    def step(self):
        self.agents.wealth_transfer()
        self.record_wealth()  # Record wealth after each step
        self.step_count += 1  # Increment the step count
        
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
        self.evaluate_winners()  # Llama a la función que evalúa los ganadores


    def evaluate_winners(self):
        """ Evaluar quién ha ganado al final de la simulación """
        winners = []
        for i, agent in enumerate(self.agents):
            if agent.wealth > self.initial_wealth[i]:  # Condición de ganancia
                winners.append(agent.strategy_name)
        print(f"Ganan: {winners}")

    def record_wealth(self):
        """ Record the wealth of each agent after each step. """
        wealths = [agent.wealth for agent in self.agents]
        types = [agent.strategy_name for agent in self.agents]
        step_data = pd.DataFrame({'Step': self.step_count, 'Wealth': wealths, 'Agent Type': types})
        self.wealth_history = pd.concat([self.wealth_history, step_data], ignore_index=True)

# Hyper-parameters
parameters = {
    'agents': {
        'Base': 10,
        'Conservative': 10,
        'Greedy': 10,
        'Charitable': 10,
        'RiskTaker': 10,
        'AllOrNothing': 1
    },
    'steps': 100,
    'seed': 42,
}

def plot_detailed_utilities(model, parameters):
    # Create DataFrames for storing utilities of all agent types
    agent_types = ['Base', 'Conservative', 'Greedy', 'Charitable', 'RiskTaker', 'AllOrNothing']
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown']
    agent_colors = dict(zip(agent_types, colors))
    
    # Initialize dictionaries to store utilities by type
    state_utilities = {agent_type: [] for agent_type in agent_types}
    cumulative_utilities = {agent_type: [] for agent_type in agent_types}
    
    # Process utilities for each step
    for step in range(parameters['steps']):
        for agent_type in agent_types:
            agents_of_type = [agent for agent in model.agents if agent.strategy_name == agent_type]
            if agents_of_type:
                state_utilities[agent_type].append([agent.state_utility for agent in agents_of_type])
                cumulative_utilities[agent_type].append([agent.cumulative_utility for agent in agents_of_type])
    
    # Create figure with subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 12))
    
    # Plot state utilities
    for agent_type in agent_types:
        if state_utilities[agent_type]:
            # Plot individual lines
            for agent_idx in range(len(state_utilities[agent_type][0])):
                agent_utility = [step_utilities[agent_idx] for step_utilities in state_utilities[agent_type]]
                ax1.plot(range(parameters['steps']), agent_utility, 
                        color=agent_colors[agent_type], alpha=0.2, linewidth=0.5)
            
            # Plot average line
            means = [sum(step_utilities)/len(step_utilities) for step_utilities in state_utilities[agent_type]]
            ax1.plot(range(parameters['steps']), means, 
                    color=agent_colors[agent_type], linewidth=2.5, label=f'{agent_type} (Avg)')
    
    ax1.set_title('State Utility Over Time by Agent Type', fontsize=14)
    ax1.set_xlabel('Time Steps')
    ax1.set_ylabel('State Utility')
    ax1.grid(True, alpha=0.3)
    ax1.legend(title='Agent Type')
    
    # Plot cumulative utilities
    for agent_type in agent_types:
        if cumulative_utilities[agent_type]:
            # Plot individual lines
            for agent_idx in range(len(cumulative_utilities[agent_type][0])):
                agent_utility = [step_utilities[agent_idx] for step_utilities in cumulative_utilities[agent_type]]
                ax2.plot(range(parameters['steps']), agent_utility, 
                        color=agent_colors[agent_type], alpha=0.2, linewidth=0.5)
            
            # Plot average line
            means = [sum(step_utilities)/len(step_utilities) for step_utilities in cumulative_utilities[agent_type]]
            ax2.plot(range(parameters['steps']), means, 
                    color=agent_colors[agent_type], linewidth=2.5, label=f'{agent_type} (Avg)')
    
    ax2.set_title('Cumulative Utility Over Time by Agent Type', fontsize=14)
    ax2.set_xlabel('Time Steps')
    ax2.set_ylabel('Cumulative Utility')
    ax2.grid(True, alpha=0.3)
    ax2.legend(title='Agent Type')
    
    # Add summary statistics
    stats_text = "Final Statistics:\n"
    for agent_type in agent_types:
        if state_utilities[agent_type] and cumulative_utilities[agent_type]:
            final_state_mean = sum(state_utilities[agent_type][-1])/len(state_utilities[agent_type][-1])
            final_cum_mean = sum(cumulative_utilities[agent_type][-1])/len(cumulative_utilities[agent_type][-1])
            stats_text += f'\n{agent_type}:\n'
            stats_text += f'Avg State Utility: {final_state_mean:.2f}\n'
            stats_text += f'Avg Cumulative Utility: {final_cum_mean:.2f}'
    
    plt.figtext(1.02, 0.5, stats_text, fontsize=10, 
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    return fig



def plot_utilities(model, parameters):
    # Create DataFrames for storing utilities of all agent types
    agent_types = ['Base', 'Conservative', 'Greedy', 'Charitable', 'RiskTaker', 'AllOrNothing']
    
    # Initialize dictionaries to store utilities by type
    state_utilities = {agent_type: [] for agent_type in agent_types}
    cumulative_utilities = {agent_type: [] for agent_type in agent_types}
    
    # Process utilities for each step
    for step in range(parameters['steps']):
        for agent_type in agent_types:
            agents_of_type = [agent for agent in model.agents if agent.strategy_name == agent_type]
            if agents_of_type:  # Check if there are any agents of this type
                state_utilities[agent_type].append([agent.state_utility for agent in agents_of_type])
                cumulative_utilities[agent_type].append([agent.cumulative_utility for agent in agents_of_type])
    
    # Create figure with subplots
    fig = plt.figure(figsize=(20, 15))
    gs = fig.add_gridspec(3, 2, hspace=0.3)
    
    # Plot 1: State Utilities Over Time
    ax1 = fig.add_subplot(gs[0, :])
    for agent_type in agent_types:
        if state_utilities[agent_type]:  # Check if we have data for this type
            means = [sum(step_utilities)/len(step_utilities) for step_utilities in state_utilities[agent_type]]
            ax1.plot(range(parameters['steps']), means, label=agent_type, linewidth=2)
    
    ax1.set_title('Average State Utility Over Time by Agent Type', fontsize=14)
    ax1.set_xlabel('Time Steps')
    ax1.set_ylabel('State Utility')
    ax1.grid(True, alpha=0.3)
    ax1.legend(title='Agent Type')
    
    # Plot 2: Cumulative Utilities Over Time
    ax2 = fig.add_subplot(gs[1, :])
    for agent_type in agent_types:
        if cumulative_utilities[agent_type]:
            means = [sum(step_utilities)/len(step_utilities) for step_utilities in cumulative_utilities[agent_type]]
            ax2.plot(range(parameters['steps']), means, label=agent_type, linewidth=2)
    
    ax2.set_title('Average Cumulative Utility Over Time by Agent Type', fontsize=14)
    ax2.set_xlabel('Time Steps')
    ax2.set_ylabel('Cumulative Utility')
    ax2.grid(True, alpha=0.3)
    ax2.legend(title='Agent Type')
    
    # Plot 3: Final State Utility Distribution
    ax3 = fig.add_subplot(gs[2, 0])
    final_state_data = []
    for agent_type in agent_types:
        if state_utilities[agent_type]:
            final_states = state_utilities[agent_type][-1]
            final_state_data.extend([(agent_type, value) for value in final_states])
    
    final_state_df = pd.DataFrame(final_state_data, columns=['Agent Type', 'Final State Utility'])
    sns.boxplot(data=final_state_df, x='Agent Type', y='Final State Utility', ax=ax3)
    ax3.set_title('Final State Utility Distribution by Agent Type', fontsize=14)
    ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45)
    
    # Plot 4: Final Cumulative Utility Distribution
    ax4 = fig.add_subplot(gs[2, 1])
    final_cumulative_data = []
    for agent_type in agent_types:
        if cumulative_utilities[agent_type]:
            final_cumulatives = cumulative_utilities[agent_type][-1]
            final_cumulative_data.extend([(agent_type, value) for value in final_cumulatives])
    
    final_cumulative_df = pd.DataFrame(final_cumulative_data, 
                                     columns=['Agent Type', 'Final Cumulative Utility'])
    sns.boxplot(data=final_cumulative_df, x='Agent Type', y='Final Cumulative Utility', ax=ax4)
    ax4.set_title('Final Cumulative Utility Distribution by Agent Type', fontsize=14)
    ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45)
    
    # Add summary statistics
    stats_text = "Final Statistics:\n"
    for agent_type in agent_types:
        if state_utilities[agent_type] and cumulative_utilities[agent_type]:
            final_state_mean = sum(state_utilities[agent_type][-1])/len(state_utilities[agent_type][-1])
            final_cum_mean = sum(cumulative_utilities[agent_type][-1])/len(cumulative_utilities[agent_type][-1])
            stats_text += f'\n{agent_type}:\n'
            stats_text += f'Avg State Utility: {final_state_mean:.2f}\n'
            stats_text += f'Avg Cumulative Utility: {final_cum_mean:.2f}\n'
    
    plt.figtext(1.02, 0.5, stats_text, fontsize=10, 
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    return fig


# Run model
model = WealthModel(parameters)
results = model.run()

# fig = plot_utilities(model, parameters)
# plt.show()

fig = plot_detailed_utilities(model, parameters)
plt.show()

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

# Plot wealth history over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=model.wealth_history, x='Step', y='Wealth', hue='Agent Type', marker='o')
print(model.wealth_history)
plt.title('Historia de la Riqueza por Tipo de Agente')
plt.xlabel('Paso')
plt.ylabel('Riqueza')
plt.legend(title='Tipo de Agente')
plt.show()

# Histogram of wealth distribution by agent type after the simulation
agent_data = [(agent.strategy_name, agent.wealth) for agent in model.agents]
df = pd.DataFrame(agent_data, columns=["Agent Type", "Wealth"])

# Create a histogram of the wealth distribution for each agent type
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Wealth", hue="Agent Type", multiple="dodge", binwidth=1)
plt.title("Distribución de la Riqueza por Tipo de Agente")
plt.xlabel("Riqueza")
plt.ylabel("Número de Agentes")
plt.show()


# Print summary statistics
print("\nFinal Utility Statistics for Greedy Agents:")
print(f"Average State Utility: {final_state_mean:.2f}")
print(f"Average Cumulative Utility: {final_cumulative_mean:.2f}")