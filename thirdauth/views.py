from django.shortcuts import render, render_to_response
from django.template import RequestContext
from thirdauth.models import Profile


def home(request):

    if request.user != None:
        user = request.user
        if user.is_active == True:
            # profile = Profile.objects.get(user=user)
            profile = user.profile
            print("image:%s" % (profile.profile_image_url))

    context = RequestContext(request,
                           {'request':request,
                            'user': request.user})
    return render_to_response('thirdauth/home.html',
                             context_instance=context)