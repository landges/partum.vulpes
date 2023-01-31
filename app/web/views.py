from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class MainView(View):
    def get(self, request):
        print('here')
        form=''
        products=[]
        return render(request, 'index.html', context={"form":form,
                                                      "products":products})

    def post(self,request):
        pass