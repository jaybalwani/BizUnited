from django.db.models import Q
from startups.models import Pitch

def searchQuery(request):
    query = ''
    if request.GET.get('query'):
        query = request.GET.get('query')
    pitches = Pitch.objects.distinct().filter(
        Q(title__icontains=query) | Q(entrepreneur__profile__first_name__icontains=query) | Q(entrepreneur__profile__last_name__icontains=query)
    )

    return query, pitches