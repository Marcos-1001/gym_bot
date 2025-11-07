from fastapi import FastAPI
from langchain.agents import create_agent
from dotenv import load_dotenv


load_dotenv()
app =  FastAPI()


def main(): 
    model = ChatOpenAI(
        model=os.getenv("ORCHESTATOR_MODEL"),
        temperature=0.1,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    system_prompt_path = os.path.join("prompts", "orchestator_prompt.txt")

    agent = create_agent(
        model, 
        tools=[],
        system_prompt=open(system_prompt_path).read()
        
    )
    return None



if __init__ == '__main__':
    print("Hello")