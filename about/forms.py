from .models import CollaborateRequest
from django import forms

class CollaborateForm(forms.ModelForm):
            class Meta:
                model = CollaborateRequest
                fields = ('name', 'email', 'message')


def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()
    collarborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {

            "about": about,
            "collaborate_form": collaborate_form
        },    
    )

    