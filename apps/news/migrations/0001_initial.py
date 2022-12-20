# Generated by Django 4.0.4 on 2022-12-06 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='название')),
                ('photo', models.ImageField(upload_to='media')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('date_of_upload', models.DateTimeField(auto_now_add=True, verbose_name='date publish')),
                ('likes', models.IntegerField(default=0)),
                ('news_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='news.category')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'новости',
            },
        ),
    ]