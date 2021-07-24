from django.urls import path
from .schema import schema
from graphene_django.views import GraphQLView

urlpatterns = [ 
    path('graphql', GraphQLView.as_view(schema=schema, graphiql=True))
]