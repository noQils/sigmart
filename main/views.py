from django.shortcuts import render

def show_main(request):
    context = {
        'app' : 'SigMart',
        'name': 'Daffa Aqil Mahmud',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
