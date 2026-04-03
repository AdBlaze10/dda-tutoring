from django.shortcuts import render


def home(request):
    context = {
        'google_form_url': 'https://docs.google.com/forms/d/e/1FAIpQLSe4TfMRrkg1tpd_hZDVpVYVD29-SisH-7n_jM2KlTD3PDUK2g/viewform?usp=header',
        'google_embed_url': 'https://docs.google.com/forms/d/e/1FAIpQLSe4TfMRrkg1tpd_hZDVpVYVD29-SisH-7n_jM2KlTD3PDUK2gREPLACE_WITH_YOUR_FORM_ID/viewform?embedded=true',
    }
    return render(request, 'tutoring_site/home.html', context)
