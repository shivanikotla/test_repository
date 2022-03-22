from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import FormView, ListView
from django.contrib import messages
from .forms import UserForm
from .models import Interview
from django.db.models import Q
from .forms import SearchForm

class HomepageView(FormView): # new
    template_name = 'app/home.html'
    form_class = SearchForm # new

class SearchResultsView(ListView):
    model = Interview
    template_name = 'app/search.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Interview.objects.filter(
		      Q(candidate_name__icontains=query) | Q(email__icontains=query)
	    )
        return object_list

#search

# def search(request):
#     if request.method == 'POST':
#         searched = request.POST['searched']
#         s = Interview.objects.filter(candidate_name__contains=searched)

#         return render(request, 'search.html',{'searched':searched},{'s':s})
#     else:
#         return render(request, 'search.html', {})


# Create 
def create(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created')
            return redirect('read')

    context = { 'form':form }
    return render(request, 'app/create.html', context)

# Read
def read(request):

    user_data = Interview.objects.all()
    form_class = SearchForm
    context = { 'user_data': user_data }
    return render(request, 'app/read.html', context)

# Update
def update(request, pk):
    get_user_data = get_object_or_404(Interview, pk=pk)
    form = UserForm(instance=get_user_data)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=get_user_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated')
            return redirect('read')

    context = { 'form':form }
    return render(request, 'app/update.html', context)

# Delete
def delete(request, pk):
    get_user = get_object_or_404(Interview, pk=pk)
    get_user.delete()
    messages.error(request, 'User deleted')
    return redirect('/')

