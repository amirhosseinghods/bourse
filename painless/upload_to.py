def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

def product_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/product_<id>/<filename>
    return 'product_{0}/{1}'.format(instance.title, filename)

def product_movie_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/product_<id>/<filename>
    return 'product_movie/{0}/{1}'.format(instance.title, filename)

def tutorial_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/tutorial_<id>/<filename>
    return 'tutorial_{0}/{1}'.format(instance.title, filename)

def tutorial_movie_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/tutorial_<id>/<filename>
    return 'tutorial_movie/{0}/{1}'.format(instance.title, filename)