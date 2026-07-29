from fastapi import FastAPI

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
def handle_payment(req):
  return req
  if (status != "FAILED" or status != "SOLD"):
      return er()

# 1. Define your data structure
class Item():
    reservation_id: str
    status: str

# 2. Pass the model as a parameter in your route
@app.post("/webhook/payment")
async def handle_payment():
    # Access properties directly using dot notation
    req_dict = req.model_dump()
    if (req_dict.status != "FAILED" or req_dict.status != "SOLD"):
        return er()
