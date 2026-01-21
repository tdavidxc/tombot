

class ConversationMemory:
    """
    Stores short-term conversation history.
    """

    def __init__(self, max_turns: int = 10):
        self.max_turns = max_turns
        self.history: list[tuple[str, str]] = []

    #adds the latest speaker and message to the history tuple list
    def add(self, speaker: str, message: str) -> None:
        self.history.append((speaker, message))
        if len(self.history) > self.max_turns:
            self.history.pop(0)

    #converts the conversation history into a prompt block
    def to_prompt(self) -> str:
        prompt = ""
        for speaker, message in self.history:
            prompt += f"{speaker}: {message}\n"
        return prompt
