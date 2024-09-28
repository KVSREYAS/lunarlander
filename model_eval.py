import torch as T
import gym
import numpy as np

def evaluate_agent(agent, env, num_games=100, render=False):
    scores = []
    
    for i in range(num_games):
        score = 0
        done = False
        observation, _ = env.reset()
        
        while not done:
            if render:
                env.render()
            action = agent.choose_action(observation)
            observation_, reward, done, info = env.step(action)
            score += reward
            observation = observation_
        
        scores.append(score)
        print(f'Game {i + 1}: Score {score}')
    
    avg_score = np.mean(scores)
    print(f'Average Score over {num_games} games: {avg_score}')
    return avg_score

def main():
    # Set parameters
    eval_games = 100
    render_evaluation = True  # Set to True to visualize evaluation

    # Initialize the agent
    agent = Agent(gamma=0.99, epsilon=0.0, lr=0.002, input_dims=[8], batch_size=64, num_actions=4)
    
    # Load the saved weights
    agent.Q_eval.load_state_dict(T.load('path/to/your/saved_weights.pth'))  # Adjust the path to your weights file
    agent.Q_eval.eval()  # Set the model to evaluation mode

    env = gym.make('LunarLander-v2')

    # Evaluate the agent
    evaluate_agent(agent, env, eval_games, render=render_evaluation)

if __name__ == "__main__":
    main()
