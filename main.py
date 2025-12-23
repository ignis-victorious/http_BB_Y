
# 
#  Import LIBRARIES
from fastapi import FastAPI
#  Import FILES
# 
#  ______________________





app = FastAPI()

@app.get("/")
def main():
    return {"message": "Hello World"}




# 
#  Import LIBRARIES
#  Import FILES
# 
#  ______________________

