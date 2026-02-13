# AI Agent Chatbot (LangGraph + Streamlit)

## Overview
This folder contains a conversational AI chatbot built with LangGraph and Streamlit. It wires a LangGraph state machine to a Gemini model, supports multi-threaded conversations, and streams responses in real time.

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
- LangGraph
- LangChain (Google Generative AI)
- Streamlit
- Google Gemini (gemini-2.5-flash)
- Python 3.13

## Setup
1. Create and activate a virtual environment.
2. Install dependencies:
   - `pip install langchain langchain-google-genai langgraph streamlit python-dotenv`
3. Create a `.env` file and add your API key:
   - `GOOGLE_API_KEY=your-google-api-key-here`

## Running Locally
- From this folder:
  - `streamlit run frontend.py`

## Future Enhancements
- Persistent storage for conversation history (database or file-based checkpointing).
- Human-in-the-loop integration.
- Authentication and per-user chat isolation.
- System prompt configuration and model selection in the UI.
- Conversation rename/delete actions in the sidebar.
- Robust error handling for API failures and streaming interruptions.
- Telemetry: basic analytics on message counts and response latency.
- UI polishing: theming, message timestamps, and typing indicators.
- Deployment: containerized setup (Docker) and cloud hosting.
