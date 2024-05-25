from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q

from .models import TextPdf
from .forms import TextPdfForm, SignUpForm


def app(request):
    context = {}

    if request.user.is_authenticated:
        username = request.user.username
        # Do something with the username
        context['logger'] = username

    files = TextPdf.objects.all().order_by('-date')

    context['doc_files'] = files[:20]

    context['total_files'] = files.count()
    return render(request, 'index.html', context)


def discover(request):
    context = {}

    if request.user.is_authenticated:
        username = request.user.username
        # Do something with the username
        context['logger'] = username

    if request.method == 'GET':
        search = request.GET.get('searcher')

        if search is not None:
            context['search'] = search
            files = TextPdf.objects.filter(Q(title__contains=search) | Q(descr__contains=search) |
                                           Q(author__contains=search)).order_by('-date')

            # choose a few
            context['doc_files'] = files[:12]
            context['total_files'] = files.count()
            context['search'] = search
            return render(request, 'explorer.html', context)
        else:
            pass

    context['doc_files'] = TextPdf.objects.all().order_by('-date')[:12]
    return render(request, 'explorer.html', context)


def register_user(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have registered successfully.")
            return redirect('home')
        else:
            messages.success(request, "Problem occurred, enter all valid info and unique username.")
            return redirect('signin')
    else:
        return render(request, 'signin.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully, thank you.')
            return redirect('home')
        else:
            messages.success(request, 'You may have put wrong user auth, please retry.')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully, see ya.")
    return redirect('home')


def uploadText(request):
    submitted = False

    if request.method == "POST":
        form = TextPdfForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)

            if request.user.is_authenticated:
                instance.author = request.user.username

            instance.save()
            return HttpResponseRedirect('/uploadfile?submitted=True')
        else:
            messages.success(request, "An error occurred, enter valid data [urls].")
    else:
        form = TextPdfForm()

        if 'submitted' in request.GET:
            submitted = True

    context = {'submitted': submitted, 'form': form}

    return render(request, 'uploadnotes.html', context)


def terms_and_conditions(request):
    return render(request, 'terms.html', {})


def load_more(request):
    # files
    offset_f = request.GET.get('offset_f')
    offset_f_int = int(offset_f)
    limit_f = 12

    # get all
    post_f_obj = list(TextPdf.objects.values().order_by('-date')[offset_f_int:(offset_f_int + limit_f)])

    # send all
    data = {'posts_f': post_f_obj}
    return JsonResponse(data=data)


def load_more_search(request):
    search = request.GET.get('search')

    if search is None:
        return JsonResponse({})

    # files
    offset_f = request.GET.get('offset_f')
    offset_f_int = int(offset_f)
    limit_f = 12

    # get all
    post_f_obj = list(TextPdf.objects.filter(
        Q(title__contains=search) |
        Q(author__contains=search)).values().order_by('-date')[offset_f_int:(offset_f_int + limit_f)])

    # send all
    data = {'posts_f': post_f_obj}
    return JsonResponse(data=data)
