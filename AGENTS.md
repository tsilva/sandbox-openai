# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an OpenAI API sandbox repository for experiments and examples. The project uses Python 3.10 with conda environment management and python-dotenv for API key configuration.

## Environment Setup

**Initial setup:**
```bash
source activate-env.sh
```

The `activate-env.sh` script automatically:
- Creates the conda environment from `environment.yml` if it doesn't exist
- Activates the `sandbox-openai` conda environment
- Must be sourced (not executed directly)

**Manual setup:**
```bash
conda env create -f environment.yml
conda activate sandbox-openai
cp .env.example .env
# Then edit .env to add your OpenAI API key
```

## Running Code

The main entry point is `main.py`:
```bash
python main.py
```

This demonstrates a basic OpenAI chat completion using the gpt-4o model.

## Architecture

- **Environment Management**: Uses conda with `environment.yml` for dependency management
- **Configuration**: API credentials stored in `.env` (git-ignored) using python-dotenv
- **OpenAI Client**: Initialized in main.py, API key automatically loaded from environment variables

## Key Files

- `main.py` - Example OpenAI API usage (chat completion)
- `environment.yml` - Conda environment specification (python-dotenv, openai, requests)
- `activate-env.sh` - Automated environment setup and activation script
- `.env` - API credentials (create from `.env.example`)

## Important Instructions

- README.md must be kept up to date with any significant project changes
- Always use the `readme-generator` skill to author README files
