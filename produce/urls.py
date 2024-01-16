from django.urls import path, include


from .views import (ProductView, DetailUserView, DetailProductView,
                    CategoryView, DetailCategoryView, OrderView,
                    CreateProductView,RegisterUserView,
                    )

urlpatterns = [

    path('', ProductView.as_view()),
    path('product/<int:pk>/', DetailProductView.as_view()),
    path('product/create/', CreateProductView.as_view()),
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', DetailCategoryView.as_view()),
    path('order/', OrderView.as_view()),
    path('register/user/', RegisterUserView.as_view()),
    path('user/<str:username>/<str:password>/', DetailUserView.as_view()),

]