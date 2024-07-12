import strawberry

@strawberry.type
class UserType:
    id: int
    firstName: str
    lastName: str
    age: int
    gender: str
    email: str
    phone: str
    username: str
    password: str

@strawberry.type
class DeleteUserResponse:
    success: bool
    message: str
