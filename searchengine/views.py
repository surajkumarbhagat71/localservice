from django.shortcuts import render,redirect
from django.views.generic import View , ListView , DetailView ,TemplateView
from django.views.generic.edit import UpdateView
from .forms import *
from .models import *
from django.db.models import *
from django.http import Http404

# Create your views here.

class Home(View):
    def get(self,request,*args,**kwargs):
        context = {"category":Category.objects.all()}

        return render(request,'owner/home.html',context)


class FindWorker(View):
    def get(self,request):

        category = request.GET.get("category")
        city = request.GET.get("city")

        cond = Q(cotegory__title__icontains = category) & Q( city__icontains = city)

        porson = Porson.objects.filter(cond).count()

        if (porson >= 1):
             context = {"porson": Porson.objects.filter(cond)}
             return render(request,'owner/findporson.html', context)
        else:
            return render(request,'owner/react.html')


class DetailPorson(View):
    def get(self,request,pk):

        context = {"porson":Porson.objects.get(porson_id=pk)}

        return render(request,'owner/details_porson.html',context)


#############################  Admin Work ######################

class Login(View):
    def get(self,request):
        form = {"forms":OwnerForm}

        return render(request,'owner/login.html',form)

    def post(self,request):
        username = request.POST.get('email')
        password = request.POST.get('password')

        cond = Q(email = username) & Q(password = password)
        check = Owner.objects.filter(cond).count()

        if (check == 1):
            request.session['login'] = username
            return redirect('dashaboard')
        else:
            return redirect('login')


class AboutUs(TemplateView):
    template_name = 'owner/about.html'


class Dashaboard(View):
    def get(self,request):
        data = {
            "all_worker":Porson.objects.all().count(),
            "all_category":Category.objects.all().count(),
        }
        return render(request,'owner/dashaboard.html',data)


class AddWorker(View):
    def get(self,request):

        data ={"form":PorsonForm()}

        return render(request,'owner/add_worker.html',data)

    def post(self,request,*args,**kwargs):
        form = PorsonForm(request.POST or None , request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect('dashaboard')


class AddCategory(View):
    def get(self,request,*args,**kwargs):
        data = {"form":CategoryForm}

        return render(request,'owner/add_category.html',data)

    def post(self,request,*args,**kwargs):
        form = CategoryForm(request.POST or None )

        if form.is_valid():
            form.save()
            return redirect('dashaboard')


class Logout(View):
    def get(self,request):
        if request.session.has_key('login'):
            del request.session['login']

        return render(request,'owner/login.html')


class All_Workers(View):
    def get(self,request):
        data = {"proson":Porson.objects.all()}

        return render(request,'owner/all_worker.html',data)



class UpdatePorson(UpdateView):
    model = Porson
    form_class = PorsonForm
    template_name = 'owner/add_worker.html'

    def form_valid(self, form):
        form.save()
        return redirect('dashaboard')


class Contact(View):
    def get(self,request):

        data = {"contact":Owner.objects.all()}

        return render(request,'owner/contact.html',data)


class Profile(View):
    def get(self,request):
        data = {"profile":Owner.objects.all()}

        return render(request,'owner/profile.html',data)


class UpdateProfile(UpdateView):
    model = Owner
    form_class = OwnerForm
    template_name = 'owner/updateprofile.html'

    def form_valid(self, form):
        form.save()
        return redirect('dashaboard')



