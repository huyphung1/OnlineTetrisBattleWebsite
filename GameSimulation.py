from TetrisBattle.envs.tetris_env import TetrisDoubleEnv
from CustomAgent import Agent
import cv2, time
import numpy as np
import pandas as pd

env = TetrisDoubleEnv(gridchoice="none", obs_type="grid", mode="rgb_array")

done = False
state = env.reset()
agent_list = [Agent(), Agent()]

imgs = []

while not done:
    img = env.render(mode='rgb_array') # img is rgb array, you need to render this or can check my colab notebook in readme file
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    imgs.append(img)
    action = agent_list[env.game_interface.getCurrentPlayerID()].choose_action(state)
    state, reward, done, _ = env.step(action)
    print(_)
    env.take_turns()
    cv2.imshow('image', img)
    cv2.waitKey(2)

# print(state.shape)
state = list(state)
state2 = []
for i in state:
    state2.append([])
    for j in i:
        state2[-1].append(j[0])
# print(state2)

# print(np.squeeze(state, 2).shape)
pd.DataFrame(state2).to_csv("data.csv")

out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc(*'DIVX'), 25, (800,600))
for img in imgs:
    cv2.imwrite('img.jpg',img)
    out.write(img)
out.release()

cv2.destroyAllWindows()