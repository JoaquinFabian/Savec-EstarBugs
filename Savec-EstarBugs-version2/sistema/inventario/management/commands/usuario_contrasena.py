from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from inventario.models import Usuario

class Command(BaseCommand):
    help = 'Crea un usuario en la base de datos con una contraseña hasheada'

    def handle(self, *args, **kwargs):
        datos_usuario = {
            'last_login': '2024-05-05 00:00:00',
            'is_superuser': 0,
            'is_staff': 0,
            'is_active': 1,
            'date_joined': '2024-05-05 00:00:00',
            'username': 'joaquinFabian',
            'email': 'joaquin.ponze@ucsm.edu.pe',
            'first_name': 'Joaquin',
            'last_name': 'Ponze',
            'nivel': 1
        }

        datos_usuario['password'] = make_password('Gringo1234567')

        usuario = Usuario.objects.create(**datos_usuario)

        self.stdout.write(self.style.SUCCESS(f'Usuario creado correctamente: {usuario.username}'))
