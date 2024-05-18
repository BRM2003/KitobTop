# Generated by Django 5.0.6 on 2024-05-18 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="genre",
            name="cr_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="added_by",
                to="users.admins",
            ),
        ),
        migrations.CreateModel(
            name="Languages",
            fields=[
                ("lang_id", models.AutoField(primary_key=True, serialize=False)),
                ("language", models.CharField(max_length=64)),
                ("cr_on", models.DateTimeField(auto_now_add=True)),
                (
                    "cr_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="lang_added_by",
                        to="users.admins",
                    ),
                ),
            ],
            options={
                "verbose_name": "Language",
                "verbose_name_plural": "Languages",
            },
        ),
        migrations.AddField(
            model_name="books",
            name="languages",
            field=models.ManyToManyField(to="products.languages"),
        ),
    ]