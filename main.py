#
#  Import LIBRARIES
from typing import Annotated

import bcrypt
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
hash: bytes = bcrypt.hashpw(password=password.encode(encoding="utf-8"), salt=bcrypt.gensalt())
print(hash)


@app.get(path="/")
def secret_response(credentials: Annotated[HTTPBasicCredentials, Depends(dependency=security)]) -> dict[str, str]:
    passwords_match: bool = bcrypt.checkpw(password=credentials.password.encode(encoding="utf-8"), hashed_password=hash)

    if credentials.username == username and passwords_match:
        # if credentials.username == username and credentials.password == password:
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
