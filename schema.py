import graphene
import webapp.schema


class Query(webapp.schema.Query, graphene.ObjectType):
    pass


class Mutation(webapp.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
