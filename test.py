from config import llm
from langchain_core.messages import HumanMessage

print(llm.invoke([HumanMessage(content="hello")]))