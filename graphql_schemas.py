import strawberry
from typing import List
from strawberry.fastapi import GraphQLRouter
from sqlalchemy.orm import Session
from crud import get_items, create_item, update_item, delete_item
from database import SessionLocal

@strawberry.type
class ItemType:
    id: int
    name: str
    description: str

@strawberry.type
class Query:
    items: List[ItemType] = strawberry.field(resolver=lambda: get_items(SessionLocal()))

@strawberry.input
class ItemInput:
    name: str
    description: str

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_item(self, input: ItemInput) -> ItemType:
        db: Session = SessionLocal()
        return create_item(db, input.name, input.description)
    
    @strawberry.mutation
    def update_item(self, id: int, input: ItemInput) -> ItemType:
        db: Session = SessionLocal()
        return update_item(db, id, input.name, input.description)

    @strawberry.mutation
    def delete_item(self, id: int) -> ItemType:
        db: Session = SessionLocal()
        return delete_item(db, id)

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
