# Generated by Django 3.2.19 on 2023-06-05 11:14

import django.contrib.postgres.fields
from django.db import migrations, models

BATCH_SIZE = 1000


def queryset_in_batches(queryset):
    """Slice a queryset into batches.

    Input queryset should be sorted be pk.
    """
    start_pk = 0

    while True:
        qs = queryset.order_by("pk").filter(pk__gt=start_pk)[:BATCH_SIZE]
        pks = list(qs.values_list("pk", flat=True))

        if not pks:
            break

        yield pks

        start_pk = pks[-1]


def convert_void_to_cancel(apps, schema_editor):
    TransactionItem = apps.get_model("payment", "TransactionItem")
    qs = TransactionItem.objects.filter(available_actions__contains=["void"]).order_by(
        "pk"
    )
    for batch_pks in queryset_in_batches(qs):
        transactions = TransactionItem.objects.filter(pk__in=batch_pks)
        for transaction_item in transactions:
            current_available_actions = transaction_item.available_actions
            if "void" in current_available_actions:
                current_available_actions.remove("void")
                current_available_actions.append("cancel")
            TransactionItem.objects.bulk_update(transactions, ["available_actions"])


class Migration(migrations.Migration):
    dependencies = [
        ("payment", "0050_drop_unused_transaction_fields"),
    ]

    operations = [
        migrations.RunPython(convert_void_to_cancel, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="transactionitem",
            name="available_actions",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(
                    choices=[
                        ("charge", "Charge payment"),
                        ("refund", "Refund payment"),
                        ("cancel", "Cancel payment"),
                    ],
                    max_length=128,
                ),
                default=list,
                size=None,
            ),
        ),
    ]
