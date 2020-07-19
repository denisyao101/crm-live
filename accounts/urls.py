from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutView, name='logout'),

    path('products/', views.products, name='products'),
    path('customers/<int:pk>/', views.customers, name='customers'),
    path('create_order/', views.create_order, name='create_order'),
    path('update_order/<int:pk>/', views.update_order, name='update_order'),
    path('delete_order/<int:pk>/', views.delete_order, name='delete_order'),
    path('create_customer_order/<int:cid>/', views.create_customer_order, name='create_customer_order'),
    path('user/', views.user_page, name='user_page'),
    path('settings/', views.user_profile, name='settings'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),name="password_reset_complete"),

]
