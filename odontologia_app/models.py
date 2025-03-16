from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.conf import settings


class Rol(models.Model):
    es_admin = models.BooleanField(default=False, verbose_name="Es Administrador")

    def __str__(self):
        return "Administrador" if self.es_admin else "Usuario"

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"


class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombre, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico.')
        email = self.normalize_email(email)
        if usuario.objects.filter(email=email).exists():
            raise ValueError('El correo electrónico ya está en uso.')
        usuario = self.model(
            email=email,
            nombre=nombre,
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, nombre, password):
        usuario = self.create_user(
            email=self.normalize_email(email),
            nombre=nombre,
            password=password,
        )
        usuario.is_admin = True
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.save(using=self._db)
        return usuario


class usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['nombre'] 

    def __str__(self):
        return self.nombre

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


class Representante(models.Model):
    cedula = models.CharField(max_length=20, primary_key=True, verbose_name="Cédula del Representante")
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Representante")

    def __str__(self):
        return f"{self.nombre} (Cédula: {self.cedula})"

    class Meta:
        verbose_name = "Representante"
        verbose_name_plural = "Representantes"

class Paciente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]

    ESTADO_CIVIL_CHOICES = [
        (True, 'Casado'),
        (False, 'Soltero'),
    ]

    id = models.AutoField(primary_key=True, verbose_name="ID del Paciente")
    cedula_representante = models.ForeignKey(
        Representante,  # Relación con el modelo Representante
        on_delete=models.CASCADE,
        verbose_name="Cédula del Representante",
        related_name="pacientes",
        null=True,  # Permite valores nulos
        blank=True   # Permite que el campo esté vacío en formularios
    )
    cedula = models.CharField(max_length=20, verbose_name="Cédula del Paciente")
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Paciente")  
    edad = models.PositiveIntegerField(verbose_name="Edad del Paciente")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono del Paciente")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name="Sexo del Paciente")
    estado_civil = models.BooleanField(choices=ESTADO_CIVIL_CHOICES, verbose_name="Estado Civil")
    ocupacion = models.CharField(max_length=100, verbose_name="Ocupación del Paciente")

    def __str__(self):
        return f"Paciente {self.id} (Cédula: {self.cedula})"

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

class HistoriaMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    examinador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Examinador")  # Usar el modelo de usuario configurado en settings
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def __str__(self):
        return f"Historia Médica de {self.paciente.nombre} (Examinador: {self.examinador.nombre})"

    class Meta:
        verbose_name = "Historia Médica"
        verbose_name_plural = "Historias Médicas"

class Anamnesis(models.Model):
    historia_medica = models.OneToOneField(
        'HistoriaMedica',  # Nombre corregido del modelo
        on_delete=models.CASCADE,
        verbose_name="Historia Médica",
        related_name="anamnesis"
    )
    diabetes = models.BooleanField(default=False, verbose_name="Diabetes")
    tbc = models.BooleanField(default=False, verbose_name="T.B.C.")
    hipertension = models.BooleanField(default=False, verbose_name="Hipertensión")
    artritis = models.BooleanField(default=False, verbose_name="Artritis")
    alergias = models.BooleanField(default=False, verbose_name="Alergias")
    neuralgias = models.BooleanField(default=False, verbose_name="Neuralgias")
    hemorragias = models.BooleanField(default=False, verbose_name="Hemorragias")
    hepatitis = models.BooleanField(default=False, verbose_name="Hepatitis")
    sinusitis = models.BooleanField(default=False, verbose_name="Sinusitis")
    trastornos_mentales = models.BooleanField(default=False, verbose_name="Trastornos Mentales")
    enfermedades_eruptivas = models.BooleanField(default=False, verbose_name="Enfermedades Eruptivas")
    enfermedades_renales = models.BooleanField(default=False, verbose_name="Enfermedades Renales")
    parotiditis = models.BooleanField(default=False, verbose_name="Parotiditis")

    def __str__(self):
        return f"Anamnesis de {self.historia_medica.paciente.nombre}"

    class Meta:
        verbose_name = "Anamnesis"
        verbose_name_plural = "Anamnesis"



class AntecedentesFamiliares(models.Model):
    TIPO_CHOICES = [
        ('P', 'Paternos'),
        ('M', 'Maternos'),
        ('A', 'Ambos'),
    ]

    anamnesis = models.ForeignKey(
        Anamnesis, 
        on_delete=models.CASCADE, 
        verbose_name="Anamnesis",
        related_name='antecedentes_familiares'  
    )
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, verbose_name="Tipo")
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return f"Antecedentes Familiares de {self.anamnesis.historia_medica.paciente.nombre}"

    class Meta:
        verbose_name = "Antecedente Familiar"
        verbose_name_plural = "Antecedentes Familiares"


class Habitos(models.Model):
    anamnesis = models.ForeignKey(
        Anamnesis, 
        on_delete=models.CASCADE, 
        verbose_name="Anamnesis",
        related_name='habitos'  
    )
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return f"Hábitos de {self.anamnesis.historia_medica.paciente.nombre}"

    class Meta:
        verbose_name = "Hábito"
        verbose_name_plural = "Hábitos"
