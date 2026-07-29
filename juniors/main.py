from fastapi import FastAPI, Request # type: ignore

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

def current_state():
    return { "total": app.state.total, "sold": app.state.sold, "available": app.state.total - app.state.sold }

def er():
    return { "error": "error" }

app.state.total = 120
app.state.sold = 10

@app.get("/batch")
def view_batch():
    if (app.state.total - app.state.sold) >= 0:
        return current_state()
    return er()

@app.post("/batch/reset")
def reset_batch():
    app.state.total = 100
    app.state.sold = 0
    return current_state()

@app.post("/webhook/payment")
async def handle_payment(req: Request):
  payload = await req.json()
  status = payload.get("status")
  if (status != "FAILED" or status != "SOLD"):
      return er()
