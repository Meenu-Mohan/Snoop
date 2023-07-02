from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.shortcuts import render, redirect

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(request, "You don't have admin privileges!")
            return redirect('users:profile')
        return view_func(request, *args, **kwargs)
    return wrapper