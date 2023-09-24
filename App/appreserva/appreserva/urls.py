from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from .schema import schema
from ApiPrueba.schemaApi import schemaApi

urlpatterns = [
    path("admin/", admin.site.urls),
    path("store/", include("store.urls")),
    # path("catalogo/", include("catalogo.urls")),
    path("ApiPrueba/", include("ApiPrueba.urls")),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
    path("graphqlApi", GraphQLView.as_view(graphiql=True, schema=schemaApi)),
]
