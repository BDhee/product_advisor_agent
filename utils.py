
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain.chat_models import BaseChatModel, init_chat_model
from dotenv import load_dotenv
import os

def get_model(model:str, **args:dict)->BaseChatModel:
    return init_chat_model(
        model=model, 
        **args
        )

def get_model_from_gcp()->ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model=os.getenv('MODEL_NAME',"gemini-3.5-flash-lite"), 
        project= os.getenv('PROJECT_ID'),
        
        
        )

if __name__ == "__main__":
    load_dotenv()
    llm = get_model(
    model=os.getenv('MODEL_NAME',"gemini-3.5-flash"), 
    project= os.getenv('PROJECT_ID'), 
    model_provider= "google_genai" ,
    vertexai=True  
    )
    response = llm.invoke("What is captial  of Delhi?")
    response.pretty_print()