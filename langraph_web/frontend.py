from langchain_core.messages import BaseMessage, HumanMessage
from bot_backend import chatbot
import streamlit as st
import uuid

# utility functions

def generate_thread_id():
    # generate a new thread id
    return uuid.uuid4()

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_threads(st.session_state['thread_id'])
    st.session_state['message_history'] = []

def add_threads(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    return state.values.get('message', [])

 # Session Setup

defaults = {
    'message_history': [],
    'thread_id': generate_thread_id(),
    'chat_threads': [],
    'thread_titles': {}
}

for key, default in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = default

CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}


#  Sidebar UI

st.sidebar.title('LangGraph Chatbot')

if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('My Conversations')

for thread_id in st.session_state['chat_threads'][::-1]:  # newest first
    title = st.session_state['thread_titles'].get(thread_id, str(thread_id))
    if st.sidebar.button(title):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)
        temp_message = []
        for msg in messages:
            role = 'user' if isinstance(msg, HumanMessage) else 'assistant'
            temp_message.append({'role': role, 'content': msg.content})
            
        st.session_state['message_history'] = temp_message

 # Main UI 

# chat history
for msg in st.session_state['message_history']:
    with st.chat_message(msg['role']):
        st.text(msg['content'])

user_input = st.chat_input('Ask Anything')

if user_input:
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    
    if st.session_state['thread_id'] not in st.session_state['thread_titles']:
        title = user_input.strip()
        if len(title) > 50:
            title = title[:47] + "...."
        st.session_state['thread_titles'][st.session_state['thread_id']] = title  # fixed name

    with st.chat_message('user'):
        st.text(user_input)

    def stream_and_print():
        ai_response = ""
        for message_chunk, meta_data in chatbot.stream(
            {'message': [HumanMessage(content=user_input)]},
            config=CONFIG,
            stream_mode='messages'
        ):
            if message_chunk.content:
                ai_response += message_chunk.content
                yield message_chunk.content

        st.session_state['message_history'].append({'role': 'assistant', 'content': ai_response})

    with st.chat_message('assistant'):
        st.write_stream(stream_and_print())
