from state import AdvisoryState
from langgraph.graph import START , StateGraph , END

def graph_state(AdvisoryState):
    """_summary_

    Args:
        AdvisoryState (_type_): _description_
    """    
    graph = StateGraph(AdvisoryState)