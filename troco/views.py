from pymongo import MongoClient
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse, HttpResponse
from utils.desafio_entrevista import troco_facil


@api_view(['POST'])
def troco(request):

    if request.method == 'POST':
        try:
            a = request.data["preco"]
            b = request.data["pgto"]
            c = troco_facil(a, b)

            return JsonResponse(c)
        except ValueError as e:
            return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def lista_detalhes(request):
    if request.method == 'GET':

        client = MongoClient('localhost', 27017)
        db = client.caixaDB
        array = list(db.troco_trococerto.find())
        for i in range(len(array)):
            array[i]['_id'] = i

        return JsonResponse(array, safe=False)


def troco_detalhe(request, pk):

    client = MongoClient('localhost', 27017)
    db = client.caixaDB

    if request.method == 'GET':

        array = list(db.troco_trococerto.find())
        for i in range(len(array)):
            array[i]['_id'] = i

        obj = array[pk]
        return JsonResponse(obj, safe=False)

    elif request.method == 'PUT':

        array = list(db.troco_trococerto.find())
        for i in range(len(array)):
            array[i]['_id'] = i

        obj = array[pk]
        return JsonResponse(obj, safe=False)

    elif request.method == 'DELETE':

        array = list(db.troco_trococerto.find())
        for i in range(len(array)):
            array[i]['_id'] = i

        array.remove(pk)
        return HttpResponse(status=204)