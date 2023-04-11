from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post, Comment, Amigos, Soporte, Megusta
from django.db.models import Q
from functools import reduce

# Create your views here.

def registerPage(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        email= request.POST.get('email')
        name= request.POST.get('firs_name')
        last_name= request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if (password != confirm_password):
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('/registro')
        User.objects.create_user(username, email =email, first_name=name, last_name=last_name, password=password)
        return redirect('/login')
    return render(request,'registerPage.html')

            
def soportePage(request):
    if (request.method == 'POST'):
        email = request.POST.get('email')
        sugerencia = request.POST.get('sugerencia')
        Soporte.objects.create(text = sugerencia, email = email)
        messages.success(request, 'Se envio la sugerencia')

    return render (request,'soporte.html')

def loginPage(request):
    if (request.method == 'POST'):
        username= request.POST.get('username')
        password= request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Se inició sesión correctamente')
                return redirect('/')
        messages.success(request, 'Datos incorrectos')
    

    return render(request,'login.html')

def logoutPage(request):
    logout(request)
    return redirect ('/login/')

def home(request):
    if str(request.user) == 'AnonymousUser':
        return redirect('/login/')
    follows = Amigos.objects.filter(user= request.user)
    
    # listaFollows =[]
    # for follow in follows:
    #     listaFollows.append(Q(user=follow.follow))
    #     print(follow.follow)
    listaFollows= [Q(user=follow.follow) for follow in follows]

    filtro=[Q(user=request.user)]+ listaFollows
    filtroT= reduce(lambda x, y:x | y, filtro)
    publicaciones = Post.objects.filter(filtroT).order_by('-created')
    data={
        'posts': publicaciones,

    }
    # id_admin = User.objects.get(username='admin')
    # posts= Post.objects.filter(Q(user=request.user)|Q(user=id_admin.id)).order_by('-created')
    return render (request,'home.html', data)

def perfilPage(request):
    if str(request.user) == 'AnonymousUser':
        return redirect('/login/')
    usuario = User.objects.get(username=request.user)
    posts= Post.objects.filter(user=request.user).order_by('-created')
    if len(posts) == 0: posts = None
    data = {'usuario':usuario, 'posts': posts}   
    return render (request,'perfil.html', data)

def publicacion(request):
    id = request.POST.get('id')
    text = request.POST.get('text')
    if(id is None and text !=''):
        Post.objects.create(text = text,user = request.user)
        messages.success(request, 'Post creado correctamente')
    return redirect('/')

def comentar(request):
    p = Post.objects.get(id = request.POST.get('post'))
    Comment.objects.create(
        text = request.POST.get('text'),
        user = request.user,
        post = p
    )
    return redirect('/')

def amigos(request):
    usuarios = User.objects.all()
    agregados = Amigos.objects.filter(user=request.user)
    usuario = User.objects.get(username=request.user)
    sugerencias= []
    for i in usuarios:
        coincide= False
        for e in agregados:
            if i == e.follow:
                coincide = True 
                break

        if not coincide:
            sugerencias.append(i)

    data ={
        'usuarios':usuarios,
        'usuario' : usuario,
        'agregados': agregados,
        'sugerencias': sugerencias
    }
    
    return render (request,'amigos.html', data)

def megusta(request):
    usuario = User.objects.get(username=request.user)
    pId = request.POST.get('megusta')
    post = Post.objects.get(id=pId)
    try:
        comprobar = Megusta.objects.get(user= usuario, post= post)
        comprobar.delete()
    except:
        Megusta.objects.create(user = request.user,post = post)
    return redirect('/')

def seguir(request):
    follow = request.POST.get('amigo')
    usuario = User.objects.get(username=request.user)
    follow = User.objects.get(username=follow)
    try:
        comprobar= Amigos.objects.get(user=usuario, follow=follow)
    except:
        amigo = Amigos(user=usuario, follow=follow)
        amigo.save()
   

    return redirect('/amigos/')

def eliminar(request):
    follow = request.POST.get('amigo')
    usuario = User.objects.get(username=request.user)
    follow = User.objects.get(username=follow)
    amistad= Amigos.objects.get(user=usuario, follow=follow)
    amistad.delete()

    return redirect('/amigos/')

