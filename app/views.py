from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import URL
from hashlib import md5
from django.http import HttpResponseRedirect


def main(request):
    urls = URL.objects.all()
    return render(request, 'main.html', {'urls': urls})


def create(request):
    if request.method == "POST":
        url = URL()
        url.full_url = str(request.POST.get("full_url"))
        url.url_hash = str(md5(url.full_url.encode()).hexdigest()[:5])
        url.save()
    return HttpResponseRedirect("/")


def redirect_clicks(request, url_hash):
    url = get_object_or_404(URL, url_hash=url_hash)
    url.clicked()
    return redirect(url.full_url)


def delete(request):
    all_url = URL.objects.all()
    all_url.delete()
    return HttpResponseRedirect("/")
