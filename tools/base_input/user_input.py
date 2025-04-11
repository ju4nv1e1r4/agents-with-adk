from pydantic import BaseModel

class UserInput(BaseModel):
    URL: str
    Problem: str
    Details: str

def user_input_function(user_input: dict) -> str:
    user_data = UserInput(**user_input)

    result = (
        f"URL: {user_data.URL}\n"
        f"Problema principal: {user_data.Problem}\n"
        f"Detalhes adicionais: {user_data.Details}"
    )

    return result
