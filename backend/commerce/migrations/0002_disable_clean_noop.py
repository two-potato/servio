from typing import ClassVar

from django.db import migrations


def noop(apps, schema_editor):
    # No DB changes required; business validation disabled at model clean level
    pass


class Migration(migrations.Migration):
    dependencies: ClassVar[list] = [
        ("commerce", "0001_initial"),
    ]

    operations: ClassVar[list] = [
        migrations.RunPython(noop, reverse_code=noop),
    ]

