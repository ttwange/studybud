from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_function(request, *args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return  wrapper_function

def allowed_users(allowed_roles=[]):
    def decorators(view_func):
      def wrapper_func(request, *args, **kwargs):
          print("Working")
          return view_func(request, *args, **kwargs):
      return wrapper_func
    return decorators