# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task

@csrf_exempt  # Solo si no usas CSRF token
def delete_task(request, task_id):
    if request.method != 'DELETE':
        return JsonResponse(
            {'error': 'Método no permitido'}, 
            status=405,
            json_dumps_params={'ensure_ascii': False}
        )
    
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return JsonResponse(
            {'message': 'Tarea eliminada correctamente'},
            status=200
        )
    except Task.DoesNotExist:
        return JsonResponse(
            {'error': 'Tarea no encontrada'},
            status=404
        )
    except Exception as e:
        return JsonResponse(
            {'error': str(e)},
            status=500
        )