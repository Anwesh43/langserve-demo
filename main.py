from langchain import OpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes 
import uvicorn 
from fastapi import FastAPI
from dotenv import load_dotenv

def initializeApp():
    app = FastAPI(name = "langserve server")
    model = ChatOpenAI()
    prompt = ChatPromptTemplate.from_template('tell me a joke {topic}')
    add_routes(app, prompt | model, path = "/joke")
    return app 
if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(initializeApp(), host='localhost', port = 8080)
