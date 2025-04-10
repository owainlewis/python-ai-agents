from prompts.prompt_manager import PromptManager

from datetime import datetime

prompt = PromptManager.load_prompt(
    "prompt", {"time": datetime.now(), "example_1": "Hello, world!"}
)

print(prompt)
