from django.http import JsonResponse
from ..models import Post, Megusta, Comment, Amigos, Soporte
from django.contrib.auth.models import User

def routes(request):
    routes =[
        'GET /api/usuarios',
        'GET /api/amigos/<str:usuario>',
        'GET /api/posts/<str:usuario>',
        'GET /api/seguir/<str:usuario1>/<str:usuario2>',
    ]
    return JsonResponse(routes, safe=False)

def usuarios(request):
    usuarios= User.objects.all()
    data = []
    for usuario in usuarios:
        data.append({
            'username': usuario.username,
            'first_name': usuario.first_name,
            'last_name' : usuario.last_name,
            'email': usuario.email
        })

    return JsonResponse(data, safe=False)

def amigos(request, usuario):
    data=[]
    id = User.objects.get(username=usuario)
    amigos = Amigos.objects.filter(user=id)
    for amigo in amigos:
        data.append({
            'username': amigo.follow.username,
            'first_name': amigo.follow.first_name,
            'last_name' : amigo.follow.last_name,
        })
    return JsonResponse(data, safe=False)

def posts(request, usuario):
    data=[]
    id = User.objects.get(username=usuario)
    posts = Post.objects.filter(user=id)
    for post in posts:
        comentariosData = []
        comentarios = Comment.objects.filter(post=post)
        for comentario in comentarios:
            comentariosData.append({
                'username': comentario.user.username,
                'text': comentario.text
            })
        megustasData =[]
        megustas = Megusta.objects.filter(post=post)
        for megusta in megustas:
            megustasData.append({
                'username': megusta.user.username,
            })
        data.append({
            'username' : id.username,
            'text': post.text,
            'comentarios': comentariosData,
            'megustas': megustasData
        })
    return JsonResponse(data, safe=False)


def seguir(request, usuario1, usuario2):
    usuario = User.objects.get(username=usuario1)
    follow = User.objects.get(username=usuario2)
    try:
        comprobar= Amigos.objects.get(user=usuario, follow=follow)
        data = {'message': f'{usuario1} ya sigue a {usuario2}'}
    except:
        amigo = Amigos(user=usuario, follow=follow)
        amigo.save()
        data = {'message': f'{usuario1} acaba de convertirse en michiamigo de {usuario2}'}
    return JsonResponse(data, safe=False)

