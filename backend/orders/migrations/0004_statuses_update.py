from typing import ClassVar

from django.db import migrations


def forwards(apps, schema_editor):
    # Map old statuses to new ones
    mapping = {
        "approved": "confirmed",
        "shipped": "delivering",
        "done": "delivered",
        # keep 'new' and 'paid' and 'canceled' as-is
    }
    Order = apps.get_model("orders", "Order")
    for old, new in mapping.items():
        Order.objects.filter(status=old).update(status=new)


def backwards(apps, schema_editor):
    # Reverse mapping if needed
    mapping = {
        "confirmed": "approved",
        "delivering": "shipped",
        "delivered": "done",
    }
    Order = apps.get_model("orders", "Order")
    for old, new in mapping.items():
        Order.objects.filter(status=old).update(status=new)


class Migration(migrations.Migration):
    dependencies: ClassVar[list] = [
        ("orders", "0003_order_fk_nullable"),
    ]

    operations: ClassVar[list] = [
        migrations.RunPython(forwards, backwards),
    ]

