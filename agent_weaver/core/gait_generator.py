"""Gait Pattern Generator"""
import numpy as np

class GaitGenerator:
    def __init__(self, gait_type="tripod"):
        self.gait_type = gait_type
        self.cycle_phase = 0.0

    def step(self, dt, params):
        self.cycle_phase += dt / params.cycle_time

    def get_foot_positions(self, phase, params):
        return [None] * 6
