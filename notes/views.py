from django.shortcuts import render
from django.http import Http404
# Create your views here.
from .models import Notes
from .forms import NotesForm
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'


class NotesUpdateView(UpdateView):
    model = Notes
    # fields = ['title', 'text']
    form_class = NotesForm
    success_url = '/smart/notes'


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    # fields = ['title', 'text']
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = '/admin'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()
# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_details.html'

# def details(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         return render(request, 'notes/notes_error.html', {})
#     return render(request, 'notes/notes_details.html', {'note': note})
