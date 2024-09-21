from Agent import Agent # from agent.py file
import gym
import numpy as np


scores,eps_history=[],[]
games=500      
agent=Agent(gamma=0.99,epsilon=1.0,batch_size=64,num_actions=4,input_dims=[8],lr=0.002)
   
env = gym.make('LunarLander-v2',render_mode='human') # Remove render_mode for faster training without visualization

for i in range(games):
    score=0
    done=False
    safe_threshold=0.5
    observation=env.reset()
    observation=observation[0]
    frames=[]
    actions=[]
    while not done:
        env.render()
        action=agent.choose_action(observation)
        actions.append(action)
        details=env.step(action)
        observation_=details[0]
        reward=details[1]
        crashed=details[2]
        landed=details[3]
        done=landed or crashed
        score+=reward
        agent.store_transition(observation,action,reward,observation_,done)
        agent.learn()
        observation=observation_
        
        frame=env.render()
        frames.append(frame)
    #print(actions)
    if landed:
        print("landed")
    elif crashed:
        print("crashed")
    scores.append(score)
    eps_history.append(agent.epsilon)
    
    avg_score=np.mean(scores[-10:])

    print('epsiode',i,'score %.2f'%score,'avgscore %.2f'%avg_score,'epsilon %.2f'%agent.epsilon,'loss ',agent.loss)
    
    
