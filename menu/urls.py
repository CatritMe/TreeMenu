from django.urls import path

from menu.apps import MenuConfig
from menu.views import index, draw_menu

app_name = MenuConfig.name

urlpatterns = [
    path('', index, name='main_menu'),
    path('<path:path>/', draw_menu, name='draw_menu'),
]
