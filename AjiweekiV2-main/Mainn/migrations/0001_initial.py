# Generated by Django 4.0.5 on 2022-11-25 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MasterTable', '0001_initial'),
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=2000, null=True)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('category_name', models.CharField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elements', models.CharField(blank=True, max_length=2000, null=True)),
                ('name', models.CharField(blank=True, max_length=2000, null=True)),
                ('is_required', models.CharField(blank=True, max_length=2000, null=True)),
                ('form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Mainn.form')),
                ('question_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MasterTable.questiontype')),
            ],
        ),
        migrations.CreateModel(
            name='UserResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(blank=True, max_length=2000, null=True)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='Mainn.questions')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Account.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=2000, null=True)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Mainn.questions')),
            ],
        ),
    ]
