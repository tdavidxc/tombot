import subprocess
from llm.client import LLMClient

class OllamaClient(LLMClient):
    def __init__(self, model: str = "mistral"):
        self.model = model

    def generate(self, prompt: str) -> str:
        result = subprocess.run(
            ["ollama", "run", self.model],
            input=prompt,
            text=True,
            encoding="utf-8",
            capture_output=True
        )
        if result.stderr:
            print("LLM stderr:", result.stderr)


        return result.stdout.strip()