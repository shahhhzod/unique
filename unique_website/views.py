def set_language(request):
    if 'language' in request.GET:
        language = request.GET['language']
        activate(language)
        next_url = request.GET.get('next', '/')
        return redirect(next_url)
    return redirect('/')