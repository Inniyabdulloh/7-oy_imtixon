from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .models import Xodimlar, Davomat
# Create your views here.



class DashboardView(View):
    def get(self, request):
        xodimlar = Xodimlar.objects.all()
        return render(request, 'index.html', {'xodimlar': xodimlar})


class AttendanceCreate(View):
    def post(self, request):
        id = request.POST.get('xodim')
        xodim = Xodimlar.objects.get(id=id)
        Davomat.objects.create(xodim=xodim)
        return redirect('dashboard:dashboard')


class AttendanceListView(View):
    def get(self, request):
        davomat = Davomat.objects.all()
        return render(request, 'staff/attendance-list.html',{'davomat': davomat})


class LoginView(View):
    def get(self, request):
        return render(request, 'profile/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            return redirect('dashboard:dashboard')

        return render(request, 'profile/login.html')


class ProfileEditView(View, LoginRequiredMixin):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        return render(request, 'profile/staff-profile.html', {'user': user})

    def post(self, request):
        user = User.objects.get(id=request.user.id)


        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        user.save()

        return redirect('dashboard:staff_profile')


class StaffCreateView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'staff/staff-create.html')

    def post(self, request):
        Xodimlar.objects.create(
            full_name=request.POST['full_name'],
            age=request.POST['age'],
            phone=request.POST['phone'],
            position=request.POST['position'],
            photo=request.FILES['photo'],
        )

        return redirect('dashboard:dashboard')


class StaffDetailView(View):
    def get(self, request, id):
        xodim = Xodimlar.objects.get(id=id)
        return render(request, 'staff/staff-detail.html', {'xodim': xodim})


class StaffListView(View):
    def get(self, request):
        xodimlar = Xodimlar.objects.all()
        return render(request, 'staff/staff-list.html', {'xodimlar': xodimlar})


class StaffUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        xodim = Xodimlar.objects.get(id=id)
        return render(request, 'staff/staff-update.html', {'xodim': xodim})

    def post(self, request, id):
        xodim = Xodimlar.objects.get(id=id)
        xodim.full_name = request.POST['full_name']
        xodim.age = request.POST['age']
        xodim.phone = request.POST['phone']
        xodim.position = request.POST['position']
        photo = request.FILES.get('photo')
        xodim.is_active = bool(request.POST.get('is_active'))
        if photo:
            xodim.photo = photo

        xodim.save()
        messages.success(request, 'Your Staff Details has been updated.')
        return redirect('dashboard:dashboard')





class StaffDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        Xodimlar.objects.get(id=id).delete()
        messages.success(request, 'Your Staff Details has been deleted.')
        return redirect('dashboard:dashboard')
