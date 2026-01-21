from llm.client import MockLLMClient

def main():
    llm = MockLLMClient()

    while True:
        user_input = input("> ")
        # if user_input.lower() in {"exit", "quit"}: #not having break or exit conditions because in general convo, conversations are continuous
        #     break

        response = llm.generate(user_input)
        print(f"bot: {response}")

if __name__ == "__main__":
    main()