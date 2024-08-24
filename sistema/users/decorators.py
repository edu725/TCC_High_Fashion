from django.contrib.auth.decorators import user_passes_test

def user_is_manager(function=None):
    decorator = user_passes_test(lambda u: u.is_active and u.user_type == 'manager')
    if function:
        return decorator(function)
    return decorator

def user_is_common(function=None):
    decorator = user_passes_test(lambda u: u.is_active and u.user_type == 'common')
    if function:
        return decorator(function)
    return decorator

def user_is_manager_or_common(function=None):
    def check_user(user):
        return user.is_active and user.user_type in ['manager', 'common']

    decorator = user_passes_test(check_user)

    if function:
        return decorator(function)
    return decorator
