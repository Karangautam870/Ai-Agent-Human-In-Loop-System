# AI Agent Chatbot (LangGraph + Streamlit)

## Overview
This folder contains a conversational AI chatbot built with LangGraph and Streamlit. It wires a LangGraph state machine to a Gemini model, supports multi-threaded conversations, and streams responses in real time.

> [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-agent-human-in-loop-system-karangautam870.streamlit.app/)

## Features
- Multi-thread support for managing multiple conversation threads.
- State management with LangGraph for workflow orchestration.
- Real-time streaming of AI responses.

## What Has Been Done So Far
- Implemented a LangGraph chat graph with a single `chat_node`, using `ChatGoogleGenerativeAI` and a typed state with message aggregation.
- Added an in-memory checkpointing strategy (`InMemorySaver`) to support thread-based conversations.
- Built a Streamlit UI with:
  - New chat creation
  - Conversation list in the sidebar
  - Thread titles auto-generated from the first user message
  - Streaming assistant responses to the main chat window
- Added utility functions for thread management and loading prior state from LangGraph.

## Tech Stack

- **LangGraph**: State machine and workflow orchestration
- **LangChain**: LLM framework and integrations
- **Streamlit**: Interactive web interface
- **Google Gemini**: AI model (gemini-2.5-flash)
- **Python 3.13**: Core language

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Karangautam870/Ai-Agent-Human-In-Loop-System.git
cd Ai-Agent-Human-In-Loop-System
```

2. Create a virtual environment:
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install langchain langchain-google-genai langgraph streamlit python-dotenv
```

4. Create `.env` file:
```bash
cp .env.example .env
```

5. Add your API keys to `.env`:
```
GOOGLE_API_KEY=your-google-api-key-here
```

Get your Google API key from: https://makersuite.google.com/app/apikey

## Running Locally

```bash
cd langraph_web
streamlit run frontend.py
```

## Deployment on Streamlit Cloud

1. Push your code to GitHub (without .env file)
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Deploy from GitHub repository
4. Add your API keys in **Secrets** section:
```toml
GOOGLE_API_KEY = "your-google-api-key-here"
```

## Project Structure

```
├── langraph_web/
│   ├── bot_backend.py   # LangGraph workflow and state management
│   ├── frontend.py      # Streamlit UI 
├── .env.example         # Example environment variables
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Future Enhancements

- [ ] Human-in-the-Loop integration
- [ ] Persistent database storage (PostgreSQL/SQLite)
- [ ] Multi-agent workflows
- [ ] Custom tool integration
- [ ] Advanced conversation analytics

## License

MIT

## Author

Karan Gautam
