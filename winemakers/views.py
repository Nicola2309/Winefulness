from django.shortcuts import (
    render, redirect, get_object_or_404, reverse,)
from .models import Winemakers, Comments
from django.contrib import messages
from .forms import WinemakersForm, CommentForm

from django.contrib.auth.decorators import login_required


def view_winemakers(request):
    """ A view to render the winemakers page """
    winemakers = Winemakers.objects.all()

    context = {
        'winemakers': winemakers,
    }

    return render(request, 'winemakers/winemakers.html', context)


def winemaker_detail(request, winemaker_id):
    """ A view to render the winemaker detail page """
    winemakers = get_object_or_404(Winemakers, pk=winemaker_id)
    comments = Comments.objects.filter(winemakers=winemaker_id)
    comment_form = CommentForm(data=request.POST)

    context = {
        'winemakers': winemakers,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'winemakers/winemaker_detail.html', context)


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
    template = 'winemakers/add_winemaker.html'
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


@login_required
def add_comment(request, winemaker_id):
    """ A view to add a comment to Wine Producers """
    winemakers = get_object_or_404(Winemakers, pk=winemaker_id)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        comments = Comments.objects.filter(winemakers=winemaker_id)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.winemakers = winemakers
            new_comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect(reverse('winemaker_detail', args=[winemakers.id]))
        else:
            messages.error(
                request, 'Failed to add your comment. \
                    Please ensure that the form is valid.')
    else:
        comment_form = CommentForm()

    template = 'winemakers/winemaker_detail.html'

    context = {
        'winemakers': winemakers,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }

    return render(request, template, context)


@login_required
def edit_comment(request, winemaker_id, comment_id):
    """ A view to edit a comment """
    winemakers = get_object_or_404(Winemakers, pk=winemaker_id)
    comment = get_object_or_404(Comments, winemakers=winemakers, pk=comment_id)
    if request.user == comment.user:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST, instance=comment)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.user = request.user
                new_comment.winemakers = winemakers
                new_comment.save()
                messages.success(request, 'Your comment has been updated!')
                return redirect('winemaker_detail', winemaker_id)
            else:
                messages.error(request, 'Unable to update your comment. Please ensure that the \
                form is valid before submitting')

                return redirect('winemaker_detail', winemaker_id)
        else:
            comment_form = CommentForm(instance=comment)
            context = {
                'comment_form': comment_form,
            }
            return render(request, 'winemakers/edit_comment.html', context)
    else:
        return redirect('winemaker_detail', winemaker_id)


@login_required
def delete_comment(request, winemaker_id, comment_id):
    """ A view to delete a comment """
    winemakers = get_object_or_404(Winemakers, pk=winemaker_id)
    comment = get_object_or_404(Comments, winemakers=winemakers, pk=comment_id)

    if request.user == comment.user:
        comment.delete()
        messages.success(request, 'Your comment has been deleted!')

    return redirect('winemaker_detail', winemaker_id)
