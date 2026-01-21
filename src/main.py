from llm.client import MockLLMClient
from persona.persona import DEFAULT_PERSONA, PersonaInfoGetter
from memory.memory import ConversationMemory


def build_prompt(persona_prompt: str, memory_prompt: str, user_input: str) -> str:
    return (
        f"{persona_prompt}\n"
        f"Conversation so far:\n"
        f"{memory_prompt}"
        f"{PersonaInfoGetter.get_user_name()}: {user_input}\n"
        f"{PersonaInfoGetter.get_bot_name()}:"
    )


def main():
    llm = MockLLMClient()
    persona_prompt = DEFAULT_PERSONA.to_prompt()
    memory = ConversationMemory(max_turns=8)
    print(f"{PersonaInfoGetter.get_bot_name()}: Hey")

    while True:
        user_input = input("> ").strip()
        if not user_input:
            continue

        memory.add(PersonaInfoGetter.get_user_name(), user_input)
        prompt = build_prompt(persona_prompt, memory.to_prompt(), user_input)
        response = llm.generate(prompt)
        memory.add(PersonaInfoGetter.get_user_name(), user_input)
        memory.add(PersonaInfoGetter.get_bot_name(), response)


        print(f"{PersonaInfoGetter.get_bot_name()}: {response}")

if __name__ == "__main__":
    main()