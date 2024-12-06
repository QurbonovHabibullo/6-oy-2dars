from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Home sahifasini qaytaradi

def about(request):
    return render(request, 'about.html')  # About sahifasini qaytaradi

def contact(request):
    return render(request, 'contact.html')  # Contact sahifasini qaytaradi

def view4(request):
    return render(request, 'view4.html')

def view5(request):
    return render(request, 'view5.html')

def view6(request):
    return render(request, 'view6.html')

def view7(request):
    return render(request, 'view7.html')

def view8(request):
    return render(request, 'view8.html')

def view9(request):
    return render(request, 'view9.html')

def view10(request):
    return render(request, 'view10.html')