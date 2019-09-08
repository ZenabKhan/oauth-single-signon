def update_photo_url(backend, strategy, details, response,
              user=None, *args, **kwargs):
    if backend.name == 'google-oauth2':
        url = response['picture']
        user.photo_url = url
        user.save()
