from google.adk.agents.llm_agent import Agent

from .shared import constants, prompts
from .subagents.agents import Agents

def root_agent(url, prompt):
    subagents = Agents(
        user_input= url,
        prompt=prompt
    )

    tutor_agent = Agent(
        model=constants.TUTOR_MODEL,
        name=constants.AGENT_NAME,
        description=constants.DESCRIPTION,
        instruction=prompts.ROOT_PROMPT,
        sub_agents=[
            subagents.bring_solution(),
            subagents.read_docs(),
        ]
    )

    return tutor_agent