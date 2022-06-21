from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    context = {
        'counter': request.session['count']
    }
        
    return render(request,'index.html',context)