from django.db import migrations


def create_roles(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    for name in ['Administrador', 'Editor']:
        Group.objects.get_or_create(name=name)


def delete_roles(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name__in=['Administrador', 'Editor']).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0002_asistente_creado_por_asistente_modificado_por_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(create_roles, delete_roles),
    ]
