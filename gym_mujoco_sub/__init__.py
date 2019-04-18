#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:52:00 2019

@author: Shukai
"""

from gym.envs.registration import register

register(
    id='foo-v0',
    entry_point='gym_foo.envs:MujocoEnv',
)
# =============================================================================
# register(
#     id='foo-extrahard-v0',
#     entry_point='gym_foo.envs:MujocoExtraHardEnv',
# )
# =============================================================================
