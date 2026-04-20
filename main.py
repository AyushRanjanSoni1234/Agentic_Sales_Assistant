import streamlit as st
import requests

st.title("AI Sales Agent 🤖")

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.chat_input("Ask your query")

if user_input:
    st.session_state.chat.append(("user", user_input))

    response = requests.post(
        "https://agentic-sales-assistant.onrender.com/chat",
        json={"message": user_input}
    )

    reply = response.json()["response"]
    st.session_state.chat.append(("agent", reply))

for role, msg in st.session_state.chat:
    if role == "user":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)