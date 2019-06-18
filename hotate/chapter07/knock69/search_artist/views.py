from django.shortcuts import render
from .models import ArtistDB


def search_artist(request):
    search = request.GET.get('search')
    limit = request.GET.get('limit')
    mode = request.GET.get('mode')
    db = ArtistDB()
    if search:
        limit = int(limit)
        if mode == 'artist_name':
            context = {
                'result': db.search_artist(search, limit),
            }
        elif mode == 'area':
            context = {'result': db.search_area(search, limit)}
        elif mode == 'aliases_name':
            context = {'result': db.search_aliases_name(search, limit)}
        elif mode == 'tag':
            context = {'result': db.search_tag(search, limit)}
    else:
        context = {}

    return render(request, 'search_artist/search.html', context)
