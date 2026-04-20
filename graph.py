from langgraph.graph import StateGraph, END
from typing import TypedDict
from agent import *

class AgentState(TypedDict):
    messages: str

workflow = StateGraph(AgentState)

workflow.add_node("qualification", qualification_agent)
workflow.add_node("requirement", requirement_agent)
workflow.add_node("pricing", pricing_agent)
workflow.add_node("negotiation", negotiation_agent)
workflow.add_node("closing", closing_agent)

workflow.set_entry_point("qualification")

workflow.add_edge("qualification", "requirement")
workflow.add_edge("requirement", "pricing")
workflow.add_edge("pricing", "negotiation")
workflow.add_edge("negotiation", "closing")
workflow.add_edge("closing", END)

app = workflow.compile()


