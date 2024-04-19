# Generated by Django 5.0.2 on 2024-03-15 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("EmployeeID", models.IntegerField(primary_key=True, serialize=False)),
                ("Age", models.IntegerField()),
                ("Attrition", models.CharField(max_length=3)),
                ("BusinessTravel", models.CharField(max_length=50)),
                (
                    "Department",
                    models.CharField(
                        choices=[
                            ("Nursing", "Nursing"),
                            ("Care", "Care"),
                            ("Dietary", "Dietary"),
                        ],
                        max_length=50,
                    ),
                ),
                ("DistanceFromHome", models.IntegerField()),
                ("Education", models.IntegerField()),
                ("EducationField", models.CharField(max_length=50)),
                (
                    "Gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")], max_length=50
                    ),
                ),
                ("HourlyRate", models.IntegerField()),
                ("JobLevel", models.IntegerField()),
                (
                    "JobRole",
                    models.CharField(
                        choices=[
                            ("Nurse", "Nurse"),
                            ("Other", "Other"),
                            ("Therapist", "Therapist"),
                            ("Administrative", "Administrative"),
                            ("Admin", "Admin"),
                        ],
                        max_length=50,
                    ),
                ),
                ("JobSatisfaction", models.IntegerField()),
                (
                    "MaritalStatus",
                    models.CharField(
                        choices=[
                            ("Married", "Married"),
                            ("Single", "Single"),
                            ("Divorced", "Divorced"),
                        ],
                        max_length=50,
                    ),
                ),
                ("MonthlyIncome", models.IntegerField()),
                ("MonthlyRate", models.IntegerField()),
                ("NumCompaniesWorked", models.IntegerField()),
                ("OverTime", models.CharField(max_length=3)),
                ("PerformanceRating", models.IntegerField()),
                ("StandardHours", models.IntegerField()),
                ("Shift", models.IntegerField()),
                ("TotalWorkingYears", models.IntegerField()),
                ("TrainingTimesLastYear", models.IntegerField()),
                ("WorkLifeBalance", models.IntegerField()),
                ("YearsAtCompany", models.IntegerField()),
                ("YearsInCurrentRole", models.IntegerField()),
                ("YearsSinceLastPromotion", models.IntegerField()),
                ("YearsWithCurrManager", models.IntegerField()),
                ("Hours", models.IntegerField()),
            ],
        ),
    ]