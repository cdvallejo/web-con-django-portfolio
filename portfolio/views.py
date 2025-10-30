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
    fotos = [
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54776980347/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54776980347_c062fc9a82_3k.jpg', 'title': 'feria-mijas-2025-73'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54778069693/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54778069693_f7d4a5df48_6k.jpg', 'title': 'feria-mijas-2025-22'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54750318229/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54750318229_f393f9e36b_6k.jpg', 'title': 'Hotel en ruidas en pantano de Casasola (29)'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54750258629/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54750258629_9545ab8ed5_6k.jpg', 'title': 'feria_malaga_2025-66'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54742407400/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54742407400_6d37c8ee4a_3k.jpg', 'title': 'CineStill50D-Canon-Jun25 (32)'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54722537845/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54722537845_8fa3617756_3k.jpg', 'title': 'genalguacil-agos-2025-21'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54528448625/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54528448625_b77a117d33_3k.jpg', 'title': 'DSCF1733'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54528290804/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54528290804_907f0dfd59_3k.jpg', 'title': 'dia_museos_2025-12'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54511521407/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54511521407_ca268722c8_3k.jpg', 'title': 'feria_sevilla2025-77'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54741209777/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54741209777_abad2666c5_3k.jpg', 'title': 'CineStill50D-Canon-Jun25 (7)'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54474634267/in/dateposted-public/', 'img_url': 'https://live.staticflickr.com/65535/54474634267_65df3bc7be_3k.jpg', 'title': 'Luna'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54714455964/in/album-72177720328316699', 'img_url': 'https://live.staticflickr.com/65535/54714455964_08738f8dd0_3k.jpg', 'title': 'montoro-agos25-15'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54340909245/in/album-72177720325004226', 'img_url': 'https://live.staticflickr.com/65535/54340909245_26528c76dd_3k.jpg', 'title': 'Chica de espaldas mirando un menú'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54621804810/in/album-72177720325004226', 'img_url': 'https://live.staticflickr.com/65535/54621804810_f17f571ec2_3k.jpg', 'title': 'Crisol Muelle Uno'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/54340909255/in/album-72177720325004226', 'img_url': 'https://live.staticflickr.com/65535/54340909255_ee104c8a99_3k.jpg', 'title': 'Noche en calle Alcazabilla'},
        {'page_url': 'https://www.flickr.com/photos/113666935@N06/14596775931/in/album-72157645567479604/', 'img_url': 'https://live.staticflickr.com/3925/14596775931_116352c91a_3k.jpg', 'title': 'IMG_0951'},
    ]
    return render(request, "fotografia.html", {'fotos': fotos})

def contacto(request):
  return render(request, "contacto.html")
