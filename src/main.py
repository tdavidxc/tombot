from llm.client import MockLLMClient
from persona.persona import DEFAULT_PERSONA, PersonaInfoGetter
from memory.memory import ConversationMemory
from llm.ollama_client import OllamaClient
import random

#hardcoding
LOW_EFFORT_INPUTS = {
    "hi", "hii", "hiii",
    "hey", "heyy",
    "yo",
    "sup",
}

def normalize(text: str) -> str:
    return text.lower().strip()


def build_prompt(persona_prompt: str, memory_prompt: str, user_input: str) -> str:
    return (
        f"{persona_prompt}\n"
        f"Conversation so far:\n"
        f"{memory_prompt}"
        f"{PersonaInfoGetter.get_user_name()}: {user_input}\n"
        f"{PersonaInfoGetter.get_bot_name()}:"
    )


def main():
    llm = OllamaClient(model="mistral") #LLM changer
    persona_prompt = DEFAULT_PERSONA.to_prompt()
    memory = ConversationMemory(max_turns=8)
    print(f"{PersonaInfoGetter.get_bot_name()}: Hey {PersonaInfoGetter.get_user_name()}")

    while True:
        user_input = input(f"{PersonaInfoGetter.get_user_name()}: ").strip()
        if not user_input:
            continue

        normalized = normalize(user_input)
        # 🔒 HARD OVERRIDE FOR GREETINGS
        if normalized in LOW_EFFORT_INPUTS:
            response = random.choice(["hru", "yo", "sup", "hey", "hi", "hii", "hiii", "heyy"])
            memory.add("user", user_input)
            memory.add(PersonaInfoGetter.get_bot_name(), response)
            print(f"{PersonaInfoGetter.get_bot_name()}: {response}")
            continue

        memory.add(PersonaInfoGetter.get_user_name(), user_input)
        prompt = build_prompt(persona_prompt, memory.to_prompt(), user_input)
        response = llm.generate(prompt)
        memory.add(PersonaInfoGetter.get_user_name(), user_input)
        memory.add(PersonaInfoGetter.get_bot_name(), response)


        print(f"{PersonaInfoGetter.get_bot_name()}: {response}")

if __name__ == "__main__":
    main()