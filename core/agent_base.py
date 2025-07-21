from abc import ABC, abstractmethod

class AgentBase(ABC):
    def __init__(self, context=None):
        self.context = context

    @abstractmethod
    def run(self, input_data):
        pass
