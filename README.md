# Portfolio Personal - Django

Portfolio desarrollado con Django que incluye secciones de biografía, programación, música, audiovisual, fotografía y contacto.

🔗 Puedes ver la web aquí:  
👉 [**https://cvallejo.pythonanywhere.com**](https://cvallejo.pythonanywhere.com)

## 🚀 Características

- **Arquitectura Django**: Uso de vistas, templates y configuración modular
- **Herencia de plantillas**: Sistema de templates reutilizables
- **Gestión de contenido estático**: CSS, imágenes y documentos
- **Formulario de contacto**: Envío de emails con Gmail SMTP
- **Variables de entorno**: Configuración segura con python-decouple
- **Despliegue en producción**: PythonAnywhere

## 📁 Estructura del Proyecto

```
web-con-django-portfolio/
├── portfolio/              # Aplicación principal
│   ├── settings.py        # Configuración Django
│   ├── urls.py            # Rutas principales
│   └── views.py           # Lógica de vistas
├── templates/             # Plantillas HTML
│   ├── base.html          # Template base (herencia)
│   ├── index.html
│   ├── bio.html
│   ├── programacion.html
│   ├── musica.html
│   ├── audiovisual.html
│   ├── fotografia.html
│   ├── contacto.html
│   └── includes/          # Componentes reutilizables
│       ├── cabecera.html
│       ├── menu.html
│       └── pie.html
├── static/                # Archivos estáticos
│   ├── css/
│   ├── images/
│   └── docs/
└── manage.py
```

## 🔧 Extractos de Código

### 1. Herencia de Plantillas

**Base template** (`templates/base.html`):
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carlos Vallejo - Portfolio</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    {% include "includes/cabecera.html" %}
    
    {% block content %}
    <!-- Contenido específico de cada página -->
    {% endblock %}
    
    {% include "includes/pie.html" %}
</body>
</html>
```

**Template hijo** (`templates/bio.html`):
```html
{% extends "base.html" %}
{% load static %}

{% block content %}
<div class="contacto-section">
  <div class="bio-content">
    <div class="bio-text">
      <h2>Sobre mí</h2>
      <p>Contenido de la biografía...</p>
    </div>
    <div class="bio-sidebar">
      <div class="bio-img">
        <img src="{% static 'images/carlos-vallejo-bio.jpg' %}" alt="Bio Carlos Vallejo">
      </div>
    </div>
  </div>
</div>
{% endblock %}
```

### 2. Definición de Rutas

**URLs principales** (`portfolio/urls.py`):
```python
from django.contrib import admin
from django.urls import path
from portfolio.views import contacto, index, musica, programacion, fotografia, audiovisual, bio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('bio', bio, name="bio"),
    path('musica', musica, name="musica"),
    path('programacion', programacion, name="programacion"),
    path('audiovisual', audiovisual, name="audiovisual"),
    path('fotografia', fotografia, name="fotografia"),
    path('contacto', contacto, name="contacto"),
]
```

### 3. Vistas con Contexto Dinámico

**Vista de fotografía** (`portfolio/views.py`):
```python
def fotografia(request):
    fotos = [
        {
            'page_url': 'https://www.flickr.com/photos/113666935@N06/54891143659/in/album-72177720330019503',
            'img_url': 'https://live.staticflickr.com/65535/54891143659_0334204675_3k.jpg',
            'title': 'Spotmatic-Ilford-HP5-Octubre-2025-17'
        },
        {
            'page_url': 'https://www.flickr.com/photos/113666935@N06/54776980347/in/dateposted-public/',
            'img_url': 'https://live.staticflickr.com/65535/54776980347_c062fc9a82_3k.jpg',
            'title': 'feria-mijas-2025-73'
        },
        # Más fotos...
    ]
    
    context = {
        'fotos': fotos,
        'social_media': SOCIAL_MEDIA
    }
    return render(request, "fotografia.html", context)
```

**Template correspondiente** (`templates/fotografia.html`):
```html
{% extends "base.html" %}
{% load static %}

{% block content %}
<section class="fotografia-section">
  <div class="fotos-grid">
    {% for foto in fotos %}
      <div class="foto-item">
        <a href="{{ foto.page_url }}" target="_blank">
          <img src="{{ foto.img_url }}" alt="{{ foto.title }}">
        </a>
      </div>
    {% endfor %}
  </div>
</section>
{% endblock %}
```

### 4. Uso de Static Files

**Carga de archivos estáticos en templates**:
```html
{% load static %}

<!-- CSS -->
<link rel="stylesheet" href="{% static 'css/styles.css' %}">

<!-- Imágenes -->
<img src="{% static 'images/charlitos-avatar-web.jpg' %}" alt="Carlos Vallejo">

<!-- Documentos -->
<a href="{% static 'docs/CV-Carlos-Vallejo.pdf' %}" target="_blank">
  📄 Descargar CV
</a>
```

**Configuración en settings.py**:
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Para producción
```

### 5. Formulario de Contacto con Email

**Vista de contacto** (`portfolio/views.py`):
```python
from django.core.mail import send_mail

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')
        
        try:
            mensaje_completo = f"""
            Nuevo mensaje de contacto
            
            Nombre: {nombre}
            Email: {email}
            Asunto: {asunto}
            
            Mensaje:
            {mensaje}
            """
            
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
            context = {'error': 'Error al enviar el mensaje.', 'social_media': SOCIAL_MEDIA}
            return render(request, "contacto.html", context)
    
    context = {'social_media': SOCIAL_MEDIA}
    return render(request, "contacto.html", context)
```

**Template del formulario**:
```html
<form method="POST" action="{% url 'contacto' %}">
    {% csrf_token %}
    <input type="text" name="nombre" placeholder="Tu nombre" required>
    <input type="email" name="email" placeholder="Tu email" required>
    <input type="text" name="asunto" placeholder="Asunto" required>
    <textarea name="mensaje" placeholder="Tu mensaje" required></textarea>
    <button type="submit">Enviar Mensaje</button>
</form>

{% if mensaje_enviado %}
    <p class="success-message">¡Mensaje enviado correctamente!</p>
{% endif %}

{% if error %}
    <p class="error-message">{{ error }}</p>
{% endif %}
```

### 6. Variables de Entorno

**Configuración segura** (`portfolio/settings.py`):
```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = ['cvallejo.pythonanywhere.com']

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'carlosd.vallejo@gmail.com'
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
```

## 🛠️ Tecnologías Utilizadas

| Tecnología | Descripción |
|-------------|-------------|
| ![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white) | Framework web de Python para el backend |
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | Lenguaje de programación principal (v3.10) |
| ![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) | Estructura y contenido de las páginas |
| ![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white) | Estilos, diseño visual y animaciones |
| ![python-decouple](https://img.shields.io/badge/python--decouple-3.8-green) | Gestión segura de variables de entorno |
| ![Gmail SMTP](https://img.shields.io/badge/Gmail_SMTP-EA4335?logo=gmail&logoColor=white) | Servidor de correo para formulario de contacto |
| ![PythonAnywhere](https://img.shields.io/badge/PythonAnywhere-1D9FD7?logo=python&logoColor=white) | Plataforma de despliegue en producción |
| ![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white) | Control de versiones |
| ![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white) | Repositorio remoto y colaboración |

## 📦 Instalación Local

```bash
# Clonar el repositorio
git clone https://github.com/cdvallejo/web-con-django-portfolio.git
cd web-con-django-portfolio

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Crear archivo .env con las variables necesarias
# SECRET_KEY=tu-secret-key
# EMAIL_HOST_PASSWORD=tu-app-password
# DEBUG=True

# Ejecutar servidor de desarrollo
python manage.py runserver
```

## 📚 Proyecto académico

💡 Proyecto realizado para la asignatura **"Desarrollo de aplicaciones web en el entorno servidor"**  
📜 Dentro del **Certificado de Desarrollo de Aplicaciones con Tecnología Web (IFCD2010)**  
🏫 Impartido por el **CPIFP Alan Turing**  
👨‍🏫 Profesor: **Luis José Sánchez González**

---

Si te ha gustado este proyecto, ¡no olvides dejar una ⭐ en el repositorio!

---
## Galería:
<img width="1211" height="859" alt="1" src="https://github.com/user-attachments/assets/33412cb7-37b5-4d62-b7a7-7eae2b743bee" />


<img width="1140" height="744" alt="2" src="https://github.com/user-attachments/assets/6c5a7d67-520a-4a97-bb9b-d49d5098705d" />


<img width="1140" height="744" alt="2" src="https://github.com/user-attachments/assets/3b6f2109-9264-4070-9abd-72a72293251b" />

