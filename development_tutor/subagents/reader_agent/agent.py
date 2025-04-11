from google.adk.agents.llm_agent import Agent
from ...shared_libraries import constants
from . import prompt 
from google.adk.tools import google_search

reader = Agent(
    model=constants.BASE_MODEL,
    name="reader",
    description="Recebe e lê a documentação e entende como funciona o desenvolvimento",
    instruction=prompt.READ_DESTROY_CONQUER_DONE,
    tools=[google_search]
)