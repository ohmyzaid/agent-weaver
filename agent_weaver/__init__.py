"""
Agent Weaver - AGI-Driven Hexapod Locomotion Platform

A hexapod robot that thinks before it moves. Combines Claude AI reasoning
with reinforcement learning-based locomotion policies for adaptive terrain
navigation.
"""

__version__ = "1.0.0"
__author__ = "Crawler AGI Team"

from agent_weaver.core.runner import CrawlerAGI
from agent_weaver.core.policy import RLPolicy, GaitType
from agent_weaver.core.ik_solver import IKSolver
from agent_weaver.configs import CrawlerConfig

__all__ = [
    "CrawlerAGI",
    "RLPolicy",
    "GaitType",
    "IKSolver",
    "CrawlerConfig",
]
