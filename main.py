from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    dni = Column(String, nullable=False)
    position = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
    db = SessionLocal()
    try:
        employees = db.query(Employee).order_by(Employee.id.desc()).all()
        return templates.TemplateResponse("index.html", {"request": request, "employees": employees})
    finally:
        db.close()

@app.post("/add")
def add_employee(first_name: str = Form(...), last_name: str = Form(...), dni: str = Form(...), position: str = Form(...)):
    db = SessionLocal()
    try:
        emp = Employee(first_name=first_name.strip(), last_name=last_name.strip(), dni=dni.strip(), position=position.strip())
        db.add(emp)
        db.commit()
    finally:
        db.close()
    return RedirectResponse(url="/", status_code=303)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)