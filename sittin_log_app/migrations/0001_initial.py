# Generated by Django 2.2 on 2019-06-02 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=48)),
                ('family_address', models.CharField(max_length=255)),
                ('contact1', models.CharField(max_length=48)),
                ('contact1_phone', models.CharField(max_length=15)),
                ('contact1_email', models.EmailField(max_length=48)),
                ('contact2', models.CharField(max_length=48)),
                ('contact2_phone', models.CharField(max_length=15)),
                ('contact2_email', models.EmailField(max_length=48)),
                ('emergency_contact', models.CharField(max_length=48)),
                ('emergency_contact_phone', models.CharField(max_length=15)),
                ('vet_clinic', models.CharField(max_length=48)),
                ('vet_phone', models.CharField(max_length=15)),
                ('vet_address', models.CharField(max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='family', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=48)),
                ('pet_photo_url', models.URLField(max_length=500)),
                ('bio', models.CharField(max_length=255)),
                ('animal_type', models.CharField(choices=[('animal', 'Animal'), ('amphibian', 'Amphibian'), ('birb', 'Birb'), ('doggo', 'Doggo'), ('fish', 'Fish'), ('kitteh', 'Kitteh'), ('livestock', 'Livestock'), ('rabbit', 'Rabbit'), ('reptile', 'Reptile'), ('rodent', 'Rodent')], default='Animal', max_length=48)),
                ('age', models.IntegerField()),
                ('birthday_adoptiversary', models.CharField(max_length=48)),
                ('feeding_notes', models.CharField(max_length=500)),
                ('care_routine', models.CharField(max_length=500)),
                ('other_info', models.CharField(max_length=500)),
                ('family', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pet', to='sittin_log_app.Family')),
            ],
        ),
    ]
