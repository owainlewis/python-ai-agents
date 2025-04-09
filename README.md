# AI Agents Python

A simple project exploring AI agents with Pydantic AI.

## Setup

1. Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

2. Add your OpenAI credentials to `.env`:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `OPENAI_ORGANIZATION`: Your OpenAI organization ID (found in OpenAI dashboard)

3. Source your environment variables:
```bash
source .env
```

4. Install dependencies with uv:
```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

5. Run the example:
```bash
python 1-basic.py
```