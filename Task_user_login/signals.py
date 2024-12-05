from .models import UserModel, Group
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

def send_email(subject, html_message, recipients):

    mail = EmailMultiAlternatives(
        subject, html_message, settings.EMAIL_HOST_USER, recipients
    )
    mail.attach_alternative(html_message, "text/html")
    mail.send(fail_silently=True)
@receiver(post_save, sender = UserModel)
def login_mail(sender, instance, created, **kwargs):
    print("gggggggggggggggggggggg")
    if created:
        if instance.password[0]=='!':
            random_password = uuid.uuid4().hex[:8]
            Candidate, _ = Group.objects.get_or_create(name = 'Candidate')
            instance.set_groups(Candidate)
            instance.set_password(random_password)
            instance.save(update_fields = ['password'])
            subject = "Your Account has been created successfully"
            html_template = get_template("create_user.html")
            email_content = {
                "Employee_name": instance.username.title() if instance.username else instance.email,
                "password": random_password,
            }
            html_message = html_template.render(email_content)

            candidate_email = [instance.email]

            send_email(subject, html_message, candidate_email)
            

