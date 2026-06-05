class SoftDeleteMixin:

    def perform_destroy(self, instance):
        instance.activo = False
        instance.save()