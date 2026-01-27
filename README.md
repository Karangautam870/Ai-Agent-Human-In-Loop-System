# AI Agent Human-In-Loop System

A conversational AI chatbot built with LangGraph, featuring persistent memory and multi-session management. Powered by Google's Gemini API with a Streamlit frontend.

## Features

- 🧠 **Persistent Memory**: Conversations are stored and can be resumed across sessions
- 💬 **Multi-Thread Support**: Manage multiple conversation threads
- 🔄 **State Management**: Built with LangGraph for robust workflow orchestration
- ⚡ **Real-time Streaming**: Stream responses from the AI model
- 🎯 **Human-in-the-Loop Ready**: Architecture designed for future HITL integration

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
│   └── notes.txt        # Development notes
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
