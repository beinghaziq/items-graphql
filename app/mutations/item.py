import strawberry
from sqlalchemy.orm import Session
from app.cruds.item import create_item, update_item, delete_item
from database import SessionLocal
from app.types.item_type import ItemType

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
