from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Family(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='family', null=True)

    family_name = models.CharField(max_length=48)
    family_address = models.CharField(max_length=255)

    contact1 = models.CharField(max_length=48)
    contact1_phone = models.CharField(max_length=15)
    contact1_email = models.EmailField(max_length=48)

    contact2 = models.CharField(max_length=48)
    contact2_phone = models.CharField(max_length=15)
    contact2_email = models.EmailField(max_length=48)

    emergency_contact = models.CharField(max_length=48)
    emergency_contact_phone = models.CharField(max_length=15)

    vet_clinic = models.CharField(max_length=48)
    vet_phone = models.CharField(max_length=15)
    vet_address = models.CharField(max_length=255)

    def __repr__(self):
        return f'<Family: {self.family_name}>'
    
    def __str__(self):
        return f'Family: {self.family_name}'


class Pet(models.Model):

    TYPES = [
        ('animal', 'Animal'),
        ('amphibian', 'Amphibian'),
        ('birb', 'Birb'),
        ('doggo', 'Doggo'),
        ('fish', 'Fish'),
        ('kitteh', 'Kitteh'),
        ('livestock', 'Livestock'),
        ('rabbit', 'Rabbit'),
        ('reptile', 'Reptile'),
        ('rodent', 'Rodent'),
    ]

    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='pet', null=True)

    pet_name = models.CharField(max_length=48)
    pet_photo_url = models.CharField(max_length=1000)
    bio = models.CharField(max_length=255)

    animal_type = models.CharField(choices=TYPES, default='Animal', max_length=48)
    age = models.IntegerField()
    birthday_adoptiversary = models.CharField(max_length=48)

    feeding_notes = models.CharField(max_length=500)
    care_routine = models.CharField(max_length=500)
    other_info = models.CharField(max_length=500)


    def __repr__(self):
        return f'<{self.pet_name}, {self.family}\'s {self.animal_type}>'
    
    def __str__(self):
        return f'{self.pet_name}, {self.family}\'s {self.animal_type}'


# class Household(models.Model):

#     family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='pet', null=True)

#     home_care_notes = models.CharField(max_length=500)

#     def __repr__(self):
#         return f'<{self.family}\'s home>'

#     def __str__(self):
#         return f'{self.family}\'s home'
