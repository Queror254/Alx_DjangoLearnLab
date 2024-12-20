# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import AppConfig


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth, profile_photo=profile_photo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, date_of_birth, profile_photo, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']  

    def __str__(self):
        return self.email


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title


class YourAppConfig(AppConfig):
    name = 'LibraryProject.bookshelf'

    def ready(self):
        self.create_groups()

    def create_groups(self):
        # Create Groups if they do not exist
        groups = ['Editors', 'Viewers', 'Admins']
        for group_name in groups:
            Group.objects.get_or_create(name=group_name)

        # Get the content type for the Book model
        content_type = ContentType.objects.get_for_model(Book)

        # Get permissions
        can_view_permission = Permission.objects.get(codename='can_view', content_type=content_type)
        can_create_permission = Permission.objects.get(codename='can_create', content_type=content_type)
        can_edit_permission = Permission.objects.get(codename='can_edit', content_type=content_type)
        can_delete_permission = Permission.objects.get(codename='can_delete', content_type=content_type)

        # Get or create the groups
        editor_group = Group.objects.get(name='Editors')
        viewer_group = Group.objects.get(name='Viewers')
        admin_group = Group.objects.get(name='Admins')

        # Assign permissions to groups
        editor_group.permissions.set([can_create_permission, can_edit_permission])
        viewer_group.permissions.set([can_view_permission])
        admin_group.permissions.set([can_view_permission, can_create_permission, can_edit_permission, can_delete_permission])

        # Save groups
        editor_group.save()
        viewer_group.save()
        admin_group.save()
