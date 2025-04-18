import os
from dotenv import load_dotenv

load_dotenv()

AGENT_NAME = "development_tutor"
DESCRIPTION = "Um agente instrutor/tutor para desenvolvedores."
PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT", "EMPTY")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "global")
TUTOR_MODEL = os.getenv("TUTOR_MODEL", "learnlm-1.5-pro-experimental")
BASE_MODEL = os.getenv("BASE_MODEL", "gemini-2.0-flash-thinking-exp-01-21")