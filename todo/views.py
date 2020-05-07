from django.shortcuts import render, redirect
from .models import Activity, Profile
from .forms import AddForm, EditForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.save()
            profile.save()
            profile.activities.add(activity)
            return redirect('home')
             
    activities = profile.activities.all()
    context = {
        'activities': activities,
        'form': AddForm()
    }
    return render(request, 'todo/home.html', context)

@login_required
def delete(request, id):
    item = Activity.objects.get(id=id)
    user = Profile.objects.get(user=request.user)
    user.activities.remove(item)
    user.save()
    item.delete()
    context = {
        'activities': user.activities.all(),
        'form': AddForm()
    }
    return render(request, 'todo/home.html', context)

@login_required
def toggle(request, id):
    item = Activity.objects.get(id=id)
    item.crossed= False if item.crossed else True
    item.save()
    context = {
        'activities': Profile.objects.get(user=request.user).activities.all(),
        'form': AddForm()
    }
    return render(request, 'todo/home.html', context)

@login_required
def edit(request, id):
    item = Activity.objects.get(id=id)
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            updated_title = form.cleaned_data.get('title')
            user = Profile.objects.get(user=request.user)
            item = user.activities.get(id=id)
            item.title = updated_title
            item.save()
            return redirect('home')

    form = EditForm(instance=item)
    return render(request, 'todo/edit.html', {'form': form, 'item': item})