import strawberry
from typing import List
from app.cruds.item import get_items
from database import SessionLocal
from app.types.item_type import ItemType

@strawberry.type
class Query:
    items: List[ItemType] = strawberry.field(resolver=lambda: get_items(SessionLocal()))

