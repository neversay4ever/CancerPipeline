from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from djangoql.admin import DjangoQLSearchMixin
from django.core import serializers

# Register your models here.
from .models import Cancer, Panel, Gene, Mutation, Fusion, RefGeneFlat, OncoKB, OncoKBMutation, Civic, PharmGKB, Hereditary, ClinicalTrials, ImmunityReport, Drug, TargetDrug
from django.db.models import Count


class CustomModelAdmin(DjangoQLSearchMixin, ImportExportModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [
            field.name for field in model._meta.fields if field.name != "id"]
        self.search_fields = [
            field.name for field in model._meta.fields if field.name != "id"]
        super(CustomModelAdmin, self).__init__(model, admin_site)


@admin.register(Cancer)
class CancerAdmin(CustomModelAdmin):
    pass


@admin.register(Panel)
class PanelAdmin(CustomModelAdmin):
    pass


@admin.register(Gene)
class GeneAdmin(CustomModelAdmin):
    pass


@admin.register(Mutation)
class MutationAdmin(CustomModelAdmin):
    pass


@admin.register(Fusion)
class FusionAdmin(CustomModelAdmin):
    pass


@admin.register(RefGeneFlat)
class RefGeneFlatAdmin(CustomModelAdmin):
    pass


@admin.register(OncoKB)
class OncoKBAdmin(CustomModelAdmin):
    pass


@admin.register(OncoKBMutation)
class OncoKBMutationAdmin(CustomModelAdmin):
    pass


@admin.register(Civic)
class CivicAdmin(CustomModelAdmin):
    pass


@admin.register(PharmGKB)
class PharmGKBAdmin(CustomModelAdmin):
    pass


@admin.register(Hereditary)
class HereditaryAdmin(CustomModelAdmin):
    pass


@admin.register(ClinicalTrials)
class ClinicalTrialsAdmin(CustomModelAdmin):
    pass


@admin.register(ImmunityReport)
class ImmunityReportAdmin(CustomModelAdmin):
    pass


@admin.register(Drug)
class DrugReportAdmin(CustomModelAdmin):
    pass


@admin.register(TargetDrug)
class TargetDrugAdmin(CustomModelAdmin):
    pass
