from django.shortcuts import render
from pyswip import Prolog

def get_recommendations(request):
    prolog = Prolog()
    prolog.consult("recommendation_rules.pl")

    user_preferences = list(UserPreference.objects.filter(user=request.user))
    genres = [up.genre for up in user_preferences]

    recommendations = list(prolog.query(f"product_genre(Title, Genre), member(Genre, {genres})"))

    context = {
        'recommendations': recommendations
    }
    return render(request, 'recommendations/recommendations.html', context)
