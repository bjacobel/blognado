from django.shortcuts import render
from blognado.apps.core import models
from django.http import HttpResponseNotFound

def BlogListView(request):
    ctx = {
        "liveblogs": models.Liveblog.objects.all()
    }

    return render(request, 'pages/index.html', ctx)

def BlogDetailView(request, id=None, slug=None):

    blog = None

    if id:
        blog = models.Liveblog.objects.get(id=id)
    elif slug:
        blog = models.Liveblog.objects.get(slug=slug)
    else:
        raise Exception("neither ID nor slug passed to BlogDetailView")

    if blog:
        ctx = {
            "blog": blog,
            "updates": models.Update.objects.filter(blog__exact=blog.pk)
        }

        return render(request, 'pages/detail.html', ctx)
    else:
        return HttpResponseNotFound()