from django.urls import path

from . import views


app_name = "polls"

urlpatterns = [
    # ex: /polls/
    # path("", views.index, name="index"), # HARD VIEW
    path("", views.IndexView.as_view(), name="index"), # GENERIC VIEW
    
    # ex: /polls/5/
    # path("<int:question_id>/", views.detail, name="detail"), # HARD VIEW
    # # added the word 'specifics' then have two routes that do the same
    # path("specifics/<int:question_id>/", views.detail, name="detail"), # HARD VIEW
    path("<int:pk>/", views.DetailView.as_view(), name="detail"), # GENERIC VIEW

    # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"), # HARD VIEW
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"), # GENERIC VIEW

    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"), # views complexa não entram no conceito de GENERIC VIEW
]
