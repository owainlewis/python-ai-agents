from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from dotenv import load_dotenv

load_dotenv()

model = OpenAIModel("gpt-4o")

agent = Agent(
    model,
    system_prompt="You are a helpful assistant. Use the name_generator tool to generate a name.",
)


@agent.tool_plain
def name_generator(name: str) -> str:
    """Generate a name from a given string."""
    return name.upper()


def agent_loop():
    messages = None
    while True:
        user_input = input("User: ")
        if user_input == "exit":
            break

        if messages is None:
            result = agent.run_sync(user_input)
            messages = result.all_messages()
        else:
            result = agent.run_sync(user_input, message_history=messages)
            messages = result.all_messages()

        print(result.data)


if __name__ == "__main__":
    agent_loop()
