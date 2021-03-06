# Generated by Django 2.1.7 on 2020-02-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200212_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('category', models.CharField(max_length=255, null=True)),
                ('datePost', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
