# Generated by Django 5.0.6 on 2024-06-01 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection_system', '0019_customerrequest_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerrequest',
            old_name='name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='customerrequest',
            name='district',
        ),
        migrations.RemoveField(
            model_name='customerrequest',
            name='payment_status',
        ),
        migrations.RemoveField(
            model_name='customerrequest',
            name='street',
        ),
        migrations.RemoveField(
            model_name='customerrequest',
            name='ward',
        ),
        migrations.AddField(
            model_name='customerrequest',
            name='amount_to_invest',
            field=models.DecimalField(decimal_places=2, default=10000, max_digits=10),
        ),
        migrations.AddField(
            model_name='customerrequest',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='customerrequest',
            name='national_id_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
