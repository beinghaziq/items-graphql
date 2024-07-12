from fastapi import FastAPI
from database import engine, Base
from graphql_schemas import graphql_app

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
