from abc import ABC, abstractmethod


class LLMClient(ABC):
    """
    Abstract base class for all LLM backends so that they implement a common interface for any LLM client.
    """

    #generate takes a prompt string and returns the generated string
    @abstractmethod
    def generate(self, prompt: str) -> str: 
        pass



# A mock implementation of LLMClient for testing purposes
class MockLLMClient(LLMClient):
    
    def generate(self, prompt: str) -> str:
        return (
            "lol yeah that makes sense\n"
            "(mock response for now)"
        )
