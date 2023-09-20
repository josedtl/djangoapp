from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Alumno, Curso, Accion
from .serializers import AlumnoSerializer, CursoSerializer


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
