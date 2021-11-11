# Generated by Django 3.2.9 on 2021-11-11 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_number', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('balance', models.DecimalField(decimal_places=0, default=0, max_digits=20)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(choices=[('WITHDRAW', 'Withdraw'), ('DEPOSIT', 'Deposit')], max_length=8)),
                ('transaction_amount', models.DecimalField(decimal_places=0, default=0, max_digits=20)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=20)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eightpercent.account')),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
    ]
