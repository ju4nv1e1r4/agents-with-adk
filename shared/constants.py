import os
from dotenv import load_dotenv

load_dotenv()

AGENT_NAME = "development_tutor"
DESCRIPTION = "Um agente instrutor/tutor para desenvolvedores."
TUTOR_MODEL = os.getenv("TUTOR_MODEL", "learnlm-1.5-pro-experimental")
BASE_MODEL = os.getenv("BASE_MODEL", "gemini-2.0-flash-thinking-exp-01-21")
WHL_FILE_NAME = os.getenv("ADK_WHL_FILE", "")