from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from chat import LLAMACodeGenerator

app = FastAPI()
app.mount("/static", StaticFiles(directory="./web"), name="web")
templates = Jinja2Templates(directory="./")
model = None

@app.on_event("startup")
async def load_model():
    global model
    model = LLAMACodeGenerator()

@app.post("/generate_code")
async def generate(request: Request):
    request_data = await request.json()
    code = model.generate_code(request_data.get('description'))
    return {"code": code}

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("./web/index.html", {"request": request})

@app.post("/submit_feedback")
async def generate(request: Request):
    request_data = await request.json()
    # TODO Save feedback 
    request_data.get('feedback')
    return 0