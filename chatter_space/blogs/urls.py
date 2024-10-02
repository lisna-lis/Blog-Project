from django.urls import path
from blogs import views

urlpatterns = [
    path('blog/new/',views.BlogCreateView.as_view()),
    path('blog/<str:uuid>/',views.BlogRetreiveUpdateDeleteView.as_view()),
    path('blog/public/',views.PublicBlogListView.as_view()),
    path('blog/user/',views.UserBlogListView.as_view()),
    path('blog/public/<str:uuid>/',views.PublicBlogRetreiveView.as_view()),
]



