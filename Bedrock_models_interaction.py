from langchain_aws import ChatBedrockConverse
from langchain.chat_models import BaseChatModel, init_chat_model
from dotenv import load_dotenv
import os

def get_model(model:str, **args:dict)->BaseChatModel:
    return init_chat_model(
        model=model, 
        **args
        )

def get_model_from_gcp()->ChatBedrockConverse:
    return ChatBedrockConverse(
        model=os.getenv('MODEL_NAME',"amazon.nova-lite-v1:0"), 
        project= os.getenv('AWS_REGION'),
        )

if __name__ == "__main__":
    load_dotenv()
    llm = ChatBedrockConverse(
    model=os.getenv("MODEL_NAME"),
    region_name=os.getenv("AWS_REGION")
    )
    
    response = llm.invoke("What is captial  of Delhi?")
    response.pretty_print()