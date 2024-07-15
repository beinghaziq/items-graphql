import strawberry

@strawberry.type
class ItemType:
    id: int
    name: str
    description: str
