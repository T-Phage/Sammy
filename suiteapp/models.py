from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# Create your models here.
class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    faculty_name = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        default='_'
    )

    def __str__(self):
        return str(self.faculty_name)

    class Meta:
        verbose_name_plural = 'Faculties'


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(
        max_length=255,
        unique=True,
        blank=True, default='-'
    )
    faculty = models.ForeignKey(Faculty, null=True, verbose_name="faculty", on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.dept_name)


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    firstname = models.CharField(
        verbose_name='firstname',
        max_length=255,
        null=True,
    )
    surname = models.CharField(
        verbose_name='lastname',
        max_length=255,
        null=True,
    )
    othername = models.CharField(
        verbose_name='othername',
        max_length=255,
        null=True,
        blank=True,
    )
    gender = models.CharField(
        verbose_name='gender',
        max_length=255,
        null=True, default='null',
    )
    # faculty = models.ForeignKey(
    #     Faculty,
    #     verbose_name='faculty',
    #     null=True, default='null',
    #     on_delete=models.SET_NULL,
    # )
    department = models.ForeignKey(
        Department,
        verbose_name='department',
        null=True,
        on_delete=models.SET_NULL,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_full_name(self):
        # The user is identified by their email address
        return self.firstname + " " + self.surname

    class Meta:
        verbose_name_plural = 'Users'


class Folder(models.Model):
    folder_id = models.AutoField(primary_key=True)
    folder_name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    is_rep = models.BooleanField(default=True)
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.SET_NULL)
    faculty = models.ForeignKey(Faculty, blank=True, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL)
    main_folder = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.folder_name)


class Task(models.Model):
    # task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100, primary_key=True,)
    assigner = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.task_name)
        
    
class File(models.Model):
    uploaded_by = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL)
    file_id = models.AutoField(primary_key=True)
    filepath = models.FileField(upload_to='files/', null=True, verbose_name="")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.SET_NULL,)
    faculty = models.ForeignKey(Faculty, blank=True, null=True, on_delete=models.SET_NULL, )
    is_rep = models.BooleanField(default=False)
    folder = models.ForeignKey(Folder, blank=True, null=True, on_delete=models.CASCADE)
    is_task = models.BooleanField(default=False)
    task_name = models.ForeignKey(Task, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.filepath)  # + ":" + str(self.filepath)

    def last_10_files(self):
        return File.objects.order_by('-file_id').all()

    def display_text_file(self):
        with open(self.filepath.path) as fp:
            return fp.read().replace('\n', '<br>')


class Site(models.Model):
    site_name = models.CharField(max_length=200)
    site_id = models.CharField(max_length=200,primary_key=True, unique=True)
    description = models.TextField()
    site_visibilty = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.site_name)


PRIO_CHOICES = [('high', 'High'),
                ('medium', 'Medium'),
                ('low', 'Low')]
class TaskDetail(models.Model):
    task = models.ForeignKey(Task, blank=True,  null=True, on_delete=models.CASCADE)
    priority = models.CharField(blank=True, max_length=7, choices=PRIO_CHOICES,)
    due_date = models.DateField(blank=True, null=True)
    due_time = models.TimeField(blank=True, null=True)
    assignee = models.ForeignKey(MyUser, blank=True, null=True, on_delete=models.SET_NULL)
    faculty = models.ForeignKey(Faculty, blank=True, null=True, on_delete=models.SET_NULL)
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.SET_NULL)
    comment = models.TextField(blank=True, null=True,)


ROLE_CHOICE = [('---------', '---------'),
               ('manager', 'manager'),
               ('collaborator', 'collaborator'),
               ('contributor', 'contributor'),
               ('consumer', 'consumer'),]
class SiteUser(models.Model):
    site = models.ForeignKey(Site,blank=True, null=True, on_delete=models.SET_NULL) 
    user = models.ForeignKey(MyUser,blank=True, null=True, on_delete=models.SET_NULL)
    role = models.CharField(max_length=15, blank=True, choices=ROLE_CHOICE, default='---------',)

    def __str__(self):
        return str(self.site)