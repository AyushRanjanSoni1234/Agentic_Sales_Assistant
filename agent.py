from config import llm
from langchain_core.messages import HumanMessage

def qualification_agent(state):
    prompt = f"""
You are ONLY a sales qualification agent.

STRICT RULES:
- Only ask qualification questions
- Do NOT discuss pricing
- Do NOT discuss discounts
- Do NOT finalize deal
- Ask 1-2 questions only

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

# ## Add Conditional Routing

# def router(state):
#     msg = str(state["messages"]).lower()

#     if "budget" not in msg:
#         return "qualification"

#     if "chatbot" in msg or "ai" in msg:
#         return "requirement"

#     if "price" in msg or "cost" in msg:
#         return "pricing"

#     if "discount" in msg or "reduce" in msg:
#         return "negotiation"

#     if "proceed" in msg or "okay" in msg:
#         return "closing"

#     return "qualification"    