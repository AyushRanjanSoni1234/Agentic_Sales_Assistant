from config import llm
from langchain_core.messages import HumanMessage

def qualification_agent(state):
    prompt = f"""
You are a sales qualification agent.
Ask about:
- company type
- use case
- budget
- timeline

Conversation:
{state['messages']}
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"messages": response.content}


def requirement_agent(state):
    prompt = f"""
You are requirement analysis agent.
Extract project type and features.

Conversation:
{state['messages']}
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"messages": response.content}


def pricing_agent(state):
    prompt = f"""
You are pricing agent.
Suggest price between ₹40,000 and ₹1,20,000.
Adjust based on complexity.

Conversation:
{state['messages']}
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"messages": response.content}


def negotiation_agent(state):
    prompt = f"""
You are negotiation agent.
Rules:
- never go below ₹40,000
- offer max 15% discount
- justify value

Conversation:
{state['messages']}
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"messages": response.content}


def closing_agent(state):
    prompt = f"""
You are closing agent.
Collect:
- name
- email
- phone

Conversation:
{state['messages']}
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    return {"messages": response.content}