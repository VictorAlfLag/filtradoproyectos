from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import Technology
from .models import Category
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html')

# Listar todas las tecnologías
def list_technologies(request):
    # Agrega los mensajes antes de pasar la lista de tecnologías
    messages.success(request, "Technology list loaded successfully.")
    technologies = Technology.objects.all()
    return render(request, 'TECHNOLOGY/listadoTecnologias.html', {'list_technologies': technologies})

def new_technology(request):
    return render(request, 'TECHNOLOGY/nuevaTecnologia.html')

def save_technology(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.POST.get('name')
        description = request.POST.get('description')
        version = request.POST.get('version')
        image = request.FILES.get('image')
        creation_date_str = request.POST.get('creation_date')

        # Verificar si se está recibiendo la imagen
        if image:
            print(f"Imagen cargada: {image.name}")
        else:
            print("No se ha cargado ninguna imagen.")

        # Validaciones del formulario
        if not name or not description or not version or not creation_date_str:
            messages.error(request, "All fields are required.")
            return render(request, 'TECHNOLOGY/nuevaTecnologia.html', {
                'name': name, 'description': description, 'version': version, 'creation_date': creation_date_str
            })

        try:
            creation_date = datetime.strptime(creation_date_str, '%Y-%m-%dT%H:%M')
            if not (2025 <= creation_date.year <= 2035):
                messages.error(request, "Please enter a valid date between 2025 and 2035.")
                return render(request, 'TECHNOLOGY/nuevaTecnologia.html', {
                    'name': name, 'description': description, 'version': version, 'creation_date': creation_date_str
                })
        except ValueError:
            messages.error(request, "Invalid date format. Please enter a date in YYYY-MM-DDTHH:MM format.")
            return render(request, 'TECHNOLOGY/nuevaTecnologia.html', {
                'name': name, 'description': description, 'version': version, 'creation_date': creation_date_str
            })
        
        # Crear el objeto Technology con la imagen
        technology = Technology.objects.create(
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
    # Eliminar una tecnología
    try:
        technology = Technology.objects.get(id=id)
        technology.delete()
        messages.success(request, "Technology deleted successfully.")
    except Technology.DoesNotExist:
        messages.error(request, "Technology not found.")
    
    return redirect('list_technologies')

# Listar todas las categorías
def list_categories(request):
    messages.success(request, "Category list loaded successfully.")
    categories = Category.objects.all()
    return render(request, 'CATEGORY/listadoCategorias.html', {'list_categories': categories})

# Crear una nueva categoría
def new_category(request):
    return render(request, 'CATEGORY/nuevaCategoria.html')

# Guardar una nueva categoría
def save_category(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        icon = request.FILES.get('icon')
        
        # Validaciones del formulario
        if not name or not description or not status or not icon:
            messages.error(request, "All fields are required.")
            return render(request, 'CATEGORY/nuevaCategoria.html', {
                'name': name, 'description': description, 'status': status
            })

        # Crear el objeto Category con el icono
        category = Category.objects.create(
            name=name,
            description=description,
            status=status,
            icon=icon
        )

        messages.success(request, "Category created successfully!")
        return redirect('list_categories')

    return render(request, 'CATEGORY/nuevaCategoria.html')

# Editar una categoría
def edit_category(request, id):
    category = get_object_or_404(Category, id=id)
    return render(request, 'CATEGORY/editarCategoria.html', {'category': category})

# Actualizar una categoría
def update_category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        messages.error(request, "Category not found.")
        return redirect('list_categories')

    if request.method == 'POST':
        category.name = request.POST.get('name')
        category.description = request.POST.get('description')
        category.status = request.POST.get('status')
        category.icon = request.FILES.get('icon') or category.icon  # Si no se carga un nuevo icono, mantener el actual
        category.save()
        messages.success(request, "Category successfully updated.")
        return redirect('list_categories')

    return render(request, 'CATEGORY/editarCategoria.html', {'category': category})

# Eliminar una categoría
def delete_category(request, id):
    try:
        category = Category.objects.get(id=id)
        category.delete()
        messages.success(request, "Category deleted successfully.")
    except Category.DoesNotExist:
        messages.error(request, "Category not found.")
    
    return redirect('list_categories')
from .models import Tag

# Listar todas las etiquetas
def list_tags(request):
    messages.success(request, "Tag list loaded successfully.")
    tags = Tag.objects.all()
    return render(request, 'TAG/listadoTags.html', {'list_tags': tags})

# Crear una nueva etiqueta
def new_tag(request):
    return render(request, 'TAG/nuevaEtiqueta.html')

# Guardar una nueva etiqueta
def save_tag(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        code = request.POST.get('code')

        # Validaciones del formulario
        if not name or not description or not status:
            messages.error(request, "All fields are required.")
            return render(request, 'TAG/nuevaEtiqueta.html', {
                'name': name, 'description': description, 'status': status, 'code': code
            })

        # Crear el objeto Tag
        tag = Tag.objects.create(
            name=name,
            description=description,
            status=status,
            code=code
        )

        messages.success(request, "Tag created successfully!")
        return redirect('list_tags')

    return render(request, 'TAG/nuevaEtiqueta.html')

# Editar una etiqueta
def edit_tag(request, id):
    tag = get_object_or_404(Tag, id=id)
    return render(request, 'TAG/editarEtiqueta.html', {'tag': tag})

# Actualizar una etiqueta
def update_tag(request, id):
    try:
        tag = Tag.objects.get(id=id)
    except Tag.DoesNotExist:
        messages.error(request, "Tag not found.")
        return redirect('list_tags')

    if request.method == 'POST':
        tag.name = request.POST.get('name')
        tag.description = request.POST.get('description')
        tag.status = request.POST.get('status')
        tag.code = request.POST.get('code') or tag.code  # Si no se especifica un nuevo código, mantener el actual
        tag.save()
        messages.success(request, "Tag successfully updated.")
        return redirect('list_tags')

    return render(request, 'TAG/editarEtiqueta.html', {'tag': tag})

# Eliminar una etiqueta
def delete_tag(request, id):
    try:
        tag = Tag.objects.get(id=id)
        tag.delete()
        messages.success(request, "Tag deleted successfully.")
    except Tag.DoesNotExist:
        messages.error(request, "Tag not found.")
    
    return redirect('list_tags')

from .models import Project

# Listar todos los proyectos
def list_projects(request):
    messages.success(request, "Project list loaded successfully.")
    projects = Project.objects.all()
    return render(request, 'PROJECT/listadoProyectos.html', {'list_projects': projects})

# Crear un nuevo proyecto
def new_project(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    technologies = Technology.objects.all()
    return render(request, 'PROJECT/nuevoProyecto.html', {'categories': categories, 'tags': tags, 'technologies': technologies})

# Guardar un nuevo proyecto
def save_project(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.POST.get('name')
        description = request.POST.get('description')
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
        category_id = request.POST.get('category')
        tags_ids = request.POST.getlist('tags')
        technology_id = request.POST.get('technology')

        # Validaciones del formulario
        if not name or not description or not start_date_str or not end_date_str or not category_id or not technology_id:
            messages.error(request, "All fields are required.")
            return render(request, 'PROJECT/nuevoProyecto.html', {
                'name': name, 'description': description, 'start_date': start_date_str, 'end_date': end_date_str,
                'category_id': category_id, 'tags_ids': tags_ids, 'technology_id': technology_id,
                'categories': Category.objects.all(), 'tags': Tag.objects.all(), 'technologies': Technology.objects.all()
            })

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, "Invalid date format. Please enter dates in YYYY-MM-DD format.")
            return render(request, 'PROJECT/nuevoProyecto.html', {
                'name': name, 'description': description, 'start_date': start_date_str, 'end_date': end_date_str,
                'category_id': category_id, 'tags_ids': tags_ids, 'technology_id': technology_id,
                'categories': Category.objects.all(), 'tags': Tag.objects.all(), 'technologies': Technology.objects.all()
            })

        category = Category.objects.get(id=category_id)
        technology = Technology.objects.get(id=technology_id)
        tags = Tag.objects.filter(id__in=tags_ids)

        # Crear el objeto Project
        project = Project.objects.create(
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            category=category,
            technology=technology
        )

        project.tags.set(tags)  # Asignar las tags al proyecto

        messages.success(request, "Project created successfully!")
        return redirect('list_projects')

    return render(request, 'PROJECT/nuevoProyecto.html')

# Editar un proyecto
def edit_project(request, id):
    project = get_object_or_404(Project, id=id)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    technologies = Technology.objects.all()
    return render(request, 'PROJECT/editarProyecto.html', {'project': project, 'categories': categories, 'tags': tags, 'technologies': technologies})

# Actualizar un proyecto
def update_project(request, id):
    try:
        project = Project.objects.get(id=id)
    except Project.DoesNotExist:
        messages.error(request, "Project not found.")
        return redirect('list_projects')

    if request.method == 'POST':
        project.name = request.POST.get('name')
        project.description = request.POST.get('description')
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
        category_id = request.POST.get('category')
        tags_ids = request.POST.getlist('tags')
        technology_id = request.POST.get('technology')

        # Validaciones del formulario
        if not project.name or not project.description or not start_date_str or not end_date_str or not category_id or not technology_id:
            messages.error(request, "All fields are required.")
            return render(request, 'PROJECT/editarProyecto.html', {
                'project': project, 'categories': Category.objects.all(), 'tags': Tag.objects.all(), 'technologies': Technology.objects.all()
            })

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, "Invalid date format. Please enter dates in YYYY-MM-DD format.")
            return render(request, 'PROJECT/editarProyecto.html', {
                'project': project, 'categories': Category.objects.all(), 'tags': Tag.objects.all(), 'technologies': Technology.objects.all()
            })

        category = Category.objects.get(id=category_id)
        technology = Technology.objects.get(id=technology_id)
        tags = Tag.objects.filter(id__in=tags_ids)

        # Actualizar el proyecto
        project.category = category
        project.technology = technology
        project.start_date = start_date
        project.end_date = end_date
        project.tags.set(tags)  # Asignar las tags actualizadas
        project.save()

        messages.success(request, "Project updated successfully.")
        return redirect('list_projects')

    return render(request, 'PROJECT/editarProyecto.html', {'project': project, 'categories': Category.objects.all(), 'tags': Tag.objects.all(), 'technologies': Technology.objects.all()})

# Eliminar un proyecto
def delete_project(request, id):
    try:
        project = Project.objects.get(id=id)
        project.delete()
        messages.success(request, "Project deleted successfully.")
    except Project.DoesNotExist:
        messages.error(request, "Project not found.")
    
    return redirect('list_projects')
