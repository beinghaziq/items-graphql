import strawberry
from strawberry.fastapi import GraphQLRouter
from app.mutations.item import Mutation
from app.queries.item import Query

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)