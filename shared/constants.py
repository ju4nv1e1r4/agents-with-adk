import os
from dotenv import load_dotenv

load_dotenv()

AGENT_NAME = "development_tutor"
DESCRIPTION = "Um agente instrutor/tutor para desenvolvedores."
MODEL = os.getenv("MODEL", "learnlm-1.5-pro-experimental")
WHL_FILE_NAME = os.getenv("ADK_WHL_FILE", "")