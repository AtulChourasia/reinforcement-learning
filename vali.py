import gymnasium as gym
env = gym.make("FrozenLake-v1", render_mode="human")
observation, info = env.reset()

print(env.action_space)
print(env.observation_space)
print(env.P[6][3])

num_timestep = 10
num_episode = 5
for i in range(num_episode):
    print("episode number - ",i)
    env.reset()
            
    for j in range(num_timestep):
        action = env.action_space.sample()
        o, r, term, trun,info = env.step(action)
        print(o," ",term," ",info)
        
        if(term):
            break
        
    
        

# for _ in range(1000):
#     action = env.action_space.sample()  # agent policy that uses the observation and info
#     observation, reward, terminated, truncated, info = env.step(action)

#     if terminated or truncated:
#         observation, info = env.reset()

env.close()