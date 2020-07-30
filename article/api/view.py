from rest_framework.generics import( 
ListAPIView , RetrieveAPIView ,
CreateAPIView , UpdateAPIView ,
DestroyAPIView)

from article.models import Article
from .serializers import ArticleSerializer
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class ListView(ListAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer


class DetailView(RetrieveAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer


class CreateView(CreateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer


class UpdateView(UpdateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class DestroyView(DestroyAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter	 	