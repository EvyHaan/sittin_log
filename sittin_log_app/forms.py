from django.forms import ModelForm
from .models import Pet, Family

class PetForm(ModelForm):

    class Meta:
        model = Pet
        fields = ['family', 'pet_name', 'pet_photo_url', 'bio', 'animal_type', 'age', 'birthday_adoptiversary', 'feeding_notes', 'care_routine', 'other_info']
    
class PictureForm(ModelForm):

    class Meta:
        model = Family
        fields = ['family_name', 'family_address', 'contact1', 'contact1_phone', 'contact1_email', 'contact2', 'contact2_phone', 'contact2_email', 'emergency_contact', 'emergency_contact_phone', 'vet_clinic', 'vet_phone', 'vet_address']