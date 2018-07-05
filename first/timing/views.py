from django.shortcuts import render, redirect, reverse

from timing.models import Meeting


# Create your views here.
def list(request):
    meetings = Meeting.objects.all()
    return render(request, 'timing/list.html', context={'meetings': meetings})


def save(request):
    meeting = Meeting()
    meeting.save_me(request)
    return redirect(reverse('timing:list'))
