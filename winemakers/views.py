from django.shortcuts import (
    render, redirect, get_object_or_404, reverse,)
from .models import Winemakers
from django.contrib import messages
from .forms import WinemakersForm

from django.contrib.auth.decorators import login_required


def view_winemakers(request):
    """ A view to render the winemakers page """
    winemakers = Winemakers.objects.all()

    context = {
        'winemakers': winemakers,
    }

    return render(request, 'winemakers/winemakers.html', context)


@login_required
def add_winemakers(request):
    """ Add a Producer to the site """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry only store owners are allowed to do that!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = WinemakersForm(request.POST, request.FILES)
        if form.is_valid():
            winemakers = form.save()
            messages.success(request, 'Producer Successfully added!')
            return redirect(reverse('winemaker_detail', args=[winemakers.id]))
        else:
            messages.error(request, 'Failed to add a Producer. \
                 Please ensure the form is valid.')
    else:
        form = WinemakersForm()
    template = 'winemakers/add_winemakers.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_winemaker(request, winemaker_id):
    """ Edit a Winemaker Info  """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry only store owners are allowed to do that!')
        return redirect(reverse('home'))

    wm = get_object_or_404(Winemakers, pk=winemaker_id)
    if request.method == 'POST':
        form = WinemakersForm(request.POST, request.FILES, instance=wm)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wine Producer successfully updated!')
            return redirect(reverse('winemaker_detail', args=[wm.id]))
        else:
            messages.error(request, 'Unable to update Producer Infos. \
                Please ensure that the form is valid.')
    else:
        form = WinemakersForm(instance=wm)
        messages.info(request, f'You are editing {wm.title}')

    template = 'winemakers/edit_winemaker.html'
    context = {
        'form': form,
        'wm': wm,
    }

    return render(request, template, context)


@login_required
def delete_winemaker(request, winemaker_id):
    """ Delete a Producer from the store """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry only store owners are allowed to do that!')
        return redirect(reverse('home'))

    wm = get_object_or_404(Winemakers, pk=winemaker_id)
    wm.delete()
    messages.success(request, 'Producer succesfully deleted!')
    return redirect(reverse('winemakers'))
