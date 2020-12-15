from typing import List

from fastapi import FastAPI

import databases
import sqlalchemy
from fastapi import FastAPI, status, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}'.format("user", "admin@123", "localhost", "5432", "postgres")

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

employees = sqlalchemy.Table(
    "employees",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("empid", sqlalchemy.String),
    sqlalchemy.Column("empname", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String),
    sqlalchemy.Column("phoneno", sqlalchemy.String),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, pool_size=3, max_overflow=0
)
metadata.create_all(engine)


# output Employee data
class Employee(BaseModel):
    id: int
    empid: str
    empname: str
    email: str
    phoneno: str


# input Employee data
class EmployeeIn(BaseModel):
    empid: str
    empname: str
    email: str
    phoneno: str


app = FastAPI(title="REST API using FastAPI PostgreSQL Async EndPoints")

# like cross origin in spring boot, for giving access to specific urls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# for connecting and disconnecting database while using database
@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# Insert Single Employee details
@app.post("/employees/", response_model=Employee, status_code=status.HTTP_201_CREATED)
async def create_emp(emp: EmployeeIn):
    query = employees.insert().values(empid=emp.empid, empname=emp.empname, email=emp.email, phoneno=emp.phoneno)
    last_record_id = await database.execute(query)
    return {**emp.dict(), "id": last_record_id}


# Display all Employees details
@app.get("/employees/", response_model=List[Employee], status_code=status.HTTP_200_OK)
async def display_allemps(skip: int = 0, take: int = 20):
    query = employees.select().offset(skip).limit(take)
    return await database.fetch_all(query)


# Display Employee details by id
@app.get("/employees/{emp_id}/", response_model=Employee, status_code=status.HTTP_200_OK)
async def dis_emp(emp_id: int):
    query = employees.select().where(employees.c.id == emp_id)
    return await database.fetch_one(query)