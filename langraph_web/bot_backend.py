from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List, Annotated
from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv


load_dotenv()

# for a responsive chatbot
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)


class chatState(TypedDict):
    message: Annotated[list[BaseMessage], add_messages]


def chat_node(state: chatState):
    message = state['message']

    ans = model.invoke(message)

    return {'message': ans}


# checkpointer
checkpointer = InMemorySaver()

graph = StateGraph(chatState)

graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')

graph.add_edge('chat_node', END)


chatbot = graph.compile(checkpointer=checkpointer)

thread_id = 1
CONFIG = {'configurable': {'thread_id': thread_id}}

# for message_chunk, meta_data in chatbot.stream({'message': [HumanMessage(
#         content="How to make pasta")]}, config=CONFIG, stream_mode='messages'):
#     if message_chunk.content:
#         print(message_chunk.content, end=" ", flush=True)

res = chatbot.invoke(
            {'message': [HumanMessage(content='hi my name is karan')]},
            config=CONFIG,
            stream_mode='messages'
        )

# print(chatbot.get_state(config=CONFIG))
