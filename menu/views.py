from django.shortcuts import render

from menu.models import Menu


def index(request):
    return render(request, 'menu/index.html', {'menus': Menu.objects.all()})


def draw_menu(request, path):
    splitted_path = path.split('/')
    assert len(splitted_path) > 0, ('= Draw_menu function failed =')
    return render(
        request, 'menu/index.html', {'menu_name': splitted_path[0], 'menu_item': splitted_path[-1]})
