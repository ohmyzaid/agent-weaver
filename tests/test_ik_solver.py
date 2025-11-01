import pytest
import numpy as np
from agent_weaver.core.ik_solver import IKSolver, Point3D

class TestIKSolver:
    def setup_method(self):
        self.ik_solver = IKSolver()

    def test_home_position(self):
        for leg in range(6):
            joints = self.ik_solver.solve(leg, Point3D(0, 0, -80))
            assert joints is not None
