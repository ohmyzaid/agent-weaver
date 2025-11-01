"""BLE Teleoperation Controller"""
from dataclasses import dataclass

@dataclass
class ControllerInput:
    left_x: float = 0.0
    left_y: float = 0.0
    right_x: float = 0.0
    right_y: float = 0.0

class BLEController:
    pass
