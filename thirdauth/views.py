from django.shortcuts import render, render_to_response
from django.template import RequestContext


def home(request):

    user = request.user
    print("email:%s" % (user.email))
    print("name:%s" % (user.get_full_name()))

    context = RequestContext(request,
                           {'request':request,
                            'user': request.user})
    return render_to_response('thirdauth/home.html',
                             context_instance=context)