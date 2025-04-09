from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from dotenv import load_dotenv

load_dotenv()

model = OpenAIModel("gpt-4o")

agent = Agent(model, system_prompt="You are a helpful assistant.")

result_sync = agent.run_sync("What is the capital of Italy?")

print(result_sync.data)
