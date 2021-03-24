from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("This is a place holder for blogs")

def new(request):
    return HttpResponse("This is a placeholder for the form for new blogs")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f'The blog number is {number}')

def edit(request, number):
    return HttpResponse(f'Placeholder to edit blog {number}')

def destroy(request, number):
    return redirect('/')

# def profile(request):
#     context = {
#     	"name": "Noelle",
#     	"favorite_color": "turquoise",
#     	"pets": ["Bruce", "Fitz", "Georgie"]
#     }
#     return render(request, "index.html", context)

# def fav_num(request, fav_num):
#     return redirect("/profile")
