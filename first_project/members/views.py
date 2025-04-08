from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Member

# Create your views here.
def members(request):
  mymembers = Member.objects.all().values()

  template = loader.get_template('all_members.html')
  context = {
    'members': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, member_id):
  mymember = Member.objects.get(id=member_id)
  template = loader.get_template('details.html')
  context = {
    'member': mymember,
  }
  return HttpResponse(template.render(context, request))

def api(request):
  mymembers = Member.objects.all().values()
  return JsonResponse({
    'members': list(mymembers)
  }, content_type='application/json')