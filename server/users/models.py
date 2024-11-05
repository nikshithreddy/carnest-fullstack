from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

#  Custom User Manager
class UserManager(BaseUserManager):
  def create_user(self, email, first_name, last_name, phone_number, terms_and_conditions_accepted, password=None, password2=None,):
      """
      Creates and saves a User with the given email, first_name, last_name, phone_number, terms_and_conditions_accepted, password.
      """
      if not email:
          raise ValueError('User must have an email address')

      user = self.model(
          email=self.normalize_email(email),
          first_name=first_name,
          last_name= last_name,
          phone_number= phone_number,
          terms_and_conditions_accepted=terms_and_conditions_accepted,
      )
      user.set_password(password)
      user.save(using=self._db)
      return user

  def create_superuser(self, email, first_name, last_name, terms_and_conditions_accepted,phone_number= None , password=None):
      """
      Creates and saves a superuser with the given email, first_name, last_name, phone_number, terms_and_conditions_accepted, password.
      """
      user = self.create_user(
          email,
          password= password,
          first_name=first_name,
          last_name= last_name,
          phone_number= phone_number,
          terms_and_conditions_accepted = terms_and_conditions_accepted,
      )
      user.is_admin = True
      user.save(using=self._db)
      return user

#  Custom User Model
class User(AbstractBaseUser ):
  # Basic user information
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True )
    first_name = models.CharField(max_length=30, default='None')
    last_name = models.CharField(max_length=30, blank=True, default='None')
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    # # Personal details
    date_of_birth = models.DateField(null=True, blank=True)
    # address = models.TextField(null=True, blank=True)
    # gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], null=True)

    # # Verification and security
    # email_verified = models.BooleanField(default=False)
    # phone_number_verified = models.BooleanField(default=False)
    # government_id_type = models.CharField(max_length=50, null=True, blank=True)
    # government_id_number = models.CharField(max_length=50, null=True, blank=True)

    # # Carpool-specific details
    # bio = models.TextField(null=True, blank=True)
    # preferred_carpool_days = models.CharField(max_length=255, null=True, blank=True)
    # rating = models.FloatField(default=0.0)
    # total_reviews = models.PositiveIntegerField(default=0)

    # Activity details
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    # total_rides_completed = models.PositiveIntegerField(default=0)
    # cancellations = models.PositiveIntegerField(default=0)
    
    # Security and compliance
    terms_and_conditions_accepted = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'terms_and_conditions_accepted']

    def _str_(self):
        return self.email


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin




# # Vehicle Model for User's Vehicles
# class Vehicle(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicles')
#     make = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#     plate_number = models.CharField(max_length=20, unique=True)
#     year = models.PositiveIntegerField()
#     color = models.CharField(max_length=50)
#     number_of_seats = models.PositiveIntegerField()

#     def _str_(self):
#         return f"{self.make} {self.model} ({self.plate_number})"


