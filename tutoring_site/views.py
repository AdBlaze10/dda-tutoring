from django.shortcuts import render


def home(request):
    context = {
        'google_form_url': 'https://docs.google.com/forms/d/e/1FAIpQLSe4TfMRrkg1tpd_hZDVpVYVD29-SisH-7n_jM2KlTD3PDUK2g/viewform?usp=header',
        'google_embed_url': '<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSe4TfMRrkg1tpd_hZDVpVYVD29-SisH-7n_jM2KlTD3PDUK2g/viewform?embedded=true" width="640" height="1705" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>',
    }
    return render(request, 'tutoring_site/home.html', context)
