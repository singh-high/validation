# Generated by Django 4.0.3 on 2022-05-02 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recharge', '0003_alter_rechargehistory_acc_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='rechargehistory',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rechargehistory',
            name='type',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]
