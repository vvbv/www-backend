import json
import ast
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail


# Create your views here.

#{"to":"xxx@xxx.com", "subject":"Hi", "message":"Welcome to IEDB", "html":"false"}
@api_view(['POST', 'OPTIONS'])
def sendEmail(request, format=None):

    if request.method == 'OPTIONS':
        return Response({"to":"xxx@xxx.com", "subject":"Hi", "message":"Welcome to IEDB", "html":"false"})

    json_data = None
    para = None
    mensaje = None
    html = None
    de = 'iedb@mail.com'
    
    try:
        json_data = str(request.data)
        json_data = ast.literal_eval(json_data)
    except:
        return Response({"errorCode":"-1", "errorMessage": "JSON mal formateado"})
    
    try:
        para = json_data['to']
        asunto = json_data['subject']
        mensaje = json_data['message']
        html = json_data['html']
    except:
        return Response({"errorCode":"-1", "errorMessage": "JSON incompleto"})
    
    try:
        if(html == 'true'):
            send_mail(
                asunto,
                '--',
                de,
                [para],
                fail_silently=False,
                html_message=mensaje,
            )
        else:
            send_mail(
                asunto,
                mensaje,
                de,
                [para],
                fail_silently=False,
            )
    except:
        return Response({"errorCode":"-1", "errorMessage": "Error con el servidor de correos"})    
    

    return Response({"errorCode":"0", "errorMessage":"Mensaje Enviado"})