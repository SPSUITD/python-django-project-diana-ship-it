from django_messages.models import inbox_count_for


def _user_is_authenticated(user):
    try:
        return user.is_authenticated()
    except TypeError:
        return user.is_authenticated


def inbox(request):
    if _user_is_authenticated(request.user):
        return {'messages_inbox_count': inbox_count_for(request.user)}
    else:
        return {}
