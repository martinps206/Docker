from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Hola": "Martin Paliza Sanchez"}

""" python -m uvicorn main:app --reload """
""" docker build -t simple_app . """
""" docker run -it -p 8000:8000 -v cd:/usr/src/app simple_app """
""" docker start -a  """