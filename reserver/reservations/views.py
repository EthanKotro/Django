from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm

def reservation_list(request):
    reservations=Reservation.objects.all().order_by('date', 'time')
    context = {'reservations':reservations}
    return render(request, 'reservation_list.html', context)

def create_reservation(request):
    if request.method == "POST": 
        form=ReservationForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect("reservation_list")
        else: 
            print(form.errors)
    else:
        form = ReservationForm()

    context = {'form': form}
    return render(request, 'reservation_form.html', context)
def edit_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)

    context = {'form': form}
    return render(request, 'reservation_form.html', context)

def delete_reservation(request, pk):
    reservation = get_object_or_404(Reservation,pk=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')

    context = {'reservation': reservation}
    return render(request, 'reservation_confirm_delete.html', context)

def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation,pk=pk)
    context = {'reservation': reservation}
    return render(request, 'reservation_detail.html', context)
