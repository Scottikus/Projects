from django.urls import path

from . import views

app_name = 'ruinGen'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:ruinName_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:ruinName_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:ruinName_id>/vote/', views.vote, name='vote'),

    path('ruinBuild/', views.ruinBuild, name='ruinBuild'),
]