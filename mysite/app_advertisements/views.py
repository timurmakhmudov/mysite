from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Advertisement
from .forms import AdvertisementsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()


def index(request):
    title = request.GET.get('query')
    if title:
        advertisements = Advertisement.objects.filter(title__icontains=title)
    else:
        advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements, 'title': title}
    return render(request, 'app_advertisements/index.html', context)


# Create your views here.
def top_sellers(request):
    users = User.objects.annotate(adv_count=Count('advertisement')).order_by('-adv_count')
    context = {'users': users}
    return render(request, 'app_advertisements/top-sellers.html', context)


@login_required(login_url=reverse_lazy('adv_post'))
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementsForm(request.POST, request.FILES)
        if form.is_valid():
            new_advertisement = form.save(commit=False)
            new_advertisement.user = request.user
            new_advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementsForm()
    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context)


def advertisement_detail(request, pk):
    advertisement = Advertisement.objects.get(id=pk)
    context = {'advertisement': advertisement}
    return render(request, 'app_advertisements/advertisement.html', context)




