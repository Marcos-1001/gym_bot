from langchain.tools import tool
from langchain.agents import create_agent


@tool
def search_in_exercise_db(query: str) -> str: 
    model = ChatOpenAI(
        model=os.getenv("WORKOUT_EXTRACTOR_MODEL"),
        temperature=0.1,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    system_prompt_path = os.path.join("prompts", "extractor_prompt.txt")
    coding_agent = create_agent(
        model, 
        system_prompt=system_prompt_path
    )


