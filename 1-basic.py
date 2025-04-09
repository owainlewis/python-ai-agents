from pydantic_ai import Agent

agent = Agent("openai:gpt-4")

result_sync = agent.run_sync("What is the capital of Italy?")
print(result_sync.data)
