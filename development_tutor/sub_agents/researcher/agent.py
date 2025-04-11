from google.adk.agents import Agent
from . import prompt
from ...shared_libraries import constants
from ...tools.search import google_search_grounding

researcher = Agent(
    model=constants.BASE_MODEL,
    name="researcher",
    description="Pesquisa na web sobre um assunto.",
    instruction=prompt.RESEARCHER_PROMPT,
    tools=[google_search_grounding]
)
