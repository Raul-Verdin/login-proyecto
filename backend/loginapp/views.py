from django.contrib.auth import authenticate
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
    
        user = authenticate(username=username, password=password)
        if user is not None:
            return JsonResponse({'status': 'ok'})
        else:
            return JsonResponse({'status': 'fail'}, status=401)
    
    # Si es GET, muestra una respuesta simple o de prueba
    return HttpResponse("Login endpoint (esperando POST)")

def home_view(request):
    return HttpResponse("¡Bienvenido a mi backend en AWS Elastic Beanstalk!")
