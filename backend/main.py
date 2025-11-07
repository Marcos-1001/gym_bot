from fastapi import FastAPI
from langchain.agents import create_agent
from dotenv import load_dotenv
from config import Config

load_dotenv()
app =  FastAPI()

@app.post("/archive")
def save_archive_content(archive_content):
    return None


@app.post("/chat")
def main(): 
    model = ChatOpenAI(
        model=Config.ORCHESTATOR_MODEL,
        temperature=0.1,
        api_key=Config.OPENAI_API_KEY
    )
    system_prompt_path = os.path.join("prompts", "orchestator.txt")

    agent = create_agent(
        model, 
        tools=[],
        system_prompt=open(system_prompt_path).read()
        
    )
    return None



if __init__ == '__main__':
    print("Hello")