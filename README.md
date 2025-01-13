# OpenAI API Sandbox

This repository contains examples and experiments using the OpenAI API.

## Setup

1. Create the conda environment:
```bash
conda env create -f environment.yml
```

2. Activate the environment:
```bash
conda activate sandbox-openai
```

3. Copy the `.env.example` file to `.env` and add your OpenAI API key:
```bash
cp .env.example .env
```

4. Edit the `.env` file and replace `your-api-key-here` with your actual OpenAI API key.

## Running Examples

To run the example script:
```bash
python src/example.py
```
