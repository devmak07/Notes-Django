from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
from django.db.models import Q
from django.contrib import messages

# Create your views here.
# def index(request):
#     return render(request,'index.html')

# core/views.py (modified)
def create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:view')  # Correct redirection to the named URL pattern 'view'
    else:
        form = NoteForm()
    
    return render(request, 'index.html', {'form': form})

# def unlock_note(request,pk):
#     note=get_object_or_404(Note,pk=pk)

#     if request.method=="POST":
#         password=request.POST.get('password')
#         if note.password==password:
#             note.locked=False
#             note.save()
#             messages.success(request,"your note is unlockes")
#             return redirect('core:view')
#         else:
#             messages.error(request,"incorrect password,try again")
#     return render(request,'unlock_note.html',{'note':note})

def unlock_note(request, pk):
    note = Note.objects.get(pk=pk)
    flag="False"
    if request.method == 'POST':
        password = request.POST.get('password')
        print(password)
        if password == note.password:  
            flag="True"
            print(flag)# Assuming the Note model has a `password` field
            # return redirect("/view/")
            # return render(request, 'note_list.html', {'note': note})
        else:
            flag="False"
            print(flag)
            return render(request, 'unlock_note.html', {
                'error': 'Incorrect password', 
                'pk': pk, # Ensure the pk is passed to the template
            })
    return render(request, 'unlock_note.html', {'pk': pk,"flag":flag,"note":note})


    
def view(request):
    query=request.GET.get('q')
    if query:   
        notes=Note.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        notes=Note.objects.all()
    return render(request,'note_list.html',{'notes':notes,'query':query})

def update(request,pk):
    form_instance=get_object_or_404(Note,pk=pk)
    if request.method=='POST':
        form=NoteForm(request.POST,instance=form_instance)
        if form.is_valid():
            form.save()
            return redirect('core:view')
    else:
        form=NoteForm(instance=form_instance)
    return render(request,'index.html',{'form':form})

def delete(request,pk):
    form_instance=get_object_or_404(Note,pk=pk)
    form_instance.delete()
    return redirect('core:view')

