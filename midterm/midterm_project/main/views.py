from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Instructor, Member, Gym, Membership, Equipment, Workout
from .forms import InstructorForm, MemberForm, GymForm, MembershipForm, EquipmentForm, WorkoutForm, InstructorFilterForm, GymFilterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .serializers import GymSerializer,WorkoutSerializer,InstructorSerializer, MemberSerializer,MembershipSerializer

# Create your views here.

# Rendered views
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

@login_required
def add_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instructorpage')
    else:
        form = InstructorForm()
    return render(request, 'main/add_instructor.html', {'form': form})

@login_required
def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('memberpage')
    else:
        form = MemberForm()
    return render(request, 'main/add_member.html', {'form': form})

@login_required
def add_gym(request):
    if request.method == 'POST':
        form = GymForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gympage')
    else:
        form = GymForm()
    return render(request, 'main/add_gym.html', {'form': form})

@login_required
def add_membership(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('membershippage')
    else:
        form = MembershipForm()
    return render(request, 'main/add_membership.html', {'form': form})

@login_required
def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipmentpage')
    else:
        form = EquipmentForm()
    return render(request, 'main/add_equipment.html', {'form': form})

@login_required
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workoutpage')
    else:
        form = WorkoutForm()
    return render(request, 'main/add_workout.html', {'form': form})

# API views
@api_view(['GET', 'POST'])
def instructor_list(request):
    if request.method == 'GET':
        instructors = Instructor.objects.all()
        serializer = InstructorSerializer(instructors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = InstructorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def member_list(request):
    if request.method == 'GET':
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def gym_list(request):
    if request.method == 'GET':
        gyms = Gym.objects.all()
        serializer = GymSerializer(gyms, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GymSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def membership_list(request):
    if request.method == 'GET':
        memberships = Membership.objects.all()
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def equipment_list(request):
    if request.method == 'GET':
        equipment = Equipment.objects.all()
        serializer = EquipmentSerializer(equipment, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def workout_list(request):
    if request.method == 'GET':
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WorkoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def filter_instructors(request):
    if request.method == 'GET':
        form = InstructorFilterForm(request.GET)
        if form.is_valid():
            specialization = form.cleaned_data.get('specialization')
            gender = form.cleaned_data.get('gender')
            instructors = Instructor.objects.all()
            if specialization:
                instructors = instructors.filter(specialization=specialization)
            if gender:
                instructors = instructors.filter(gender=gender)

            # Фильтрация по букве "А"
            instructors = instructors.filter(instructor_name__istartswith='A')

            return render(request, 'main/instructor_list.html', {'instructors': instructors, 'form': form})
    else:
        form = InstructorFilterForm()
    return render(request, 'main/filter_instructors.html', {'form': form})


def filter_gyms(request):
    if request.method == 'GET':
        form = GymFilterForm(request.GET)
        if form.is_valid():
            location = form.cleaned_data.get('location')
            gyms = Gym.objects.all()
            if location:
                gyms = gyms.filter(location=location)
            return render(request, 'main/gym_list.html', {'gyms': gyms, 'form': form})
    else:
        form = GymFilterForm()
    return render(request, 'main/filter_gyms.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('mainpage')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

@login_required
def custom_logout(request):
    logout(request)
    return redirect('')


def get_members(request):
    members = Member.objects.all()
    data = [{'member_id': member.member_id, 'name': member.name,
             'age': member.age, 'membership_type': member.membership_type} for member in members]
    return JsonResponse(data, safe=False)

def get_gyms(request):
    gyms = Gym.objects.all()
    data = [{'gym_id': gym.gym_id, 'gym_name': gym.gym_name,
             'location': gym.location} for gym in gyms]
    return JsonResponse(data, safe=False)

def get_memberships(request):
    memberships = Membership.objects.all()
    data = [{'membership_id': membership.membership_id, 'name': membership.name,
             'price': membership.price} for membership in memberships]
    return JsonResponse(data, safe=False)

def get_equipment(request):
    equipment = Equipment.objects.all()
    data = [{'equipment_id': item.equipment_id, 'name': item.name,
             'quantity': item.quantity} for item in equipment]
    return JsonResponse(data, safe=False)

def get_workouts(request):
    workouts = Workout.objects.all()
    data = [{'workout_id': workout.workout_id, 'name': workout.name,
             'description': workout.description} for workout in workouts]
    return JsonResponse(data, safe=False)


def show_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, pk=instructor_id)
    data = {
        'instructor_id': instructor.instructor_id,
        'instructor_name': instructor.instructor_name,
        'specialization': instructor.specialization,
        'gender': instructor.gender
    }
    return JsonResponse(data)

def delete_instructor(request, instructor_id):
    instructor = Instructor.objects.filter(pk=instructor_id)
    if instructor.exists():
        instructor.delete()
        return JsonResponse({'message': 'Instructor deleted successfully'})
    else:
        return JsonResponse({'message': 'Instructor not found'}, status=404)

