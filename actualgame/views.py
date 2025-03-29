from django.shortcuts import render, redirect

def start_page(request):
    return render(request, 'start_page.html')

def menu(request):
    return render(request, 'menu.html')

def select_bin(request):
    return render(request, 'select_bin.html')

def recycling_game(request):
    return render(request, 'recycling_game.html')

def compost_bin(request):
    return render(request, 'compost_game.html')

def ewaste_bin(request):
    return render(request, 'ewaste_bin.html')

def trash_bin(request):
    return render(request, 'trash_bin.html')

def rules(request):
    return render(request, 'rules.html')

def exit_game(request):
    # For now, redirect back to the start page
    return redirect('start_page')

def game_page(request):
    return render(request, 'recycling_game.html')

