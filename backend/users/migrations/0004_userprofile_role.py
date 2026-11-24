from typing import ClassVar

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies: ClassVar[list] = [
        ("users", "0003_friendship_and_profile_photo"),
    ]

    operations: ClassVar[list] = [
        migrations.AddField(
            model_name="userprofile",
            name="role",
            field=models.CharField(choices=[("admin", "Админ"), ("manager", "Менеджер"), ("client", "Клиент")], default="client", max_length=16),
        ),
    ]

