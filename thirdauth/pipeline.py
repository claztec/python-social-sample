from django.shortcuts import redirect

from social.pipeline.partial import partial
from thirdauth.models import Profile


# @partial
# def require_email(strategy, details, user=None, is_new=False, *args, **kwargs):
#     print("require_email......")
#     if kwargs.get('ajax') or user and user.email:
#         return
#     elif is_new and not details.get('email'):
#         email = strategy.request_data().get('email')
#         if email:
#             details['email'] = email
#         else:
#             return redirect('require_email')


def save_profile(backend, details, response, user, is_new=False, *args, **kwargs):
    if backend.name == 'twitter':
        user_profile = None
        if is_new:
            user_profile = Profile.objects.get_or_create(user=user)
        else:
            user_profile = Profile.objects.get(user=user)

        profile_image_url = response.get('profile_image_url')
        print('profile_image_url : %s' % (profile_image_url))
        user_profile.profile_image_url = profile_image_url
        user_profile.save()

