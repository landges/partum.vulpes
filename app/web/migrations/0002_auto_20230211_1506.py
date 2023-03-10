from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='username',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='price_end',
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default=1, upload_to='products'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price_start',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=300),
        ),
    ]