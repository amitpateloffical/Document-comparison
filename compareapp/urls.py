from django.urls import path
from compareapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),

    # User Management system
    path('user-management/', views.userManagement, name="user-management"),

    # View analytics
    path('analytics', views.analytics, name="analytics"),


    # For Document upload
    path('form/', views.formView, name="form"),
    path('form/view/<int:doc_id>/', views.documentDetail, name="view-document"),
    path('form/initial-documents', views.initialDocument, name="initial-document"),
    path('form/remove/<int:doc_id>/', views.removeDocument, name="remove-doc"),
    
    # For comparison
    path('comparison/view/<str:report_id>', views.viewComparison, name="view-comparison"),
    path('comparison/', views.comparison, name="compare"),
    path('comparison/preview/<str:report>', views.preview, name="preview"),

    # To chatPDF
    path('upload-pdf/', views.uploadPDF, name='upload-pdf'),
    path('proxy-chat-pdf/', views.proxy_chat_pdf, name='proxy-chat-pdf'),

    # Password Resetting
    path('password_reset/', views.password_reset_request, name='password_reset'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

]
