from django.shortcuts import render
from rest_framework import generics
from .models import Category, Recipe
from .serializer import CategorySerializer, RecipeSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeByCategoryList(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        categoryId = self.kwargs['categoryId']
        return Recipe.objects.filter(category_id=categoryId)