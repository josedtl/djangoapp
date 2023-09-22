from ..serializers import CargoSerializer
from ..models import Accion
from ..modelsItem.CargoModel import CargoModel
from rest_framework.response import Response
from rest_framework import status


class CargoBs:
    def Update(data: any):
        cargo_id = data.get("CargoId")
        cargo = CargoModel.objects.get(CargoId=cargo_id)
        cargo_serializer = CargoSerializer(cargo, data=data)
        if cargo_serializer.is_valid():
            cargo_serializer.save()
            return data

    def Save(data: any):
        cargo_serializer = CargoSerializer(data=data)
        if cargo_serializer.is_valid():
            cargo = cargo_serializer.save()
            data["CargoId"] = cargo.CargoId
            return data

    def Delete(data: any):
        curso_id = data.get("CargoId", None)
        if curso_id is not None:
            curso = CargoModel.objects.get(CargoId=curso_id)
            curso.delete()
            return True
