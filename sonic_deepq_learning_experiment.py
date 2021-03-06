# -*- coding: utf-8 -*-
"""sonic-deepq-learning/experiment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z4IUxUtPWAf8xz6PCY672reMz2lFjnPW
"""

!apt-get install pkg-config lua5.1 build-essential ffmpeg git

!pip install tqdm retrowrapper gym-retro

!pip install tqdm retrowrapper gym-retro

!pip install -U git+git://github.com/frenchie4111/dumbrain.git

!python -m dumbrain.rl.retro_contest.install_games http://aiml.mikelyons.org/datasets/sonic/Sonic%20Roms.zip

import retro

import retrowrapper
env = retrowrapper.RetroWrapper(
    game='SonicTheHedgehog2-Genesis',
    state='MetropolisZone.Act1'
)

import retrowrapper
import matplotlib.pyplot as plt
observation = env.reset()
for i in range(3600):
  random_action = env.action_space.sample()
  observation, reward, done, info = env.step(
      random_action)
  if done:
         observation = env.reset()
plt.imshow(observation)