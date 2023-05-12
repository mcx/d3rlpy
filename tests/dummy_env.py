from typing import Any, Dict, Tuple

import gym
import numpy as np
from gym.spaces import Box, Discrete


class DummyAtari(gym.Env[Any, Any]):
    def __init__(self, grayscale: bool = True, squeeze: bool = False):
        if grayscale:
            shape = (84, 84) if squeeze else (84, 84, 1)
        else:
            shape = (84, 84, 3)
        self.observation_space = Box(
            low=np.zeros(shape),
            high=np.zeros(shape) + 255,
            dtype=np.uint8,
        )
        self.action_space = Discrete(4)
        self.t = 1

    def step(
        self, action: Any
    ) -> Tuple[Any, float, bool, bool, Dict[str, Any]]:
        observation = self.observation_space.sample()
        reward = np.random.random()
        return observation, reward, False, self.t % 80 == 0, {}

    def reset(self, **kwargs: Any) -> Tuple[Any, Dict[str, Any]]:
        self.t = 1
        return self.observation_space.sample(), {}
