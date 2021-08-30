import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/widget.js")
def widgetjs():
    return FileResponse("tools/widget.js")

@app.get("/api/{id}/{feedback}")
def getfeedback(id: str, feedback: str):
    print(f"ID: {id}")
    if feedback == "1":
        print("-- Positive! :)")
    elif feedback == "2":
        print("-- Neutral!  :|")
    elif feedback == "3":
        print("-- Negative! :(")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=80)