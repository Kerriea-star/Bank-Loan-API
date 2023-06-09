# Generated by Django 4.1.7 on 2023-03-23 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Approvals",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("firstname", models.CharField(max_length=128)),
                ("lastname", models.CharField(max_length=128)),
                ("dependants", models.IntegerField(default=0)),
                ("applicantincome", models.IntegerField(default=0)),
                ("coapplicantincome", models.IntegerField(default=0)),
                ("loanamt", models.IntegerField(default=0)),
                ("loanterm", models.IntegerField(default=0)),
                ("credicthistory", models.IntegerField(default=0)),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")], max_length=15
                    ),
                ),
                (
                    "married",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")], max_length=15
                    ),
                ),
                (
                    "graduateducation",
                    models.CharField(
                        choices=[
                            ("Graduate", "Graduate"),
                            ("Not_Graduate", "Not_Graduate"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "selfemployed",
                    models.CharField(
                        choices=[("Yes", "Yes"), ("No", "No")], max_length=15
                    ),
                ),
                (
                    "area",
                    models.CharField(
                        choices=[
                            ("Rural", "Rural"),
                            ("Semiurban", "Semiurban"),
                            ("Urban", "Urban"),
                        ],
                        max_length=15,
                    ),
                ),
            ],
        ),
    ]
