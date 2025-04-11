from google.adk.agents.llm_agent import Agent
from ..shared import constants, prompts
from ..tools.search_engine.web_search_tool import WebSearch
from ..tools.base_input.user_input import user_input_function


class Agents:
    def __init__(self, user_url: str, user_input: dict):
        self.user_input = user_input_function(user_input)
        self.web_search = WebSearch(user_url)

    def bring_solution(self):
        solver = Agent(
            model=constants.BASE_MODEL,
            name="solver",
            description="Recebe a documentação do reader e soluciona o problema do usuário",
            instruction=prompts.RESUME_USER_INPUT,
            tools=[
                self.user_input
            ]
        )

        return solver

    def read_docs(self):
        reader_agent = Agent(
            model=constants.BASE_MODEL,
            name="reader",
            description="Recebe e lê a documentação e entende como funciona o desenvolvimento",
            instruction=prompts.READ_DESTROY_CONQUER_DONE,
            tools=[
                self.web_search.web_search(),
            ]
        )

        return reader_agent