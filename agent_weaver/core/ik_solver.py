"""Inverse Kinematics Solver"""
import numpy as np
from dataclasses import dataclass

@dataclass
class Point3D:
    x: float
    y: float
    z: float

class IKSolver:
    def __init__(self):
        self.leg_lengths = (35.0, 55.0, 75.0)

    def solve(self, leg_index, target):
        return Point3D(0, 0, -80)
