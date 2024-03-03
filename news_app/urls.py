from django.urls import path
from .views import news_list, news_detail,homePageView, ContactPageView, HomePageView, notFound

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/<int:id>/', news_detail, name='news_detail'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('404page/', notFound, name='404page'),
]
