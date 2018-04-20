# Generated by Django 2.0.4 on 2018-04-20 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('number', models.IntegerField(verbose_name='Нумар')),
            ],
        ),
        migrations.CreateModel(
            name='Clergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Імя святара')),
            ],
        ),
        migrations.CreateModel(
            name='Dignity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Сан')),
            ],
        ),
        migrations.CreateModel(
            name='Baptism',
            fields=[
                ('certificate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='certs.Certificate')),
                ('name', models.CharField(max_length=100, verbose_name='')),
            ],
            bases=('certs.certificate',),
        ),
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('certificate_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='certs.Certificate')),
            ],
            bases=('certs.certificate',),
        ),
        migrations.AddField(
            model_name='clergy',
            name='dignity',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='certs.Dignity'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='priest',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='certs.Clergy'),
        ),
    ]