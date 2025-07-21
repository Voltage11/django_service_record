from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, resolve_url
from django.views.decorators.http import require_POST

from app.core.forms.service import ServiceForm
from app.core.models import Service



def service_list(request):
    if request.method == 'GET':
        current_user = request.user
        q = request.GET.get('q', None)
        is_active = request.GET.get('is_active', None)
        records = (Service.objects.only('name', 'comment', 'price', 'is_active', 'id').\
                   filter(user=current_user).order_by('name').all())
        if q:
            records = records.filter(name__icontains=q)
        if is_active:
            if is_active == '1':
                records = records.filter(is_active=True)
            else:
                records = records.filter(is_active=False)
        context = {
            'records': records
        }

        return render(request, 'core/service/list.html', context=context)


def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            try:
                service = form.save(commit=False)
                service.user = request.user
                service.save()
                messages.success(request, 'Услуга успешно создана!')
                return redirect(resolve_url('core:service_list'))
            except Exception as e:
                messages.error(request, f'Ошибка при создании услуги: {str(e)}')
    else:
        form = ServiceForm()

    context = {
        'title': 'Создание услуги',
        'form': form
    }
    return render(request, 'core/service/create.html', context=context)


def service_update(request, pk: int):
    if request.method == 'GET':
        return render(request, 'core/service/update.html')


@require_POST
@login_required
def service_delete(request, pk: int) -> JsonResponse:
    service = Service.objects.filter(pk=pk, user=request.user).first()

    if not service:
        return JsonResponse({
            'status': 'error',
            'message': 'Услуга не найдена или у вас нет прав на её удаление',
        }, status=404)

    try:
        service.delete()
        return JsonResponse({
            'status': 'success',
            'message': 'Услуга успешно удалена',
        }, status=200)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': 'Произошла ошибка при удалении услуги',
        }, status=500)