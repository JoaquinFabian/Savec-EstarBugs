from django import forms
from .models import Producto, Cliente, Proveedor, Usuario, Opciones

from django.forms import ModelChoiceField

class MisProductos(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.descripcion

class MisPrecios(ModelChoiceField):
    def label_from_instance(self,obj):
        return "%s" % obj.precio

class MisDisponibles(ModelChoiceField):
    def label_from_instance(self,obj):
        return "%s" % obj.disponible


class LoginFormulario(forms.Form):
    username = forms.CharField(label="Tu nombre de usuario",widget=forms.TextInput(attrs={'placeholder': 'Tu nombre de usuario',
        'class': 'form-control underlined', 'type':'text','id':'user'}))

    password = forms.CharField(label="Contraseña",widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña',
        'class': 'form-control underlined', 'type':'password','id':'password'}))


#-------------------------------------------------------------------------------------------------
    
class ProductoFormulario(forms.ModelForm):
    precio = forms.DecimalField(
        min_value = 1,
        max_value = 99,
        label = 'Precio',
        widget=forms.NumberInput(attrs={'placeholder': 'Precio del producto', 'id': 'precio', 'class': 'form-control', 'pattern': '[0-9]{1,2}', 'title': 'Solo se permiten números y máximo 2 dígitos'}),
        )
    
    disponible = forms.IntegerField(
        min_value = 1,
        max_value = 300,
        label = 'Cantidad',
        widget=forms.NumberInput(attrs={'placeholder': 'Cantidad del producto', 'id': 'disponible', 'class': 'form-control', 'pattern': '[0-9]{1,3}', 'title': 'Solo se permiten números y máximo 3 dígitos'})
        )
    
    class Meta:
        model = Producto
        fields = ['descripcion','precio','disponible','categoria','tiene_iva']
        labels = {
        'descripcion': 'Nombre',
        'tiene_iva': 'Incluye IGV?'
        }
        widgets = {
        'descripcion': forms.TextInput(attrs={'placeholder': 'Nombre del producto', 'id': 'descripcion', 'class': 'form-control', 'pattern': '^[A-Za-záéíóúñÁÉÍÓÚÑ ]{1,30}$', 'title': 'Solo se permiten letras, incluyendo la letra "ñ", las vocales con tilde, y máximo 20 caracteres'}),
        'categoria': forms.Select(attrs={'class':'form-control','id':'categoria'}),
        'tiene_iva': forms.CheckboxInput(attrs={'class':'checkbox rounded','id':'tiene_iva'})
        }


#---------------------------------------------------------------------------------------------

class ClienteFormulario(forms.ModelForm):
    tipoC =  [ ('1','P'),('2','E') ]

    telefono2 = forms.CharField(
        required = False,
        label = 'Segundo numero fijo o celular',
        widget = forms.TextInput(
        attrs={'placeholder': 'Inserte numero fijo o celular alternativo del cliente',
        'id':'telefono2','class': 'form-control', 'placeholder': 'Teléfono fijo o celular del cliente', 'pattern': '^\+?51\s?\d{6,7}$|^\+?51\s?\d{9}$', 'title': 'Debe tener el formato +51 seguido de 6 o 7 dígitos para números fijos o +51 seguido de 9 dígitos para números celulares'}),
        )

    correo2 = forms.CharField(
        required=False,
        label = 'Segundo correo electronico',
        widget = forms.TextInput(
        attrs={'placeholder': 'Inserte el correo alternativo del cliente',
        'id':'correo2', 'maxlength': '30', 'class': 'form-control', 'type': 'email', 'pattern': '[a-zA-Z0-9]+@(gmail\.com|ucsm\.edu\.pe)', 'title': 'Debe ser un correo de Gmail o UCSM válido "example@gmail.com" "example@ucsm.edu.pe"'}),
        )

    tipoCedula = forms.CharField(
        label="Tipo de cedula",
        max_length=2,
        widget=forms.Select(choices=tipoC,attrs={'placeholder': 'Tipo de cedula',
        'id':'tipoCedula','class':'form-control'}
        )
        )


    class Meta:
        model = Cliente
        fields = ['tipoCedula','cedula','nombre','apellido','direccion','nacimiento','telefono','correo','telefono2','correo2']
        labels = {
        'cedula': 'DNI del cliente',
        'nombre': 'Nombre del cliente',
        'apellido': 'Apellido del cliente',
        'direccion': 'Direccion del cliente',
        'nacimiento': 'Fecha de nacimiento del cliente',
        'telefono': 'Numero telefo fijo o celular del cliente',
        'correo': 'Correo electronico del cliente',
        'telefono2': 'Segundo numero telefonico o celular del cliente',
        'correo2': 'Segundo correo electronico'
        }
        widgets = {
        'cedula': forms.TextInput(attrs={'placeholder': 'Inserte DNI del cliente', 'id': 'cedula', 'class': 'form-control', 'pattern': '^\d{8}$', 'title': 'Debe ingresar exactamente 8 números', 'maxlength': '8', 'minlength': '8'}),
        'nombre': forms.TextInput(attrs={'placeholder': 'Inserte solo 1 nombre del cliente', 'id': 'nombre', 'class': 'form-control', 'pattern': '^[A-Za-z]+$', 'title': 'Solo se permiten letras y sin tildes ni ~', 'maxlength': '20'}),
        'apellido': forms.TextInput(attrs={'class': 'form-control', 'id': 'apellido', 'placeholder': 'Ingrese 1 apellido del cliente', 'pattern': '^[A-Za-z]+$', 'title': 'Solo se permiten letras y sin tildes ni ~', 'maxlength': '20'}),
        'direccion': forms.TextInput(attrs={'class': 'form-control', 'id': 'direccion', 'placeholder': 'Direccion del cliente', 'pattern': '^[A-Za-z0-9 ]+$', 'title': 'Solo se permiten letras sin tildes ni ~ y números', 'maxlength': '50'}), 
        'nacimiento': forms.DateInput(format=('%d-%m-%Y'),attrs={'id': 'hasta','class': 'form-control','type': 'date','min': '1940-01-01','max': '2006-12-31'}),
        'telefono':forms.TextInput(attrs={'id':'telefono','class': 'form-control', 'placeholder': 'Teléfono fijo o celular del cliente', 'pattern': '^\+?51\s?\d{6,7}$|^\+?51\s?\d{9}$', 'title': 'Debe tener el formato +51 seguido de 6 o 7 dígitos para números fijos o +51 seguido de 9 dígitos para números celulares'} ),
        'correo':forms.TextInput(attrs={'placeholder': 'Correo del cliente','id':'correo', 'maxlength': '30', 'class': 'form-control', 'type': 'email', 'pattern': '[a-zA-Z0-9]+@(gmail\.com|ucsm\.edu\.pe)', 'title': 'Debe ser un correo de Gmail o UCSM válido "example@gmail.com" "example@ucsm.edu.pe"'})
        }

#------------------------------------------------------------------------------------------------------------------------------



class EmitirFacturaFormulario(forms.Form):
    def __init__(self, *args, **kwargs):
       elecciones = kwargs.pop('cedulas')
       super(EmitirFacturaFormulario, self).__init__(*args, **kwargs)

       if(elecciones):
            self.fields["cliente"] = forms.CharField(label="Cliente a facturar",max_length=50,
            widget=forms.Select(choices=elecciones,
            attrs={'placeholder': 'La cedula del cliente a facturar',
            'id':'cliente','class':'form-control'}))
    
    productos = forms.IntegerField(label="Numero de productos",widget=forms.NumberInput(attrs={'placeholder': 'Numero de productos a facturar',
        'id':'productos','class':'form-control'}))

class DetallesFacturaFormulario(forms.Form):
    productos = Producto.objects.all()

    descripcion = MisProductos(queryset=productos, widget=forms.Select(attrs={'placeholder': 'El producto a debitar', 'class': 'form-control select-group', 'onchange': 'establecerOperaciones(this)'}))

    vista_precio = MisPrecios(required=False, queryset=productos, label="Precio del producto", widget=forms.Select(attrs={'placeholder': 'El precio del producto', 'class': 'form-control', 'disabled': 'true'}))

    cantidad = forms.IntegerField(label="Cantidad a facturar", min_value=1, widget=forms.NumberInput(attrs={'placeholder': 'Introduzca la cantidad del producto', 'class': 'form-control', 'value': '0', 'onchange': 'calculoPrecio(this);calculoDisponible(this)', 'max': '0'}))

    cantidad_disponibles = forms.IntegerField(required=False,label="Stock disponible",min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Introduzca la cantidad del producto','class':'form-control','value':'0', 'max':'0', 'disabled':'true'}))

    selec_disponibles = MisDisponibles(queryset=productos,required=False,widget=forms.Select(attrs={'placeholder': 'El producto a debitar','class':'form-control','disabled':'true','hidden':'true'}))

    subtotal = forms.DecimalField(required=False,label="Sub-total",min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Monto sub-total','class':'form-control','disabled':'true','value':'0'}))

    valor_subtotal = forms.DecimalField(min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Monto sub-total','class':'form-control','hidden':'true','value':'0'}))      


#--------------------------------------------------------------------------------------------


class EmitirPedidoFormulario(forms.Form):
    def __init__(self, *args, **kwargs):
       elecciones = kwargs.pop('cedulas')
       super(EmitirPedidoFormulario, self).__init__(*args, **kwargs)

       if(elecciones):
            self.fields["proveedor"] = forms.CharField(label="Proveedor",max_length=50,
            widget=forms.Select(choices=elecciones,attrs={'placeholder': 'El RUC del proveedor que vende el producto',
            'id':'proveedor','class':'form-control'}))

    productos = forms.IntegerField(label="Numero de productos",widget=forms.NumberInput(attrs={'placeholder': 'Numero de productos a comprar',
        'id':'productos','class':'form-control'}))


class DetallesPedidoFormulario(forms.Form):
    productos = Producto.objects.all()

    descripcion = MisProductos(queryset=productos, widget=forms.Select(attrs={'placeholder': 'El producto a debitar', 'class': 'form-control', 'onchange': 'establecerPrecio(this)'}))

    vista_precio = MisPrecios(required=False,queryset=productos,label="Precio del producto",widget=forms.Select(attrs={'placeholder': 'El precio del producto','class':'form-control','disabled':'true'}))

    cantidad = forms.IntegerField(label="Cantidad", min_value=1, widget=forms.NumberInput(attrs={'placeholder': 'Introduzca la cantidad del producto', 'class': 'form-control', 'value': '0', 'onchange': 'calculoPrecio(this)'}))

    subtotal = forms.DecimalField(required=False,label="Sub-total",min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Monto sub-total','class':'form-control','disabled':'true','value':'0'}))

    valor_subtotal = forms.DecimalField(min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Monto sub-total','class':'form-control','hidden':'true','value':'0'}))      



class ProveedorFormulario(forms.ModelForm):
    tipoC = [('1', 'P'), ('2', 'E')]
    
    tipoCedula = forms.CharField(
        label="Tipo de cedula",
        max_length=2,
        widget=forms.Select(choices=tipoC, attrs={'placeholder': 'Tipo de cedula', 'id': 'tipoCedula', 'class': 'form-control'})
    )

    telefono2 = forms.CharField(
        required=False,
        label='Segundo numero telefonico( Opcional )',
        max_length=9,
        widget=forms.TextInput(attrs={'placeholder': 'Inserte el telefono alternativo del proveedor', 'id': 'telefono2', 'class': 'form-control', 'placeholder': 'Teléfono del proveedor', 'pattern': '^\+?51\s?\d{6,7}$|^\+?51\s?\d{9}$', 'title': 'Debe tener el formato +51 seguido de 6 o 7 dígitos para números fijos o +51 seguido de 9 dígitos para números celulares'}),
    )

    correo2 = forms.CharField(
        required=False,
        max_length=30,
        label='Segundo correo electronico( Opcional )',
        widget=forms.TextInput(attrs={'placeholder': 'Inserte el correo alternativo del proveedor', 
                                      'id': 'correo2',  'maxlength': '30', 'class': 'form-control', 'type': 'email', 'pattern': '[a-zA-Z0-9]+@(gmail\.com|ucsm\.edu\.pe)', 'title': 'Debe ser un correo de Gmail o UCSM válido "example@gmail.com" "example@ucsm.edu.pe"'}),
    )

    class Meta:
        model = Cliente
        fields = ['tipoCedula', 'cedula', 'nombre', 'apellido', 'direccion', 'nacimiento', 'telefono', 'correo']
        labels = {
            'cedula': 'RUC del proveedor',
            'nombre': 'Nombre del proveedor',
            'apellido': 'Apellido del proveedor',
            'direccion': 'Direccion del proveedor',
            'nacimiento': 'Fecha de nacimiento del proveedor o inscripcion de la empresa',
            'telefono': 'Numero fijo o celular del proveedor',
            'correo': 'Correo electronico del proveedor',
        }
        widgets = {
            'cedula': forms.TextInput(attrs={'placeholder': 'Inserte el RUC del proveedor', 'id': 'cedula', 'class': 'form-control', 'pattern': '(10|20)[0-9]{9}', 'title': 'Debe ingresar exactamente 11 números comenzando con 10 o 20'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Inserte el primer nombre del proveedor', 'id': 'nombre', 'class': 'form-control', 'pattern': '[A-Za-z ]{1,30}', 'title': 'Solo se permiten letras sin tildes ni ~ y máximo 30 caracteres'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'El apellido del proveedor', 'class': 'form-control', 'id': 'apellido', 'pattern': '[A-Za-z ]{1,30}', 'title': 'Solo se permiten letras sin tildes ni ~ y máximo 30 caracteres'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'id': 'direccion', 'placeholder': 'Direccion del proveedor', 'pattern': '[A-Za-z0-9 ]*','maxlength': '50', 'title': 'Solo se permiten letras y números'}),
            'nacimiento': forms.DateInput(format=('%d-%m-%Y'),attrs={'id': 'hasta','class': 'form-control','type': 'date','min': '1900-01-01','max': '2006-12-31'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono', 'class': 'form-control', 'placeholder': 'Teléfono fijo o celular del proveedor', 'pattern': '^\+?51\s?\d{6,7}$|^\+?51\s?\d{9}$', 'title': 'Debe tener el formato +51 seguido de 6 o 7 dígitos para números fijos o +51 seguido de 9 dígitos para números celulares'}),
            'correo': forms.TextInput(attrs={'placeholder': 'Correo del proveedor', 'id': 'correo', 'maxlength': '30', 'class': 'form-control', 'type': 'email', 'pattern': '[a-zA-Z0-9]+@(gmail\.com|ucsm\.edu\.pe)', 'title': 'Debe ser un correo de Gmail o UCSM válido "example@gmail.com" "example@ucsm.edu.pe"'}),
        }

class UsuarioFormulario(forms.Form):
    niveles =  [ ('1','Administrador'),('0','Usuario') ]

    username = forms.CharField(
        label="Nombre de usuario",
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Inserte un nombre de usuario',
                                      'id': 'username', 'class': 'form-control', 'pattern': '[A-Za-z0-9]{1,12}', 'title': 'Solo se permiten letras y números y máximo 12 caracteres'}),
    )

    first_name = forms.CharField(
        label='Nombre',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Inserte un nombre',
                                      'id': 'first_name', 'class': 'form-control', 'pattern': '[A-Za-z]+', 'title': 'Solo se permiten letras sin tildes ni ~'}),
    )

    last_name = forms.CharField(
        label='Apellido',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Inserte un apellido',
                                      'id': 'last_name', 'class': 'form-control', 'pattern': '[A-Za-z]+', 'title': 'Solo se permiten letras sin tildes ni ~'}),
    )

    email = forms.CharField(
        label='Correo electronico',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Inserte un correo valido',
                                      'id': 'email', 'class': 'form-control', 'type': 'email', 'pattern': '[a-zA-Z0-9]+@(gmail\.com|ucsm\.edu\.pe)', 'title': 'Debe ser un correo de Gmail o UCSM válido "example@gmail.com" "example@ucsm.edu.pe"'})
    )

    level =  forms.CharField(
        required=False,
        label="Nivel de acceso",
        max_length=2,
        widget=forms.Select(choices=niveles,attrs={'placeholder': 'El nivel de acceso',
        'id':'level','class':'form-control','value':''}
        )
        )
    
class NuevoUsuarioFormulario(forms.Form):
    niveles =  [ ('1','Administrador'),('0','Usuario') ]

    username = forms.CharField(
        label="Nombre de usuario",
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Inserte un nombre de usuario', 'id': 'username', 'class': 'form-control', 'pattern': '[A-Za-z0-9]{1,12}', 'title': 'Solo se permiten letras y números y máximo 12 caracteres'})
    )

    first_name = forms.CharField(
        label='Nombre',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Inserte un nombre',
                                      'id': 'first_name', 'class': 'form-control', 'pattern': '[A-Za-z]+', 'title': 'Solo se permiten letras sin tildes ni ~'}),
    )

    last_name = forms.CharField(
        label='Apellido',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Inserte un apellido',
                                      'id': 'last_name', 'class': 'form-control', 'pattern': '[A-Za-z]+', 'title': 'Solo se permiten letras sin tildes ni ~'}),
    )

    email = forms.CharField(
        label='Correo electronico',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Inserte un correo valido', 'id': 'email',  'maxlength': '30', 'class': 'form-control', 'type': 'email', 'pattern': '[a-zA-Z0-9]+@(gmail\.com|ucsm\.edu\.pe)', 'title': 'Debe ser un correo de Gmail o UCSM válido "example@gmail.com" "example@ucsm.edu.pe"'})
    )

    password = forms.CharField(
        label='Clave',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Inserte una clave',
                                      'id': 'password', 'class': 'form-control', 'type': 'password', 'value': ''})
    )

    rep_password = forms.CharField(
        label='Repetir clave',
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Repita la clave de arriba',
                                      'id': 'rep_password', 'class': 'form-control', 'type': 'password', 'value': ''})
    )

    level = forms.CharField(
        label="Nivel de acceso",
        max_length=2,
        widget=forms.Select(choices=niveles, attrs={'placeholder': 'El nivel de acceso',
                                                     'id': 'level', 'class': 'form-control', 'value': ''})
    )


class ClaveFormulario(forms.Form):
    #clave = forms.CharField(
        #label = 'Ingrese su clave actual',
        #max_length=50,
        #widget = forms.TextInput(
        #attrs={'placeholder': 'Inserte la clave actual para verificar su identidad',
        #'id':'clave','class':'form-control', 'type': 'password'}),
        #)

    clave_nueva = forms.CharField(
        label = 'Ingrese la clave nueva',
        max_length=30,
        widget = forms.TextInput(
        attrs={'placeholder': 'Inserte la clave nueva de acceso',
        'id':'clave_nueva','class':'form-control', 'type': 'password'}),
        )

    repetir_clave = forms.CharField(
        label="Repita la clave nueva",
        max_length=30,
        widget = forms.TextInput(
        attrs={'placeholder': 'Vuelva a insertar la clave nueva',
        'id':'repetir_clave','class':'form-control', 'type': 'password'}),
        )


