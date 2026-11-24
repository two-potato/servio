from typing import ClassVar

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies: ClassVar[list] = [
        ("users", "0001_initial"),
    ]

    operations: ClassVar[list] = [
        migrations.AddField(
            model_name="userprofile",
            name="phone",
            field=models.CharField(max_length=32, null=True, blank=True),
        ),
    ]

