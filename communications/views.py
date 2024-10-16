from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Profile
from .models import Message
from investors.models import WatchList
from django.contrib import messages

@login_required(login_url='login')
def sendMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    if request.method == 'POST':
        if request.POST['subject'] and request.POST['message']:
            sender = request.user.profile
            email = sender.email
            name = sender.first_name
            message = Message.objects.create(
                subject = request.POST['subject'],
                body = request.POST['message'],
                sender = sender,
                recipient = recipient,
                email=email,
                name=name
            )
            message.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('global-pitches')
        else:
            messages.error('Please complete the subject and message!')
    
    return render(request, 'communications/send-message.html', {'recipient': recipient})

@login_required(login_url='login')
def inbox(request):
    comms = Message.objects.filter(recipient=request.user.profile)
    unreadCount = len(Message.objects.filter(is_read=False, recipient=request.user.profile))
    context = {'comms': comms, 'unreadCount': unreadCount}
    return render(request, 'communications/inbox.html', context)

@login_required(login_url='login')
def message(request, pk):
    message = Message.objects.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    return render(request, 'communications/message.html', {'message': message})