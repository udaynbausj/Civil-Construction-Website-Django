from django.views.generic import TemplateView
from django.shortcuts import render,redirect,HttpResponseRedirect,render_to_response,reverse
from contact.forms import subscribeform,userform
from contact.models import subscribe_model
from django.template import RequestContext
from django.core.mail import send_mail,EmailMultiAlternatives


def contact(request):
        if(request.method=='POST'):
            form = subscribeform(request.POST or None)
            form1 = userform(request.POST or None)
            List = list(subscribe_model.objects.all())
            suvar = []
            for post in List:
                suvar.append(post.Email)
            for i in range(len(suvar)):
                send_mail('Thanks for subscribing', '\nNow,Your dream is our goal.'
                                                    '\nMerci Beaucoup for subscribing'
                          '\n\n\n\n\n\n\n\nRegards Uday BK and Dheeraj Devineni', 'bk.uday2015@vit.ac.in',
                          [suvar[i]], fail_silently=False)
            if(form.is_valid()):
                form.save()
            else:
                form1.save()
        else:
            form = subscribeform()
            form1 = userform()
        return render(request,'contact',{'form':form})