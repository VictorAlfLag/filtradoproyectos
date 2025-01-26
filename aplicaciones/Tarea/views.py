import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Technology
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html')

# Listar todas las tecnologías
def list_technologies(request):
    technologies = Technology.objects.all()
    return render(request, "TECHNOLOGY/listadoTecnologias.html", {'technology_list': technologies})

def new_technology(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        version = request.POST.get('version')
        image = request.FILES.get('image')
        creation_date = request.POST.get('creation_date')

        technology = Technology.objects.create(
            name=name,
            description=description,
            version=version,
            image=image,
            creation_date=creation_date
        )
        return redirect('list_technologies')
    return render(request, 'TECHNOLOGY/nuevaTecnologia.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Technology

def save_technology(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        version = request.POST.get('version')
        image = request.FILES.get('image')
        creation_date_str = request.POST.get('creation_date')

        if not name or not description or not version or not creation_date_str:
            messages.error(request, "All fields are required.")
            return render(request, 'TECHNOLOGY/nuevaTecnologia.html', {
                'name': name, 'description': description, 'version': version, 'creation_date': creation_date_str
            })
        try:
            creation_date = datetime.strptime(creation_date_str, '%Y-%m-%d')
            if not (2025 <= creation_date.year <= 2035):
                messages.error(request, "Please enter a valid date between 2025 and 2035.")
                return render(request, 'TECHNOLOGY/nuevaTecnologia.html', {
                    'name': name, 'description': description, 'version': version, 'creation_date': creation_date_str
                })
        except ValueError:
            messages.error(request, "Invalid date format. Please enter a date in YYYY-MM-DD format.")
            return render(request, 'TECHNOLOGY/nuevaTecnologia.html', {
                'name': name, 'description': description, 'version': version, 'creation_date': creation_date_str
            })
        Technology.objects.create(
            name=name,
            description=description,
            version=version,
            image=image,
            creation_date=creation_date
        )

        messages.success(request, "Technology created successfully!")
        return redirect('list_technologies')

    return render(request, 'TECHNOLOGY/nuevaTecnologia.html')


def edit_technology(request, id):
    technology = get_object_or_404(Technology, id=id)

    if request.method == 'POST':
        technology.name = request.POST.get('name')
        technology.description = request.POST.get('description')
        technology.version = request.POST.get('version')
        technology.image = request.FILES.get('image') or technology.image  
        technology.creation_date = request.POST.get('creation_date')

        technology.save()
        return redirect('list_technologies')

    return render(request, 'TECHNOLOGY/editarTecnologia.html', {'technology': technology})

def update_technology(request, id):
    try:
        technology = Technology.objects.get(id=id)
    except Technology.DoesNotExist:
        messages.error(request, "Technology not found.")
        return redirect('list_technologies')

    if request.method == 'POST':
        technology.name = request.POST.get('name')
        technology.description = request.POST.get('description')
        technology.version = request.POST.get('version')
        technology.image = request.FILES.get('image') or technology.image  
        technology.creation_date = request.POST.get('creation_date')

        technology.save()
        messages.success(request, "Technology successfully updated.")
        return redirect('list_technologies')

    return render(request, 'TECHNOLOGY/editarTecnologia.html', {'technology': technology})

def delete_technology(request, id):
    technology = get_object_or_404(Technology, id=id)
    technology.delete()
    messages.success(request, "Technology successfully deleted.")
    return redirect('list_technologies')
