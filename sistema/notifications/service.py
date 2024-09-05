from django.core.mail import EmailMessage 
from django.conf import settings
from django.template.loader import render_to_string

class EmailService:
    @staticmethod
    def send_text_email(subject, message, recipient_list, from_email=None):
        """
        Envia um email de texto simples.
        """
        if from_email is None:
            from_email = settings.DEFAULT_FROM_EMAIL

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=recipient_list,
        )

        email.send()

    @staticmethod
    def send_html_email(subject, html_content, recipient_list, from_email=None):
        """
        Envia um email com corpo HTML.
        """
        if from_email is None:
            from_email = settings.DEFAULT_FROM_EMAIL

        email = EmailMessage(
            subject=subject,
            body=html_content,
            from_email=from_email,
            to=recipient_list,
        )
        email.content_subtype = "html"  # Define o conteúdo como HTML

        email.send()

    @staticmethod
    def send_email_with_attachment(subject, message, recipient_list, attachment_path, from_email=None, html_message=None):
        """
        Envia um email com anexo, opcionalmente pode incluir corpo HTML.
        """
        if from_email is None:
            from_email = settings.DEFAULT_FROM_EMAIL

        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=recipient_list,
        )

        if html_message:
            email.content_subtype = "html"  # Define o conteúdo como HTML
            email.body = html_message

        email.attach_file(attachment_path)  # Anexa o arquivo

        email.send()

     
    @staticmethod
    def send_html_email_with_template(subject, template_name, context, recipient_list, from_email=None):
        """
        Envia um email com corpo HTML renderizado a partir de um template.
        """
        if from_email is None:
            from_email = settings.DEFAULT_FROM_EMAIL

        html_content = render_to_string(template_name, context)
        
        email = EmailMessage(
            subject=subject,
            body=html_content,
            from_email=from_email,
            to=recipient_list,
        )
        email.content_subtype = "html"  # Define o conteúdo como HTML

        email.send()
