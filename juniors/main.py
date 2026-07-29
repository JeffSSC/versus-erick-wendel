from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

def current_state():
    return { "total": total, "sold": sold, "available": total - sold }

def er():
    return { "error": "error" }

total = 100
sold = 0

@app.get("/batch")
def view_batch():
    if (total - sold) >= 0:
        return current_state()
    return er()

@app.post("/batch/reset")
def reset_batch():
    total = 100
    sold = 0
    return current_state()

@app.post("/webhook/payment")
async def handle_payment(req: Request):
  payload = await req.json()
  status = payload.get("status")
  if (status != "FAILED" or status != "SOLD"):
      return er()
