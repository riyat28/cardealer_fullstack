# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
path('register/', views.User, name='register'),
    # path for login
     path(route='login', view=views.login_user, name='login'),
    # path for dealer reviews view
         path(route='get_cars', view=views.get_cars, name ='getcars'),
         path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
        path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_details'),
            path(route='add_review', view=views.add_review, name='add_review'),
    # path for add a review view

    # Add the logout path
    path('logout/', views.login_user, name='logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
