import graphene
from graphene_django import DjangoObjectType
from .modelsItem.PersonaNaturalModel import PersonaNaturalModel


class PersonaNaturalType(DjangoObjectType):
    class Meta:
        model = PersonaNaturalModel
        fields = (
            "PersonaNaturalId",
            "NumDocumento",
            "Nombres",
            "ApellidoPaterno",
            "ApellidoMaterno",
            "FechaNacimiento",
            "Direccion",
        )


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hello!")
    Personas = graphene.List(PersonaNaturalType)
    Persona = graphene.Field(PersonaNaturalType, id=graphene.ID())
    Personas = graphene.List(PersonaNaturalType)
    PersonasPorNombre = graphene.List(PersonaNaturalType, NumDocumento=graphene.String())
    def resolve_Personas(self, info):
        return PersonaNaturalModel.objects.all()

    def resolve_Persona(self, info, id):
        return PersonaNaturalModel.objects.get(pk=id)

    def resolve_PersonasPorNombre(self, info, NumDocumento):
        return PersonaNaturalModel.objects.filter(NumDocumento__icontains=NumDocumento)

schemaApi = graphene.Schema(query=Query)
