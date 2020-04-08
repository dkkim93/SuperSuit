import numpy as np
from gym.spaces import Box

def check_param(obs_space, new_dtype):
    assert isinstance(new_dtype, type) or isinstance(new_dtype, np.dtype), "new_dtype must be type. It is {}".format(new_dtype)

def change_observation(obs,new_dtype):
    obs = obs.astype(new_dtype)
    return obs