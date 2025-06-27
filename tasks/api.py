from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action 
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()             # Consulta todas las tareas
    permission_classes = [permissions.AllowAny]   # Permite acceso sin autenticación
    serializer_class = TaskSerializer         # Serializador para el modelo Task
 # Acción personalizada para marcar/desmarcar una tarea como hecha
    @action(detail=True, methods=['post'])
    def done(self, request, pk=None):
        task = self.get_object()     # Obtiene la tarea por su ID (pk)
        task.done = not task.done   # Guarda el cambio en la base de datos
        task.save()
        return Response(
            {
                'status': 'task done' if task.done else 'task undone' # Mensaje según el nuevo estado
            },
            status=status.HTTP_200_OK    # Código de respuesta HTTP 200 (OK)
            # en caso que no responda 
        ) 