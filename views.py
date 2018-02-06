from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'news_blog/index.html', {'articles':articles})
articles = [
   {
       'id': 1,
       'title': 'OH MY GOD',
       'text': 'This is demo of secvernation guide'
   },
   {
       'id': 2,
       'title': 'SO I LIKE THIS SHIT',
       'text': 'DNA is a trash'
   }]
