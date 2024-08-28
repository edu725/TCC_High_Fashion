from django.shortcuts import render
from notifications.service import EmailService
from produto.service import ProductService

# Create your views here.

produto = ProductService.get_last_product()

EmailService.send_email_with_attachment(
    subject="Novo produto adicionado",
    message=f"Confira as Novidades do nosso site como o novo lançamento da/o {produto.name}",
    recipient_list=EmailService.list_all_email_users,
    attachment_path=produto.path,
)