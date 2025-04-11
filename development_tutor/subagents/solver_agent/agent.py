from google.adk.agents.llm_agent import Agent
from ...shared_libraries import constants
from . import prompt

solver = Agent(
    model=constants.BASE_MODEL,
    name="solver",
    description="Recebe a documentação do reader e soluciona o problema do usuário",
    instruction=prompt.RESUME_USER_INPUT,
)