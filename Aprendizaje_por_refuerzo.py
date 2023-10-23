import random

# Definición del entorno (Entorno de cuadrícula simple)
class Environment:
    def __init__(self):
        self.grid_size = 5
        self.goal_state = (4, 4)
    
    def is_valid_state(self, state):
        x, y = state
        return 0 <= x < self.grid_size and 0 <= y < self.grid_size
    
    def get_reward(self, state):
        if state == self.goal_state:
            return 1.0
        return 0.0

# Definición del agente
class Agent:
    def __init__(self):
        self.state = (0, 0)
    
    def choose_action(self, environment):
        # Política simple: elige una acción aleatoria
        possible_actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        action = random.choice(possible_actions)
        new_state = (self.state[0] + action[0], self.state[1] + action[1])
        
        if environment.is_valid_state(new_state):
            self.state = new_state
        return action

# Proceso de aprendizaje por refuerzo
def reinforcement_learning(agent, environment, num_episodes):
    for episode in range(num_episodes):
        total_reward = 0
        while True:
            action = agent.choose_action(environment)
            new_state = (agent.state[0] + action[0], agent.state[1] + action[1])
            reward = environment.get_reward(new_state)
            total_reward += reward
            agent.state = new_state

            if new_state == environment.goal_state:
                break

        print(f"Episodio {episode + 1}: Recompensa total = {total_reward}")

# Ejecución
if __name__ == "__main__":
    env = Environment()
    agent = Agent()
    num_episodes = 10  # Número de episodios de entrenamiento
    
    print("Entorno de cuadrícula:")
    for row in range(env.grid_size):
        row_str = ""
        for col in range(env.grid_size):
            if (row, col) == env.goal_state:
                row_str += "G "
            else:
                row_str += "_ "
        print(row_str)

    print("\nEntrenamiento del agente:")
    reinforcement_learning(agent, env, num_episodes)
