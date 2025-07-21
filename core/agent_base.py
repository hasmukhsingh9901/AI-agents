from abc import ABC, abstractmethod

class AgentBase(ABC):
    def __init__(self, context=None):
        self.context = context

    @abstractmethod
    def run(self, input_data):
        """
        Run the agent with the provided input data.
        
        :param input_data: The data to process.
        :return: The result of processing the input data.
        """
        pass