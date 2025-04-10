from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from dotenv import load_dotenv
from typing import List
import httpx
import os
from datetime import datetime
from promptly_ai import PromptManager

load_dotenv()

model = OpenAIModel("gpt-4o")

system_prompt = PromptManager.render(
    "prompts/system.j2", time=datetime.now().isoformat()
)

agent = Agent(model, system_prompt=system_prompt)


@agent.tool_plain
def search_google(query: str) -> List[str]:
    """
    Search the web for the given query and return the top results.

    Args:
        query: The query to search for.

    Returns:
        The top search results
    """
    print(f"Searching Google {query}")
    api_key = os.getenv("SERPER_API_KEY")
    assert api_key, "Please set API key for serper"
    search_results = httpx.get(
        f"https://google.serper.dev/search?apiKey={api_key}&q={query}"
    ).json()

    results = []
    for item in search_results["organic"]:
        results.append(f"Title: {item['title']}\nSnippet: {item['snippet']}")

    return results


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
