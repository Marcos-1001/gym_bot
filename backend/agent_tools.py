from langchain.tools import tool
from langchain.agents import create_agent
from config import Config

@tool
def search_in_exercise_db(query: str) -> str: 
    
    model = ChatOpenAI(
        model=Config.EXTRACTOR_MODEL,
        temperature=0.1,
        api_key=Config.OPENAI_API_KEY
    )
    system_prompt_path = os.path.join("prompts", "extractor_prompt.txt")
    
    
    coding_agent = create_agent(
        model, 
        system_prompt=system_prompt_path
    )




def extract_text_content_from_ph_eval(archive):



