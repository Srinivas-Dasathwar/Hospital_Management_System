from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment
from accounts.models import Doctor, Patient
from .forms import AppointmentForm, UpdateAppointmentForm

@login_required
def dashboard(request):
    user = request.user
    context = {}
    
    if hasattr(user, 'patient'):
        context['role'] = 'Patient'
        context['appointments'] = Appointment.objects.filter(patient=user.patient).order_by('-date', '-time')[:5]
    elif hasattr(user, 'doctor'):
        context['role'] = 'Doctor'
        context['appointments'] = Appointment.objects.filter(doctor=user.doctor).order_by('-date', '-time')[:5]
    elif user.is_superuser:
        context['role'] = 'Admin'
        context['total_patients'] = Patient.objects.count()
        context['total_doctors'] = Doctor.objects.count()
        context['total_appointments'] = Appointment.objects.count()
    
    return render(request, 'hospital/dashboard.html', context)

@login_required
def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospital/doctors_list.html', {'doctors': doctors})

@login_required
def book_appointment(request):
    if not hasattr(request.user, 'patient'):
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.patient
            appointment.save()
            return redirect('appointments_list')
    else:
        form = AppointmentForm()
    
    return render(request, 'hospital/book_appointment.html', {'form': form})

@login_required
def appointments_list(request):
    user = request.user
    if hasattr(user, 'patient'):
        appointments = Appointment.objects.filter(patient=user.patient).order_by('-date', '-time')
    elif hasattr(user, 'doctor'):
        appointments = Appointment.objects.filter(doctor=user.doctor).order_by('-date', '-time')
    elif user.is_superuser:
        appointments = Appointment.objects.all().order_by('-date', '-time')
    else:
        appointments = []
        
    return render(request, 'hospital/appointments_list.html', {'appointments': appointments})

@login_required
def update_appointment(request, pk):
    if not hasattr(request.user, 'doctor'):
        return redirect('dashboard')
        
    appointment = get_object_or_404(Appointment, pk=pk, doctor=request.user.doctor)
    
    if request.method == 'POST':
        form = UpdateAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments_list')
    else:
        form = UpdateAppointmentForm(instance=appointment)
        
    return render(request, 'hospital/update_appointment.html', {'form': form, 'appointment': appointment})
