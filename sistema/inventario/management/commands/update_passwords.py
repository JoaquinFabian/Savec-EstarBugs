# en un archivo como update_passwords.py en tu app
from django.core.management.base import BaseCommand
from inventario.models import Usuario

class Command(BaseCommand):
    help = 'Actualiza las contraseñas de los usuarios para utilizar el nuevo algoritmo de hash de contraseñas'

    def handle(self, *args, **kwargs):
        # Obtener todos los usuarios utilizando el administrador de modelos personalizado
        users = Usuario.objects.all()

        # Iterar sobre los usuarios y actualizar sus contraseñas
        for user in users:
            # Actualizar la contraseña del usuario utilizando el método set_password
            user.set_password(user.password)
            # Guardar el usuario para aplicar los cambios
            user.save()

        self.stdout.write(self.style.SUCCESS('Las contraseñas de los usuarios han sido actualizadas correctamente.'))
