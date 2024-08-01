from django.shortcuts import render


from cms.models import News
# Create your views here.



def index(request):
    data = {}
    
    data['news'] = News.objects.filter(is_deleted=False).order_by('datetime_update')
    
    
    return render(request, 'cms_main.html', data)

def newsDetail(request, pk):
    data = {}
    
    data['news'] = News.objects.filter(pk=pk, is_deleted=False).order_by('datetime_update')
    
    
    return render(request, 'cms_details.html', data)