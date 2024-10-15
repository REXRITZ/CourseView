from django.db.models import Q
from django.shortcuts import render
from .models import Material, Course

def material_list(request):
    query = request.GET.get('q')
    if query:
        materials = Material.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        materials = Material.objects.all()
    
    return render(request, 'repository/material_list.html', {'materials': materials})

def course_materials(request, course_id):
    course = Course.objects.get(id=course_id)
    materials = Material.objects.filter(course=course)
    return render(request, 'repository/course_materials.html', {'materials': materials, 'course': course})