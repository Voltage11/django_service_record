from django.urls import reverse


class SubMenuItem:
    def __init__(self, title: str, url: str):
        self.title = title
        self.url = url

class MenuItem:
    def __init__(self, title: str, url: str, sub_items: list[SubMenuItem]):
        self.title = title
        self.url = url
        self.sub_items = sub_items

def get_menu_items(request):
    if request.user.is_authenticated:
        menu_items = [
            MenuItem("Записи", reverse('core:service_list'), [
                SubMenuItem("Создать", reverse('core:service_create')),
                SubMenuItem("Список", reverse('core:service_list')),
            ]),
            MenuItem("Клиенты", "/about/", []),
            MenuItem("Услуги", "/contact/", []),
        ]

        return {
            'menu_items': menu_items,
        }
    return {}
