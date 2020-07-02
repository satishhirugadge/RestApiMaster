from django.shortcuts import render

# Create your views here.

# def index6(request):
#     return render(request,"first_app/page1.html")
#
# def index7(request):
#     return render(request,"first_app/detail.html")
#
# def index8(request):
#     return render(request,"first_app/listing.html")
#
# def index9(request):
#     return render(request,"first_app/checkout.html")
#
# def index10(request):
#     return render(request,"first_app/register.html")

def login(request):
    return render(request,'register.html')