# Python's Libraries
import secrets

# Django's Libraries
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Third-party Libraries
from simple_history.models import HistoricalRecords

# Own's Libraries
from Utils.models import AppModel
from Utils.models import KeyCharField
# from Utils.models import NameCharField
from Utils.models import DescriptionCharField
from Utils.managers import UserEmailManager
from Utils.validators import ModelValidator


class User(AbstractBaseUser, AppModel, PermissionsMixin):

    email = models.EmailField(
        _('email'),
        unique=True,
        blank=False,
        null=True,
        error_messages={
            'unique': 'Ya existe otra cuenta asociada a '
            'este correo electrónico.',
        },
    )
    name = models.CharField(
        _('name'),
        max_length=100,
        blank=True,
        null=True
    )
    position = models.ForeignKey(
        'Position',
        verbose_name="puesto",
        related_name="assign_to",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    is_staff = models.BooleanField(
        _('staff status'),
        null=True,
        help_text=_('Al ser Staff se permite acceso al administrador.'),
    )
    is_active = models.BooleanField(
        _('active'),
        null=True,
        blank=True
    )
    is_verified = models.BooleanField(
        _('verificado'),
        null=True,
        blank=True
    )
    date_verified = models.DateTimeField(
        _('fecha de verificacion'),
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )
    is_superuser = models.BooleanField(
        _('superusuario'),
        null=True,
        help_text=_(
            'Un usuario Superusuario tiene privilegios totales sobre '
            'el sitio.'
        )
    )
    is_admin = models.BooleanField(
        _('administrador'),
        default=False,
        help_text=_(
            'Un usuario administrador tienen privilegios totales '
            'sobre el sitio.'
        )
    )
    first_login = models.BooleanField(
        "¿Primer ingreso?",
        null=True,
        blank=True
    )
    reset_password = models.BooleanField(
        "cambiar contraseña",
        null=True,
        blank=True
    )
    session_key = models.CharField(
        verbose_name="clave de sesión",
        max_length=40,
        null=True,
        blank=True
    )
    success_login_counter = models.PositiveIntegerField(
        verbose_name="cant. de accesos",
        null=True,
        blank=True,
        default=0
    )
    last_activity = models.DateTimeField(
        verbose_name="ultima actividad",
        null=True,
        blank=True
    )
    fail_login_counter = models.IntegerField(
        verbose_name="cant. de intentos de acceso",
        default=0,
        null=True,
        blank=True
    )
    last_pass_change = models.DateTimeField(
        verbose_name="ultimo cambio de password",
        null=True,
        blank=True
    )

    objects = UserEmailManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.email


class Module(models.Model):

    key = models.CharField(
        verbose_name='clave',
        max_length=50,
        blank=False,
        null=False,
        unique=True
    )
    name = models.CharField(
        verbose_name='nombre',
        max_length=50,
        blank=False,
        null=False,
    )
    route = models.CharField(
        verbose_name='ruta',
        max_length=200,
        blank=True,
        null=True,
    )
    active = models.BooleanField(
        verbose_name="activo",
        blank=False,
        null=True
    )

    class Meta:
        verbose_name = 'Modulo'
        verbose_name_plural = 'Modulos'

    def save(self, *args, **kwargs):
        self.key = self.key.upper()
        # self.name = self.name.upper()
        super(Module, self).save(*args, **kwargs)

    def __str__(self):
        value = "{}: {}".format(
            self.key,
            self.name
        )
        return value


class Action(AppModel):

    key = KeyCharField(
        verbose_name="clave",
        unique=True,
        max_length=50,
        blank=False,
        null=False,
        validators=[ModelValidator.check_DontHaveWhitespaces, ]
    )
    description = DescriptionCharField(
        verbose_name="descripción",
        max_length=144,
        blank=False,
        null=True,
    )
    comments = models.TextField(
        verbose_name="comentarios",
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        verbose_name="activo",
        blank=False,
        null=True
    )

    class Meta:
        verbose_name = 'Acción'
        verbose_name_plural = 'Acciones'

    def __str__(self):
        return self.key


class Permission(models.Model):

    position = models.ForeignKey(
        'Position',
        verbose_name='puesto',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    module = models.ForeignKey(
        Module,
        verbose_name='modulo',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    action = models.ForeignKey(
        'Action',
        verbose_name='acción',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        verbose_name="activo",
        blank=False,
        null=True
    )

    class Meta:
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos'
        unique_together = (('module', 'position'),)


class Page(AppModel):

    key = models.CharField(
        verbose_name="clave",
        unique=True,
        max_length=50,
        blank=False,
        null=False,
        validators=[ModelValidator.check_DontHaveWhitespaces, ]
    )
    description = DescriptionCharField(
        verbose_name="descripción",
        max_length=144,
        blank=False,
        null=True,
    )
    web_id = KeyCharField(
        verbose_name="ID en Web",
        max_length=50,
        blank=True,
        null=True,
        validators=[ModelValidator.check_DontHaveWhitespaces, ]
    )
    label = models.CharField(
        verbose_name="Etiqueta",
        max_length=144,
        blank=True,
        null=True,
    )
    icon = models.CharField(
        verbose_name="Icon",
        max_length=144,
        blank=True,
        null=True,
    )
    is_menuoption = models.BooleanField(
        verbose_name="mostrar en menú",
        blank=False,
        null=True
    )
    comments = models.TextField(
        verbose_name="comentarios",
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        verbose_name="activo",
        blank=False,
        null=True
    )

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'

    def __str__(self):
        return self.key


class PageAllowed(AppModel):

    position = models.ForeignKey(
        'Position',
        verbose_name='puesto',
        on_delete=models.PROTECT,
        related_name='pages_allowed',
        blank=True,
        null=True,
    )
    page = models.ForeignKey(
        'Page',
        verbose_name='página',
        on_delete=models.PROTECT,
        related_name='in_menu',
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        verbose_name="activo",
        blank=False,
        null=True
    )

    class Meta:
        verbose_name = 'Opción de menú'
        verbose_name_plural = 'Menu'
        unique_together = (('position', 'page'),)


class Position(models.Model):

    name = models.CharField(
        verbose_name='nombre',
        max_length=50,
        unique=True,
        blank=False,
        null=False,
    )
    parent = models.ForeignKey(
        'self',
        verbose_name='puesto padre',
        related_name='children',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    start_page = models.ForeignKey(
        Page,
        verbose_name='página de inicio',
        related_name='startpage_in',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    pages = models.ManyToManyField(
        Page,
        through=PageAllowed,
        verbose_name='Paginas permitidas',
        related_name='assigned_to',
        blank=True,
    )
    permissions = models.ManyToManyField(
        Module,
        through=Permission,
        verbose_name='Permisos',
        related_name='assigned_to',
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name="activo",
        blank=False,
        null=True
    )

    class Meta:
        verbose_name = 'Puesto'
        verbose_name_plural = 'Puestos'

    def __str__(self):
        return self.name


class ActivityLog(AppModel):

    activity = models.CharField(
        verbose_name='acción',
        max_length=100,
        null=True,
        blank=True
    )
    comments = models.TextField(
        verbose_name='comments',
        blank=True,
        null=True
    )
    origin = models.CharField(
        verbose_name='origen',
        max_length=50,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Log de acciones'
        verbose_name_plural = 'Logs de acciones'

    def __str__(self):
        return self.activity


TYPES_SERVICE = (
    ('SMTP', 'Servidor de envio de Emails'),
    ('PB', 'Base de datos')
)


class ThirdPartyService(models.Model):

    name = models.CharField(
        verbose_name='nombre',
        max_length=100,
        unique=True,
        null=True,
        blank=False,
    )
    type = models.CharField(
        verbose_name='tipo',
        max_length=10,
        null=True,
        blank=False,
        choices=TYPES_SERVICE,
        default='SMTP'
    )
    host = models.CharField(
        'host',
        max_length=150,
        null=True,
        blank=True,
    )
    port = models.IntegerField(
        'puerto',
        null=True,
        blank=True,
    )
    username = models.CharField(
        'usuario',
        max_length=150,
        null=True,
        blank=True,
    )
    password = models.CharField(
        'contraseña',
        max_length=150,
        null=True,
        blank=True,
    )
    use_tls = models.BooleanField(
        'TLS',
        default=False,
    )
    fail_silently = models.BooleanField(
        verbose_name='errores en silencio',
        blank=False,
        null=True
    )
    is_active = models.BooleanField(
        verbose_name='activo',
        blank=False,
        null=True
    )
    comments = models.TextField(
        verbose_name='comentarios',
        blank=True,
        null=True
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Servicio de Terceros'
        verbose_name_plural = 'Servicios de Terceros'

    def __str__(self):
        value = f"{self.name}"
        return value


class GlobalVariable(models.Model):

    key = models.CharField(
        verbose_name='clave',
        max_length=100,
        null=True,
        blank=False,
    )
    description = models.TextField(
        verbose_name='descripción',
        blank=True,
        null=True,
    )
    value = models.TextField(
        verbose_name='valor',
        blank=True,
        null=True,
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Valor de configuración'
        verbose_name_plural = 'Configuraciones Globales'

    def __str__(self):
        value = self.key
        return value


class Integration(models.Model):

    name = models.CharField(
        verbose_name='nombre',
        max_length=144,
        null=True,
        blank=False,
    )
    user = models.ForeignKey(
        User,
        verbose_name="usuario",
        related_name="integrations",
        on_delete=models.PROTECT,
        blank=True,
        null=False
    )
    token = models.CharField(
        verbose_name='token',
        max_length=144,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Integración'
        verbose_name_plural = 'Integraciones'

    def __str__(self):
        value = self.name
        return value

    def save(self, *args, **kwargs):

        if not self.id:
            self.token = secrets.token_hex(64)

        return super(Integration, self).save(*args, **kwargs)
