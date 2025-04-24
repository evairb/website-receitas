from django.urls import path
from authors import views

app_name = 'authors'
urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('register/create/', views.register_create, name="create"),
    path('intranet/', views.formulario_intra, name="intranet"),
    path(
        'intranet/create/',
        views.formulario_intra_create,
        name="intranet_create"
    ),
    path('login/', views.login_view, name="login"),
    path('login/create/', views.login_create, name="login_create"),
    path('logout/', views.logout_view, name="logout"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path(
        'dashboard/recipe/new/',
        views.DashboardRecipe.as_view(),
        name='dashboard_recipe_new'
    ),
    path(
        'dashboard/recipe/delete/',
        views.DashboardRecipeDelete.as_view(),
        name='dashboard_recipe_delete'
    ),
    path(
        'dashboard/recipe/<int:id>/edit/',
        views.DashboardRecipe.as_view(),
        name='dashboard_recipe_edit'
    ),
]
