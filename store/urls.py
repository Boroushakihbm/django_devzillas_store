from django.urls import path

urlpatterns = [
    path('recipe/', RecipeList.as_view()),
]