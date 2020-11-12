# Generated by Django 3.0.4 on 2020-10-26 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EasyBarber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_barber',
            name='shop_address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Shop_addresss', to='EasyBarber.Shop_Owner'),
        ),
        migrations.AlterField(
            model_name='shop_barber',
            name='shop_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Shop_Barbers', to='EasyBarber.Shop_Owner'),
        ),
    ]