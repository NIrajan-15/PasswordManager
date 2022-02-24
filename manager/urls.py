from django.urls import path
from . import views
urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('account_info/<str:key>', views.account_info, name='account_info'),
    path('addAccount/', views.addAccount, name='addAccount'),
    path('update_page/<str:key>', views.UpdateAccount, name='updateAccount' ),
    path('delete_page/<str:key>', views.DeleteAccount, name='deleteAccount'),
    path('kennedy_account/', views.kennedypage, name='kennedypage'),
    path('neighbor_account/', views.neighborspage, name='neighborspage'),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout')
]
