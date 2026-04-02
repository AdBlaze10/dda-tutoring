from django.shortcuts import render


def home(request):
    context = {
        'google_form_url': 'https://forms.gle/REPLACE_WITH_YOUR_FORM_ID',
        'google_embed_url': 'https://docs.google.com/forms/d/e/REPLACE_WITH_YOUR_FORM_ID/viewform?embedded=true',
    }
    return render(request, 'tutoring_site/home.html', context)
