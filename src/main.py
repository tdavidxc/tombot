from llm.client import MockLLMClient
from persona.persona import DEFAULT_PERSONA, PersonaInfoGetter


def build_prompt(persona_prompt: str, user_input: str) -> str:
    return (
        f"{persona_prompt}\n"
        f"Conversation:\n"
        f"user: {user_input}\n"
        f"{PersonaInfoGetter.get_bot_name()}:"
    )


def main():
    llm = MockLLMClient()
    persona_prompt = DEFAULT_PERSONA.to_prompt()
    print(f"{PersonaInfoGetter.get_bot_name()}: Hey")

    while True:
        user_input = input("> ").strip()
        if not user_input:
            continue
        prompt = build_prompt(persona_prompt, user_input)
        response = llm.generate(prompt)
        print(f"{PersonaInfoGetter.get_bot_name()}: {response}")

if __name__ == "__main__":
    main()