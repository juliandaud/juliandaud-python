from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib import messages
from .models import Message
from .forms import MessageForm


class InboxView(ListView):
    model = Message
    template_name = "mensajes/inbox.html"
    context_object_name = "messages"

    def get_queryset(self):
        return Message.objects.filter(sender__isnull=False).order_by('-timestamp')


@login_required
def enviar_mensaje(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, "Mensaje enviado, ¡muchas gracias!")
            return redirect('mensajes:inbox')
    else:
        form = MessageForm()
    return render(request, 'mensajes/enviar_mensaje.html', {'form': form})


def dejar_mensaje(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            if request.user.is_authenticated:
                message.sender = request.user
            message.save()
            messages.success(request, "Mensaje enviado, ¡muchas gracias!")
            return redirect('tienda:nosotros')
    else:
        form = MessageForm()
    return render(request, 'mensajes/dejar_mensaje.html', {'form': form})
