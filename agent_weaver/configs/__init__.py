"""Configuration module"""
from dataclasses import dataclass

@dataclass
class CrawlerConfig:
    esp32_host: str = "192.168.1.100"
    control_frequency: int = 50
