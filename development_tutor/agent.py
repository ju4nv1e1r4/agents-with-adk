from google.adk.agents.llm_agent import Agent

from .shared_libraries import constants
from .subagents.reader_agent.agent import reader
from .subagents.solver_agent.agent import solver
from . import prompt

root_agent = Agent(
    model=constants.TUTOR_MODEL,
    name=constants.AGENT_NAME,
    description=constants.DESCRIPTION,
    instruction=prompt.ROOT_PROMPT,
    sub_agents=[
        reader,
        solver,
    ]
)