<div align="center">
  <img src="logo.png" alt="sandbox-openai" width="512"/>

  [![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
  [![OpenAI](https://img.shields.io/badge/OpenAI-API-412991.svg)](https://openai.com/)
  [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

  **🤖 Sandbox for OpenAI API experiments and examples 🧪**

</div>

## Overview

sandbox-openai is a ready-to-use environment for exploring OpenAI's API capabilities. It provides a clean project structure with conda environment management and secure API key configuration, so you can focus on experimentation rather than setup.

## Features

- **Zero-friction setup** - Single command activates environment and installs dependencies
- **Secure configuration** - API keys stored in `.env` (git-ignored)
- **Modern Python** - Uses Python 3.10 with type hints and latest OpenAI SDK
- **GPT-4o ready** - Pre-configured example using the latest model

## Quick Start

```bash
# Clone and enter the repository
git clone https://github.com/tsilva/sandbox-openai.git
cd sandbox-openai

# Setup environment (creates conda env if needed and activates it)
source activate-env.sh

# Configure your API key
cp .env.example .env
# Edit .env and add your OpenAI API key

# Run the example
python main.py
```

## Installation

### Prerequisites

- [Conda](https://docs.conda.io/en/latest/miniconda.html) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- An [OpenAI API key](https://platform.openai.com/api-keys)

### Automated Setup (Recommended)

```bash
source activate-env.sh
```

This script automatically:
- Creates the conda environment from `environment.yml` if it doesn't exist
- Activates the `sandbox-openai` environment
- Must be sourced (not executed directly)

### Manual Setup

```bash
conda env create -f environment.yml
conda activate sandbox-openai
cp .env.example .env
# Edit .env to add your OpenAI API key
```

## Usage

The main entry point demonstrates a basic chat completion:

```python
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

client = OpenAI()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o",
)
print(chat_completion)
```

Run it with:

```bash
python main.py
```

## Project Structure

```
sandbox-openai/
├── main.py              # Example OpenAI API usage
├── environment.yml      # Conda environment specification
├── activate-env.sh      # Automated setup script
├── .env.example         # Template for API credentials
└── .env                 # Your API credentials (git-ignored)
```

## Dependencies

| Package | Purpose |
|---------|---------|
| `openai` | Official OpenAI Python SDK |
| `python-dotenv` | Load environment variables from `.env` |
| `requests` | HTTP library for custom API calls |

## License

MIT
