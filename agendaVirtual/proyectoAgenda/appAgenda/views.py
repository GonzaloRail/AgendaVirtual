
# views.py
from django.shortcuts import render
import webbrowser, time, pyautogui
from appAgenda.models import Contacto
from .forms import ContactoForm


def enviar_mensaje_whatsapp(request):
    if request.method == 'POST':
        mensaje = request.POST.get('mensaje', '')

        # Obtén los contactos desde la base de datos
        lista_contactos = Contacto.objects.all()

        # Recorre la lista de contactos y envía el mensaje a cada contacto
        for contacto in lista_contactos:
            # Crea la URL directa de WhatsApp para el contacto
            url_whatsapp = f"https://web.whatsapp.com/send?phone=+51{contacto.numero_telefono}"  # Ajusta el prefijo del código de país según tus necesidades

            # Abre la URL directa de WhatsApp en el navegador predeterminado
            webbrowser.open(url_whatsapp)

            # Espera hasta que WhatsApp Web se cargue completamente (ajusta el tiempo según tu conexión)
            time.sleep(10)

            # Escribe y envía el mensaje
            pyautogui.write(mensaje)
            pyautogui.press('enter')
            time.sleep(1)

        # Pasar los contactos y el mensaje al contexto
        context = {
            'contactos': lista_contactos,
            'mensaje': mensaje,
        }

        return render(request, 'enviar_mensaje.html', context)

    return render(request, 'enviar_mensaje.html')


def agregar_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar el nuevo contacto en la base de datos

    else:
        form = ContactoForm()

    return render(request, 'agregar_contacto.html', {'form': form})


