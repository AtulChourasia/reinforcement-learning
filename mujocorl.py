import gymnasium as gym

env = gym.make("Ant-v4",render_mode="human")

for i in range(100):
    action = env.action_space.sample()
    env.step(action)    
env.close()