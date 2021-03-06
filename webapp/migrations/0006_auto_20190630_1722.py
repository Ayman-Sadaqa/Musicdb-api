# Generated by Django 2.2 on 2019-06-30 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20190630_1713'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ('albumName',)},
        ),
        migrations.AddField(
            model_name='album',
            name='Artist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.Artist'),
            preserve_default=False,
        ),
    ]
