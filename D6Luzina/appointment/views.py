from django.shortcuts import render, reverse, redirect
from django.views import View
from datetime import datetime
from django.core.mail import EmailMultiAlternatives, mail_admins, mail_managers
from django.template.loader import render_to_string


from .models import Appointment


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], '%Y-%m-%d'),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        html_content = render_to_string(
            'appointment_created.html',
            {
                'appointment': appointment,
            }
        )

        msg = EmailMultiAlternatives(
            subject=f'{appointment.client_name} {appointment.date.strftime("%Y-%M-%d")}',
            body=appointment.message,
            from_email='cobac11@yandex.ru',
            to=['cobac11@yandex.ru'],  # это то же, что и recipients_list
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()

        return redirect('appointments:make_appointment')
