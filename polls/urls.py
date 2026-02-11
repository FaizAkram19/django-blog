from django.urls import path
from . import views

app_name="polls"
# we gave an app name because there can be multiple app which can have
# identical view names so in order to make sure that the {% url %} works
# we define each app_name so that we can write the view belongs to whih app
urlpatterns = [
    #/polls/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]