from rest_framework.routers import DefaultRouter
from .api import TaskViewSet
# Crea un router para las vistas de la API
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks') # Registra el ViewSet de tareas bajo la ruta /tasks/
# Las URLs generadas por el router se asignan a urlpatterns
urlpatterns = router.urls

