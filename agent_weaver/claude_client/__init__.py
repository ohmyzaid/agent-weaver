"""Claude API Client"""
import os
from dataclasses import dataclass

@dataclass
class Mission:
    name: str
    description: str
    steps: list

class ClaudeMissionPlanner:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")

    def parse_command(self, command):
        return Mission(name=command, description=command, steps=[])
