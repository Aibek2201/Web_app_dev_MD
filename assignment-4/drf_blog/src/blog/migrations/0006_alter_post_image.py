# Generated by Django 4.1.5 on 2023-03-04 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(default="cover-photo-3.PNG", upload_to=""),
        ),
    ]