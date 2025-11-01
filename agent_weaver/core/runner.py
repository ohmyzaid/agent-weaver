"""Main Control Loop Runner"""
import time

class CrawlerAGI:
    def __init__(self, config):
        self.config = config

    def initialize(self):
        pass

    def start_control_loop(self):
        while True:
            time.sleep(0.02)  # 50Hz
