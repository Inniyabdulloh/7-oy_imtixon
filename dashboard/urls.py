from django.urls import path
from .views import ( DashboardView, AttendanceCreate, AttendanceListView,
              StaffCreateView, StaffListView, StaffUpdateView, StaffDeleteView,
              StaffDetailView, ProfileEditView, LoginView
                     )

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('login/', LoginView.as_view(), name='staff_login'),
    path('attendance/', AttendanceCreate.as_view(), name='attendance'),
    path('attendance/list/', AttendanceListView.as_view(), name='attendance_list'),
    path('staff/create/', StaffCreateView.as_view(), name='staff_create'),
    path('staff/list/', StaffListView.as_view(), name='staff_list'),
    path('staff/update/<int:id>/', StaffUpdateView.as_view(), name='staff_update'),
    path('staff/delete/<int:id>/', StaffDeleteView.as_view(), name='staff_delete'),
    path('staff/detail/<int:id>/', StaffDetailView.as_view(), name='staff_detail'),
    path('staff/profile/', ProfileEditView.as_view(), name='staff_profile'),



]