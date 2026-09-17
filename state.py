from typing import TypedDict, Optional , Annotated
from langgraph.graph import MessagesState , add_messages
from langchain_core.messages import (HumanMessage, AIMessage , SystemMessage , BaseMessage)

class AdvisoryState(BaseMessage):
    messages : Annotated[list[BaseMessage], add_messages]
    product_id: Optional[str]
    mobile_number: Optional[str]
    email: Optional[str]
    customer_name: Optional[str]
    lead_status: Optional[str]
