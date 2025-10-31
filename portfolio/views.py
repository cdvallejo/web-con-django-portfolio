from django.shortcuts import render

# Redes sociales globales
SOCIAL_MEDIA = [
    {
        'name': 'YouTube',
        'url': 'https://www.youtube.com/@carlosvallejomusic',
        'icon': 'images/youtube.png'
    },
    {
        'name': 'Instagram',
        'url': 'https://www.instagram.com/carlosd.vallejo/',
        'icon': 'images/instagram.png'
    },
    {
        'name': 'Bandcamp',
        'url': 'https://carlosvallejo.bandcamp.com/',
        'icon': 'images/bandcamp.png'
    },
    {
        'name': 'LinkedIn',
        'url': 'https://www.linkedin.com/in/carlos-d-vallejo-aranda-569685a5/',
        'icon': 'images/linkedn.png'
    },
    {
        'name': 'GitHub',
        'url': 'https://github.com/cdvallejo',
        'icon': 'images/github.png'
    },
    {
        'name': 'SoundCloud',
        'url': 'https://soundcloud.com/carlos-d-vallejo',
        'icon': 'images/soundcloud.png'
    },
    {
        'name': 'Twitter/X',
        'url': 'https://twitter.com/carlvallejo',
        'icon': 'images/x-twitter.jpg'
    }
]

def index(request):
  context = {'social_media': SOCIAL_MEDIA}
  return render(request, "index.html", context)

def bio(request):
  context = {'social_media': SOCIAL_MEDIA}
  return render(request, "bio.html", context)

def musica(request):
    albums = [
        {
            'url': 'https://bandcamp.com/EmbeddedPlayer/album=1268864362/size=large/bgcol=ffffff/linkcol=7137dc/transparent=true/',
            'link': 'https://carlosvallejo.bandcamp.com/album/kid-ball-adventure',
            'title': 'Kid Ball Adventure de Carlos Vallejo',
            'width': '350px',
            'height': '786px'
        },
        {
            'url': 'https://bandcamp.com/EmbeddedPlayer/album=1834263837/size=large/bgcol=ffffff/linkcol=7137dc/transparent=true/',
            'link': 'https://carlosvallejo.bandcamp.com/album/cuando-no-est-lola',
            'title': 'Cuando no esté Lola de Carlos Vallejo',
            'width': '350px',
            'height': '720px'
        },
        {
            'url': 'https://bandcamp.com/EmbeddedPlayer/album=234291138/size=large/bgcol=ffffff/linkcol=7137dc/transparent=true/',
            'link': 'https://carlosvallejo.bandcamp.com/album/magical-prisma-2',
            'title': 'Magical Prisma de Carlos Vallejo',
            'width': '350px',
            'height': '786px'
        },
        {
            'url': 'https://bandcamp.com/EmbeddedPlayer/album=477987698/size=large/bgcol=ffffff/linkcol=7137dc/transparent=true/',
            'link': 'https://carlosvallejo.bandcamp.com/album/rebobine-por-favor',
            'title': 'Rebobine por favor de Carlos Vallejo',
            'width': '350px',
            'height': '588px'
        },
        {
            'url': 'https://bandcamp.com/EmbeddedPlayer/album=1602343228/size=large/bgcol=ffffff/linkcol=7137dc/tracklist=false/transparent=true/',
            'link': 'https://carlosvallejo.bandcamp.com/album/trafalgar-el-viaje',
            'title': 'Trafalgar: El viaje by Carlos Vallejo',
            'width': '350px',
            'height': '470px'
        },
        {
            'url': 'https://bandcamp.com/EmbeddedPlayer/track=4204268653/size=large/bgcol=ffffff/linkcol=7137dc/tracklist=false/transparent=true/',
            'link': 'https://carlosvallejo.bandcamp.com/track/peque-a-nana',
            'title': 'Pequeña nana by Carlos Vallejo',
            'width': '350px',
            'height': '442px'
        },
        {
            'url': 'https://bandcamp.com/EmbeddedPlayer/album=3171781393/size=large/bgcol=ffffff/linkcol=7137dc/transparent=true/',
            'link': 'https://carlosvallejo.bandcamp.com/album/educatpals',
            'title': 'EducatPals by Carlos Vallejo',
            'width': '350px',
            'height': '621px'
        },
        {
            'url': 'https://bandcamp.com/EmbeddedPlayer/track=1507940757/size=large/bgcol=ffffff/linkcol=7137dc/tracklist=false/transparent=true/',
            'link': 'https://carlosvallejo.bandcamp.com/track/lugar-soleado-yasunari-kawabata-audiolibro',
            'title': 'Lugar Soleado (Yasunari Kawabata) - Audiolibro by Carlos Vallejo',
            'width': '350px',
            'height': '442px'
        },
        {
            'url': 'https://bandcamp.com/EmbeddedPlayer/album=2636471890/size=large/bgcol=ffffff/linkcol=7137dc/tracklist=false/transparent=true/',
            'link': 'https://estudioabrego.bandcamp.com/album/noahmund',
            'title': 'Noahmund de Carlos Vallejo',
            'width': '350px',
            'height': '470px'
        },
    ]
    context = {
        'albums': albums,
        'social_media': SOCIAL_MEDIA
    }
    return render(request, 'musica.html', context)

def programacion(request):
    projects = [
        {
            'emoji': '💼',
            'title': 'Portfolio Personal',
            'technologies': ['Django', 'Python', 'HTML/CSS'],
            'description': 'Consulta el código del portfolio profesional que estás viendo. Desarrollado con Django.',
            'github': 'https://github.com/cdvallejo/web-con-django-portfolio'
        },
        {
            'emoji': '🗄️',
            'title': 'CRUD de Actuaciones',
            'technologies': ['PHP', 'MySQL', 'HTML/CSS', 'Javascript'],
            'description': 'Aplicación web con funcionalidades CRUD (Create, Read, Update, Delete) desarrollada con PHP, HTML, CSS, Bootstrap y algo de JavaScript.',
            'github': 'https://github.com/cdvallejo/actuaciones'
        },
        {
            'emoji': '🔌',
            'title': 'Base de datos MongoDB - FastAPI',
            'technologies': ['Python', 'FastAPI', 'MongoDB', 'Docker'],
            'description': 'API RESTful desarrollada con Python, FastAPI y MongoDB, que muestra una colección de obras artísticas.',
            'github': 'https://github.com/cdvallejo/fastapi-mongodb-con-docker-obras-v2'
        },
    ]
    
    skills_categories = [
        {
            'category': 'Lenguajes',
            'items': [
                {
                    'name': 'Python',
                    'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg',
                    'level': 'Intermedio'
                },
                {
                    'name': 'JavaScript',
                    'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg',
                    'level': 'Intermedio'
                },
                {
                    'name': 'Java',
                    'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg',
                    'level': 'Intermedio'
                },
                {
                    'name': 'C',
                    'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg',
                    'level': 'Intermedio'
                },
            ]
        },
        {
            'category': 'Frameworks',
            'items': [
                {
                    'name': 'Django',
                    'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg',
                    'level': 'Intermedio'
                },
                {
                    'name': 'Angular',
                    'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/angular/angular-original.svg',
                    'level': 'Intermedio'
                },
            ]
        },
        {
            'category': 'Frontend',
            'items': [
                {
                    'name': 'HTML5',
                    'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg',
                    'level': 'Intermedio'
                },
                {
                    'name': 'CSS3',
                    'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg',
                    'level': 'Intermedio'
                },
            ]
        },
        {
            'category': 'Bases de Datos',
            'items': [
                {
                    'name': 'MySQL',
                    'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg',
                    'level': 'Intermedio'
                },
                {
                    'name': 'MongoDB',
                    'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg',
                    'level': 'Intermedio'
                },
            ]
        },
        {
            'category': 'Herramientas & Cloud',
            'items': [
                {
                    'name': 'Git',
                    'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg',
                    'level': 'Intermedio'
                },
                {
                    'name': 'Docker',
                    'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg',
                    'level': 'Intermedio'
                },
                {
                    'name': 'AWS',
                    'icon': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg',
                    'level': 'Básico'
                },
            ]
        },
    ]
    context = {
        'projects': projects,
        'skills_categories': skills_categories,
        'social_media': SOCIAL_MEDIA
    }
    return render(request, "programacion.html", context)

def audiovisual(request):
    videos = [
        {'url': 'https://www.youtube.com/embed/0sNpG2cWJIo?si=9tVS0Ne3y1oh4ZI0'},
        {'url': 'https://www.youtube.com/embed/EjIRvxLIpww?si=k_nauj2GWHeq1m89'},
        {'url': 'https://www.youtube.com/embed/3XKruCUB1PM?si=4jNRPAQplrGkD0TY'},
        {'url': 'https://www.youtube.com/embed/b_Ya02k5DMg?si=VYL53zDtYEODEyz8'},
        {'url': 'https://www.youtube.com/embed/X7bzjwnF90k?si=fVPJ7iQuyMbXSmyL'},
        {'url': 'https://www.youtube.com/embed/NhRT8yUaxMc?si=zNMIRGM54mDfL4Hx'},
    ]
    context = {
        'videos': videos,
        'social_media': SOCIAL_MEDIA
    }
    return render(request, 'audiovisual.html', context)

def fotografia(request):
    fotos = [
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54891143659/in/album-72177720330019503', 'img_url': 'https://live.staticflickr.com/65535/54891143659_0334204675_3k.jpg', 'title': 'Spotmatic-Ilford-HP5-Octubre-2025-17'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54776980347/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54776980347_c062fc9a82_3k.jpg', 'title': 'feria-mijas-2025-73'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54778069693/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54778069693_f7d4a5df48_6k.jpg', 'title': 'feria-mijas-2025-22'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54750318229/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54750318229_f393f9e36b_6k.jpg', 'title': 'Hotel en ruidas en pantano de Casasola (29)'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54750258629/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54750258629_9545ab8ed5_6k.jpg', 'title': 'feria_malaga_2025-66'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54742407400/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54742407400_6d37c8ee4a_3k.jpg', 'title': 'CineStill50D-Canon-Jun25 (32)'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54722537845/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54722537845_8fa3617756_3k.jpg', 'title': 'genalguacil-agos-2025-21'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54528448625/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54528448625_b77a117d33_3k.jpg', 'title': 'DSCF1733'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54528290804/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54528290804_907f0dfd59_3k.jpg', 'title': 'dia_museos_2025-12'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54053314191/in/album-72177720321003992', 'img_url': 'https://live.staticflickr.com/65535/54053314191_8280784052_3k.jpg', 'title': 'Coche con patas'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54512649298/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54512649298_05af07046d_3k.jpg', 'title': 'feria_sevilla2025-80'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54741209777/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54741209777_abad2666c5_3k.jpg', 'title': 'CineStill50D-Canon-Jun25 (7)'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54474634267/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54474634267_65df3bc7be_3k.jpg', 'title': 'Luna'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54714455964/in/album-72177720328316699', 'img_url': 'https://live.staticflickr.com/65535/54714455964_08738f8dd0_3k.jpg', 'title': 'montoro-agos25-15'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54340909245/in/album-72177720325004226', 'img_url': 'https://live.staticflickr.com/65535/54340909245_26528c76dd_3k.jpg', 'title': 'Chica de espaldas mirando un menú'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54621804810/in/album-72177720325004226', 'img_url': 'https://live.staticflickr.com/65535/54621804810_f17f571ec2_3k.jpg', 'title': 'Crisol Muelle Uno'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54340909255/in/album-72177720325004226', 'img_url': 'https://live.staticflickr.com/65535/54340909255_ee104c8a99_3k.jpg', 'title': 'Noche en calle Alcazabilla'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/14596775931/in/album-72157645567479604/', 'img_url': 'https://live.staticflickr.com/3925/14596775931_116352c91a_3k.jpg', 'title': 'IMG_0951'},
        
    ]
    context = {
        'fotos': fotos,
        'social_media': SOCIAL_MEDIA
    }
    return render(request, "fotografia.html", context)

def contacto(request):
  if request.method == 'POST':
    nombre = request.POST.get('nombre')
    email = request.POST.get('email')
    asunto = request.POST.get('asunto')
    mensaje = request.POST.get('mensaje')
    
    try:
      from django.core.mail import send_mail
      
      # Cuerpo del email
      mensaje_completo = f"""
      Nuevo mensaje de contacto desde el portfolio
      
      Nombre: {nombre}
      Email: {email}
      Asunto: {asunto}
      
      Mensaje:
      {mensaje}
      """
      
      # Enviar email
      send_mail(
        subject=f'Portfolio - {asunto}',
        message=mensaje_completo,
        from_email='carlosd.vallejo@gmail.com',
        recipient_list=['carlosd.vallejo@gmail.com'],
        fail_silently=False,
      )
      
      context = {'mensaje_enviado': True, 'social_media': SOCIAL_MEDIA}
      return render(request, "contacto.html", context)
    
    except Exception as e:
      print(f"Error al enviar email: {e}")  # Para ver el error en la consola
      context = {'error': f'Error al enviar el mensaje. Por favor, intenta de nuevo.', 'social_media': SOCIAL_MEDIA}
      return render(request, "contacto.html", context)
  
  context = {'social_media': SOCIAL_MEDIA}
  return render(request, "contacto.html", context)
