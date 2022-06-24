# Generated by Django 4.0.3 on 2022-05-04 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_delete_portfoliodetails_rename_image_post_prim_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='post_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img3', models.ImageField(upload_to='pics')),
                ('title3', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('client', models.CharField(max_length=100)),
                ('projDate', models.CharField(max_length=100)),
                ('fashiontitle', models.CharField(max_length=100)),
                ('fashiondes', models.CharField(max_length=100)),
                ('fashionContent', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.post')),
            ],
        ),
        migrations.DeleteModel(
            name='Aboutproduct',
        ),
    ]
