from django.contrib import admin

from .models import PurchaseOrder


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ["po_number", "vendor", "items", "quantity", "status"]

