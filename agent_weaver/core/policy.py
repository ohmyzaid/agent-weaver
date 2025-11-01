"""RL Policy Module"""
import numpy as np
from enum import Enum

class GaitType(Enum):
    TRIPOD = "tripod"
    WAVE = "wave"

class RLPolicy:
    def __init__(self, policy_type="ppo"):
        self.policy_type = policy_type
