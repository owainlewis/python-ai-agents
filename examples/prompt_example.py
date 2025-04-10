from prompts.prompt_manager import PromptManager

# Load and render a template
variables = {
    "name": "User",
    "topic": "AI agents",
    "additional_context": "This is a demo of the prompt system.",
}

# Load the prompt
prompt = PromptManager.load_prompt("example.j2", variables)
print(prompt)

# List all available templates
print("\nAvailable templates:")
print(PromptManager.list_templates())
