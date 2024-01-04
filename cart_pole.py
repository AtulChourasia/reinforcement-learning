import gymnasium as gym

env = gym.make("MountainCar-v0",render_mode="human")

num_episode = 100
num_timestep = 50

for i in range(num_episode):
    Return = 0
    state = env.reset()
    for j in range(num_timestep):
        action = env.action_space.sample()
        ns, r, ter, tru, info =env.step(action)
        Return = Return + r
        
        if ter:
            break
    if i%10 == 0:
        print("episode :{} reward :{}".format(i,Return))
    