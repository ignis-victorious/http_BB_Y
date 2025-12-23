#
#  Import LIBRARIES
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

#  Import FILES
#
#  ______________________


app = FastAPI()

security = HTTPBasic()


#  Credentials
username: str = "Tony Soprano"
password: str = "mafia"


@app.get(path="/")
def secret_response(credentials: Annotated[HTTPBasicCredentials, Depends(dependency=security)]) -> dict[str, str]:
    if credentials.username == username and credentials.password == password:
        return {"secret": "this is highly secret.."}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Basic"},
    )


# @app.get(path="/")
# def main() -> dict[str, str]:
#     return {"message": "Hello World"}


#
#  Import LIBRARIES
#  Import FILES
#
#  ______________________
