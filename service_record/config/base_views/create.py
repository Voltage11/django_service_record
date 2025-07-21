from django.http import HttpRequest, HttpResponse
from django.forms import ModelForm, Form
from django.shortcuts import redirect, resolve_url, render
from django.urls import reverse_lazy
from typing import Union, Any, Optional, Dict


class BaseCreate:
    def __init__(
            self,
            request: HttpRequest,
            title: str,
            form: Union[ModelForm, Form],
            # href_save: Union[str, reverse_lazy],
            href_list: Union[str, reverse_lazy],
            extra_context: Optional[Dict[str, Any]] = None
    ):
        self.request = request
        self.title = title
        self.form = form
        self.href_list = href_list
        self.template = 'base/create.html'
        self.extra_context = extra_context or {}


def base_create(request: HttpRequest, props: BaseCreate) -> HttpResponse:
    form = props.form
    if request.method == 'POST':
        form = props.form(request.POST, request.FILES)  # Добавлена обработка файлов
        if form.is_valid():
            try:
                form.save()
                return redirect(resolve_url(props.href_list))
            except Exception as e:
                print(f"Error saving form: {e}")
                # Добавляем ошибку в форму
                form.add_error(None, f"An error occurred: {e}")

    context = {
        'form': form,
        'title': props.title,
        'href_list': props.href_list,
        'errors': form.errors if form.errors else None,
        **props.extra_context  # Добавляем дополнительный контекст
    }

    return render(request, props.template, context=context)