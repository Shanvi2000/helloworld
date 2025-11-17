from django.http import HttpResponse
from django.template import loader
from .forms import EmployeeForm

def members(request):
  if request.method == 'POST':
    form = EmployeeForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponse("Employee added successfully!")
  else:
    form = EmployeeForm()
  
  template = loader.get_template('myfirst.html')
  context = {'form': form}
  return HttpResponse(template.render(context, request))
