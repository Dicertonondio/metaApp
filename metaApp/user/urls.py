from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from user.views import CustomLoginView, profile
from user.forms import LoginForm

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='user/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)