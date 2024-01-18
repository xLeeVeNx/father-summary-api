from fastapi import FastAPI
from app.api.endpoints import projects, main
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

app.include_router(main.router)
app.include_router(projects.router)