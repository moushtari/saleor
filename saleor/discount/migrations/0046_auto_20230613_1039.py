# Generated by Django 3.2.19 on 2023-06-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("discount", "0045_promotion_promotionrule"),
    ]

    operations = [
        migrations.AddField(
            model_name="checkoutlinediscount",
            name="promotions",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="_discount_checkoutlinediscount_promotions_+",
                to="discount.Promotion",
            ),
        ),
        migrations.AddField(
            model_name="orderdiscount",
            name="promotions",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="_discount_orderdiscount_promotions_+",
                to="discount.Promotion",
            ),
        ),
    ]
