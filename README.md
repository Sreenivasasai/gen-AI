# gen-AI


This project demonstrates the implementation of an AI-powered application using LangChain and Groq APIs. It integrates large language models to process user queries and generate intelligent responses.

## Features

* AI-powered text generation
* LangChain integration
* Groq LLM support
* Environment-based configuration
* Easy deployment and setup

## Tech Stack

* Python
* LangChain
* Groq API
* Environment Variables (.env)

## Installation

```bash
git clone <repository-url>
cd <project-folder>
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file and add the required API keys:

```env
GROQ_API_KEY=your_api_key
LANGCHAIN_API_KEY=your_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=ProjectName
```

## Run the Project

```bash
python app.py
```

## Project Structure

```text
project/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── src/
```

## Future Enhancements

* Multi-model support
* Chat history management
* Advanced prompt engineering
* Deployment on cloud platforms

