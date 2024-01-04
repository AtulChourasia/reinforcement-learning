import gymnasium as gym

env = gym.make("ALE/Pong-v5",render_mode="human")

print(env.action_space)
print(env.observation_space)
# print(env.P[6][3])
env.reset()
num_episode = 100
num_timestep = 50
for i in range(num_episode):
    action = env.action_space.sample()
    print(env.step(action))     
env.close()