from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Employee(BaseModel):
    name: str
    position: str
    email: str
    phone: str
    department: str
    hire_date: str
    active: bool


# In-memory storage for demonstration purposes
employees = []


@app.get("/")
def read_root():
    return {"message": "Welcome to JMBDE API"}


@app.post("/employees", status_code=201)
def add_employee(employee: Employee):
    employees.append(employee)
    return employee


@app.get("/employees", response_model=List[Employee])
def list_employees():
    return employees


@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int):
    if 0 <= employee_id < len(employees):
        return employees[employee_id]
    raise HTTPException(status_code=404, detail="Employee not found")


def start_api_server():
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
