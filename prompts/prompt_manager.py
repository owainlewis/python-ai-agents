import os
from pathlib import Path
from typing import Any, Dict

from jinja2 import Environment, FileSystemLoader, select_autoescape


class PromptManager:
    # Get the absolute path to the prompts directory using pathlib
    PROMPTS_DIR = Path(__file__).parent

    # Create Jinja2 environment
    _env = Environment(
        loader=FileSystemLoader(PROMPTS_DIR),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    @staticmethod
    def load_prompt(template_name: str, variables: Dict[str, Any] = None) -> str:
        """
        Load and render a prompt template from a .j2 file.

        Args:
            template_name (str): Name of the template file (with or without .j2 extension)
            variables (Dict[str, Any], optional): Variables to render in the template

        Returns:
            str: The rendered prompt

        Example:
            prompt = PromptManager.load_prompt('example.j2', {'name': 'Alice'})
        """
        if not template_name.endswith(".j2"):
            template_name = f"{template_name}.j2"

        try:
            template = PromptManager._env.get_template(template_name)
            return template.render(**(variables or {}))
        except Exception as e:
            raise Exception(
                f"Failed to load prompt template '{template_name}': {str(e)}"
            )

    @staticmethod
    def list_templates() -> list[str]:
        """
        List all available prompt templates in the prompts directory.

        Returns:
            list[str]: List of template filenames
        """
        return [f.name for f in PromptManager.PROMPTS_DIR.glob("*.j2")]

    @staticmethod
    def get_template_path(template_name: str) -> Path:
        """
        Get the full path to a template file.

        Args:
            template_name (str): Name of the template file

        Returns:
            Path: Full path to the template file
        """
        if not template_name.endswith(".j2"):
            template_name = f"{template_name}.j2"
        return PromptManager.PROMPTS_DIR / template_name
