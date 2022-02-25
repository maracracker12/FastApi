from fastapi import FastAPI
import uvicorn

app = FastAPI()

qamar = [{"Name":"Qamar","Age":19,"Location":"Kirkuk"}]

@app.get("/")
def index():
    return {"Status":"ok"}


@app.get("/dataa")
def da_ta():
    return {"Data":qamar}

if __name__=="__main__":
    uvicorn.run("api:app",host="127.0.0.1",reload=True)

