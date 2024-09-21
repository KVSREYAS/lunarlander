<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
</head>
<body style="font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4; color: #333;">
    <div style="width: 80%; margin: 20px auto; background-color: #fff; padding: 20px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
        <h1 style="color: #555;">Lunar Lander Reinforcement Learning Project</h1>
        <p>This project involves training an agent using Deep Q-Learning to play the Lunar Lander game, a classic OpenAI Gym environment. The goal is to safely land the lunar module on the landing pad while avoiding crashes and conserving fuel.</p>
        <h2 style="color: #555;">Project Overview</h2>
        <p>The agent is trained using a neural network to approximate the Q-values for each possible action. The network consists of three fully connected layers with ReLU activations. The agent uses an epsilon-greedy policy to explore the environment, gradually shifting from exploration to exploitation as the training progresses.</p>
        <h2 style="color: #555;">Deep Q-Network Architecture</h2>
        <ul>
            <li><strong>Input Layer:</strong> 8-dimensional state space representing the lunar lander's position, velocity, and angle.</li>
            <li><strong>Hidden Layers:</strong> Two fully connected layers with 256 neurons each, using ReLU activations.</li>
            <li><strong>Output Layer:</strong> 4-dimensional action space representing the discrete actions the lander can take.</li>
        </ul>
        <h2 style="color: #555;">Training Process</h2>
        <p>The training process involves the following steps:</p>
        <ol>
            <li>Initialize the replay memory to store the agent's experiences.</li>
            <li>For each episode, the agent interacts with the environment by choosing an action based on the epsilon-greedy policy.</li>
            <li>Store the transition (state, action, reward, next state, done) in the replay memory.</li>
            <li>Sample a batch of transitions from the memory and update the Q-network using the Bellman equation.</li>
            <li>Repeat the process until the agent's performance stabilizes or a predefined number of episodes is reached.</li>
        </ol>
        <h2 style="color: #555;">Results</h2>
        <p>The agent was trained for 500 episodes. During the training, the agent learned to successfully land the lunar module by minimizing fuel consumption and avoiding crashes. Below is a graph of the agent's performance over time.</p>
        <img src="path_to_your_image.png" alt="Training Performance" style="display: block; margin: 20px auto; max-width: 100%; height: auto;">
        <h2 style="color: #555;">Watch the Agent in Action</h2>
        <p>Below is a short video demonstrating the agent's performance in the Lunar Lander environment:</p>
        <video controls style="display: block; margin: 20px auto; max-width: 100%; height: auto;">
            <source src="https://github.com/KVSREYAS/lunarlander/blob/main/result_demo.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <h2 style="color: #555;">Future Work</h2>
        <p>Future improvements could include:</p>
        <ul>
            <li>Using a more advanced neural network architecture such as a Double DQN or Dueling DQN.</li>
            <li>Implementing prioritized experience replay to improve the efficiency of the learning process.</li>
            <li>Testing the agent in different variations of the Lunar Lander environment or applying the same approach to other reinforcement learning problems.</li>
        </ul>
        <div style="text-align: center; margin-top: 30px; font-size: 0.9em; color: #777;">
            <p>&copy; 2024 Your Name. All rights reserved.</p>
        </div>
    </div>
</body>
</html>

