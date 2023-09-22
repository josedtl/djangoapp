from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Alumno, Curso, Accion
from .serializers import (
    AlumnoSerializer,
    CursoSerializer,
    CargoSerializer,
    TipoDocumentoIdentidadSerializer,
    EstadoCivilSerializer,
    GeneroSerializer,
    UbigeoSerializer,
    PersonaNaturalSerializer,
)
from .modelsItem.CargoModel import CargoModel
from .modelsItem.GeneralModel import TipoDocumentoIdentidad, EstadoCivil, Genero, Ubigeo
from .modelsItem.PersonaNaturalModel import PersonaNaturalModel


class GuardarAlumnoYCurso(APIView):
    def post(self, request, format=None):
        try:
            data = request.data

            # Validar la acción con el enumerado
            accion = data.get("Accion", None)
            if accion not in [item.value for item in Accion]:
                return Response(
                    {"error": "Acción no válida"}, status=status.HTTP_400_BAD_REQUEST
                )

            if accion == Accion.UPDATE.value:
                # Obtener el alumno a actualizar
                alumno_id = data.get("AlumnoId")
                try:
                    alumno = Alumno.objects.get(AlumnoId=alumno_id)
                except Alumno.DoesNotExist:
                    return Response(
                        {"error": "El alumno no existe"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                alumno_serializer = AlumnoSerializer(alumno, data=data)
                if alumno_serializer.is_valid():
                    alumno_serializer.save()
                else:
                    return Response(
                        alumno_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )

            elif accion == Accion.ADD.value:
                alumno_serializer = AlumnoSerializer(data=data)
                if alumno_serializer.is_valid():
                    alumno = alumno_serializer.save()
                    data["AlumnoId"] = alumno.AlumnoId
                else:
                    return Response(
                        alumno_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )

            else:
                return Response(
                    {"error": "Acción no válida"}, status=status.HTTP_400_BAD_REQUEST
                )

            cursos_data = data.get("detalles", [])
            for curso_data in cursos_data:
                curso_data["AlumnoId"] = alumno.AlumnoId

                # Validar la acción para el modelo Curso
                curso_accion = curso_data.get("Accion", None)
                if curso_accion is not None and curso_accion not in [
                    item.value for item in Accion
                ]:
                    return Response(
                        {"error": "Acción para Curso no válida"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                if curso_accion == Accion.UPDATE.value:
                    # Obtener el alumno a actualizar
                    curso_id = curso_data.get("CursoId", None)
                    try:
                        curso = Curso.objects.get(CursoId=curso_id)
                    except Alumno.DoesNotExist:
                        return Response(
                            {"error": "El alumno no existe"},
                            status=status.HTTP_400_BAD_REQUEST,
                        )

                    alumno_serializer = AlumnoSerializer(curso, data=curso_data)
                    if alumno_serializer.is_valid():
                        alumno_serializer.save()
                    else:
                        return Response(
                            alumno_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                        )

                if curso_accion == Accion.ADD.value:
                    curso_serializer = CursoSerializer(data=curso_data)
                    if curso_serializer.is_valid():
                        curso = curso_serializer.save()
                        curso_data["CursoId"] = curso.CursoId
                    else:
                        return Response(
                            curso_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                        )
                elif curso_accion == Accion.DELETE.value:
                    curso_id = curso_data.get("CursoId", None)
                    if curso_id is not None:
                        try:
                            curso = Curso.objects.get(CursoId=curso_id)
                            curso.delete()
                        except Curso.DoesNotExist:
                            pass

            data["detalles"] = cursos_data
            if accion == Accion.UPDATE.value:
                return Response(
                    {"message": "Alumno y cursos actualizados correctamente"},
                    status=status.HTTP_200_OK,
                )
            elif accion == Accion.DELETE.value:
                return Response(
                    {"message": "Alumno y cursos eliminados correctamente"},
                    status=status.HTTP_204_NO_CONTENT,
                )
            else:
                return Response(
                    {"message": "Alumno y cursos creados correctamente", "data": data},
                    status=status.HTTP_201_CREATED,
                )

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CargoListCreateView(generics.ListCreateAPIView):
    queryset = CargoModel.objects.all()
    serializer_class = CargoSerializer


class CargoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CargoModel.objects.all()
    serializer_class = CargoSerializer


from .Metodos.CargoBs import CargoBs


class CargoSave(APIView):
    def post(self, request, format=None):
        try:
            data = request.data
            accion = data.get("Action", None)

            if accion == Accion.UPDATE.value:
                respuesta = CargoBs.Update(data)
                return Response(respuesta)
            elif accion == Accion.ADD.value:
                respuesta = CargoBs.Save(data)
                return Response(respuesta)
            elif accion == Accion.DELETE.value:
                respuesta = CargoBs.Delete(data)
                return Response(respuesta)

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TipoDocumentoIdentidadViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumentoIdentidad.objects.all()
    serializer_class = TipoDocumentoIdentidadSerializer


class EstadoCivilViewSet(viewsets.ModelViewSet):
    queryset = EstadoCivil.objects.all()
    serializer_class = EstadoCivilSerializer


class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class UbigeoViewSet(viewsets.ModelViewSet):
    queryset = Ubigeo.objects.all()
    serializer_class = UbigeoSerializer


class PersonaNaturalViewSet(viewsets.ModelViewSet):
    queryset = PersonaNaturalModel.objects.all()
    serializer_class = PersonaNaturalSerializer


from .models import Persona, TipoDocumento
from .serializers import PersonaSerializer, PersonaNaturalMainSerializer


class PersonaListView(generics.ListAPIView):
    queryset = Persona.objects.select_related("TipodocumentoId")
    serializer_class = PersonaSerializer


class PersonaNaturalMainListView(generics.ListAPIView):
    queryset = PersonaNaturalModel.objects.select_related("TipoDocumentoIdentidad")
    serializer_class = PersonaNaturalMainSerializer
