from django.shortcuts import render

def index(request):
  return render(request, "index.html") # Le decimos que renderice la página index.html

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
    ]
    return render(request, 'musica.html', {'albums': albums})

def programacion(request):
  return render(request, "programacion.html")

def audiovisual(request):
    videos = [
        {'url': 'https://www.youtube.com/embed/0sNpG2cWJIo?si=9tVS0Ne3y1oh4ZI0'},
        {'url': 'https://www.youtube.com/embed/EjIRvxLIpww?si=k_nauj2GWHeq1m89'},
        {'url': 'https://www.youtube.com/embed/3XKruCUB1PM?si=4jNRPAQplrGkD0TY'},
        {'url': 'https://www.youtube.com/embed/b_Ya02k5DMg?si=VYL53zDtYEODEyz8'},
        {'url': 'https://www.youtube.com/embed/X7bzjwnF90k?si=fVPJ7iQuyMbXSmyL'},
        {'url': 'https://www.youtube.com/embed/NhRT8yUaxMc?si=zNMIRGM54mDfL4Hx'},
    ]
    return render(request, 'audiovisual.html', {'videos': videos})

def fotografia(request):
  return render(request, "fotografia.html") 

def contacto(request):
  return render(request, "contacto.html")
