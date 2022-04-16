from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from json import loads,dumps
from django.http import Http404
import datetime
import collections
import sqlite3

# Create your views here.


@csrf_exempt
def alta(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)

    username = body['username']
    comment = body['comment']

    mydb = sqlite3.connect("tarea_U_DJ.db")
    cur = mydb.cursor()

    stringSQL = '''INSERT INTO Usuario (username, comment)
VALUES (?, ?)'''

    rows = cur.execute(stringSQL, (username, comment,))
    mydb.commit()

    if rows is None:
        raise Http404("It was not possible to register that user")
    else:
        d = {"msg": "User added with success!"}
        j = dumps(d)

    mydb.close()
    return HttpResponse(j, content_type="text/json-comment-filtered")


def consulta(request):
    mydb = sqlite3.connect("tarea_U_DJ.db")
    cur = mydb.cursor()
    stringSQL = '''SELECT id as user_id, username, comment FROM Usuario'''
    rows = cur.execute(stringSQL)
    if rows is None:
        raise Http404("List unavailable")
    else:
        lista_salida = []
        for r in rows:
            print(r)
            d = {}
            d["user_id"] = r[0]
            d["username"] = r[1]
            d["comment"] = r[2]
            lista_salida.append(d)
        j = dumps(lista_salida)
    return HttpResponse(j, content_type="text/json-comment-filtered")


@csrf_exempt
def consulta_usuario(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)

    user_id = body['id']

    mydb = sqlite3.connect("tarea_U_DJ.db")
    cur = mydb.cursor()
    stringSQL = '''SELECT id as user_id, username, comment FROM Usuario WHERE user_id = ?'''
    rows = cur.execute(stringSQL, (user_id,))
    if rows is None:
        raise Http404("List unavailable")
    else:
        lista_salida = []
        for r in rows:
            print(r)
            d = {}
            d["user_id"] = r[0]
            d["username"] = r[1]
            d["comment"] = r[2]
            lista_salida.append(d)
        j = dumps(lista_salida)
    return HttpResponse(j, content_type="text/json-comment-filtered")


@csrf_exempt
def cambio(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)

    user_id = body['id']
    username = body['username']

    mydb = sqlite3.connect("tarea_U_DJ.db")
    cur = mydb.cursor()

    stringSQL = '''UPDATE Usuario SET username = ?
    WHERE Usuario.id = ?'''

    rows = cur.execute(stringSQL, (username, user_id))
    mydb.commit()

    if rows is None:
        raise Http404("It was not possible to update that user")
    else:
        d = {"msg": "Data updated with success!"}
        j = dumps(d)

    mydb.close()
    return HttpResponse(j, content_type="text/json-comment-filtered")
