from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
	return {"message": "Haha lol, World This should be visible now!"}


