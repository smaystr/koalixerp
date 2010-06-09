# -*- coding: utf-8 -*-
from django import forms
from django.core.urlresolvers import reverse
from datetime import date
from crm.models import *
from django.utils.translation import ugettext as _
from django.contrib import admin

   
class ContractPostalAddress(admin.StackedInline):
   model = PostalAddressForContract
   extra = 1
   classes = ('collapse-open',)
   fieldsets = (
      ('Basics', {
         'fields': ('prefix', 'prename', 'name', 'addressline1', 'addressline2', 'addressline3', 'addressline4', 'zipcode', 'town', 'state', 'country', 'purpose')
      }),
   )
   allow_add = True
   
class ContractPhoneAddress(admin.TabularInline):
   model = PhoneAddressForContract
   extra = 1
   classes = ('collapse-open',)
   fieldsets = (
      ('Basics', {
         'fields': ('phone', 'purpose',)
      }),
   )
   allow_add = True
   
class ContractEmailAddress(admin.TabularInline):
   model = EmailAddressForContract
   extra = 1
   classes = ('collapse-open',)
   fieldsets = (
      ('Basics', {
         'fields': ('email', 'purpose',)
      }),
   )
   allow_add = True

class PurchaseOrderPostalAddress(admin.StackedInline):
   model = PostalAddressForPurchaseOrder
   extra = 1
   classes = ('collapse-open',)
   fieldsets = (
      ('Basics', {
         'fields': ('prefix', 'prename', 'name', 'addressline1', 'addressline2', 'addressline3', 'addressline4', 'zipcode', 'town', 'state', 'country', 'purpose')
      }),
   )
   allow_add = True
   
class PurchaseOrderPhoneAddress(admin.TabularInline):
   model = PhoneAddressForPurchaseOrder
   extra = 1
   classes = ('collapse-open',)
   fieldsets = (
      ('Basics', {
         'fields': ('phone', 'purpose',)
      }),
   )
   allow_add = True
   
class PurchaseOrderEmailAddress(admin.TabularInline):
   model = EmailAddressForPurchaseOrder
   extra = 1
   classes = ('collapse-open',)
   fieldsets = (
      ('Basics', {
         'fields': ('email', 'purpose',)
      }),
   )
   allow_add = True

class SalesContractPostalAddress(admin.StackedInline):
   model = PostalAddressForSalesContract
   extra = 1
   classes = ('collapse-open',)
   fieldsets = (
      ('Basics', {
         'fields': ('prefix', 'prename', 'name', 'addressline1', 'addressline2', 'addressline3', 'addressline4', 'zipcode', 'town', 'state', 'country', 'purpose')
      }),
   )
   allow_add = True
   
class SalesContractPhoneAddress(admin.TabularInline):
   model = PhoneAddressForSalesContract
   extra = 1
   classes = ('collapse-open',)
   fieldsets = (
      ('Basics', {
         'fields': ('phone', 'purpose',)
      }),
   )
   allow_add = True
   
class SalesContractEmailAddress(admin.TabularInline):
   model = EmailAddressForSalesContract
   extra = 1
   classes = ('collapse-open',)
   fieldsets = (
      ('Basics', {
         'fields': ('email', 'purpose',)
      }),
   )
   allow_add = True

class SalesContractInlinePosition(admin.TabularInline):
    model = SalesContractPosition
    extra = 1
    classes = ('collapse-open',)
    fieldsets = (
        ('', {
            'fields': ('positionNumber', 'quantity', 'product', 'description', 'discount', 'overwriteProductPrice', 'positionPricePerUnit', 'sentOn', 'shipmentPartner')
        }),
    )
    allow_add = True


class InlineQuote(admin.TabularInline):
   model = Quote
   classes = ('collapse-open')
   extra = 1
   fieldsets = (
      (_('Basics'), {
         'fields': ('contract', 'customer', 'validuntil', 'state')
      }),
      (_('Advanced (not editable)'), {
         'classes': ('collapse',),
         'fields': ('lastPricingDate', 'lastCalculatedPrice')
      }),
   )
   allow_add = True
   
   inlines = [SalesContractInlinePosition, SalesContractPostalAddress, SalesContractPhoneAddress, SalesContractEmailAddress]

class OptionContract(admin.ModelAdmin):
   list_display = ('id', 'description', 'staff')
   list_display_links = ('id','description')
   fieldsets = (
      (_('Basics'), {
         'fields': ('description',)
      }),
   )
   save_as = True
   inlines = [ContractPostalAddress, ContractPhoneAddress, ContractEmailAddress, InlineQuote]


class PurchaseOrderInlinePosition(admin.TabularInline):
    model = PurchaseOrderPosition
    extra = 1
    classes = ('collapse-open',)
    fieldsets = (
        ('', {
            'fields': ('positionNumber', 'quantity', 'product', 'description', 'discount', 'positionPricePerUnit', 'sentOn', 'shipmentPartner')
        }),
    )
    allow_add = True


class OptionInvoice(admin.ModelAdmin):
   list_display = ('contract', 'id', 'customer', 'payableuntil', 'state', 'staff', 'lastmodification', 'lastmodifiedby')
   list_display_links = ('contract','customer')
   fieldsets = (
      (_('Basics'), {
         'fields': ('contract', 'customer', 'payableuntil', 'state')
      }),
      (_('Advanced (not editable)'), {
         'classes': ('collapse',),
         'fields': ('lastPricingDate', 'lastCalculatedPrice')
      }),
   )
   save_as = True
   inlines = [SalesContractInlinePosition, SalesContractPostalAddress, SalesContractPhoneAddress, SalesContractEmailAddress]

   def recalculatePrices(self, request, queryset):
      for obj in queryset:
         obj.recalculatePrices(date.today().__str__())
   recalculatePrices.short_description = _("Recalculate Prices")
   actions = ['recalculatePrices']


class OptionQuote(admin.ModelAdmin):
   list_display = ('contract', 'id', 'customer', 'validuntil', 'state', 'staff', 'lastmodification', 'lastmodifiedby')
   list_display_links = ('contract','customer')
   fieldsets = (
      (_('Basics'), {
         'fields': ('contract', 'customer', 'validuntil', 'state')
      }),
      (_('Advanced (not editable)'), {
         'classes': ('collapse',),
         'fields': ('lastPricingDate', 'lastCalculatedPrice')
      }),
   )
   save_as = True
   inlines = [SalesContractInlinePosition, SalesContractPostalAddress, SalesContractPhoneAddress, SalesContractEmailAddress]

   def recalculatePrices(self, request, queryset):
      for obj in queryset:
         obj.recalculatePrices(date.today().__str__())
   recalculatePrices.short_description = _("Recalculate Prices")

   def createInvoice(self, request, queryset):
      for obj in queryset:
         obj.createInvoice()
   createInvoice.short_description = _("Create Invoice")

   actions = ['recalculatePrices', 'createInvoice']

class OptionPurchaseOrder(admin.ModelAdmin):
   list_display = ('distributor', 'state',)
   list_display_links = ('distributor', 'state')
   fieldsets = (
      (_('Basics'), {
         'fields': ('distributor', 'state', 'externalReference')
      }),
   )
   save_as = True
   inlines = [PurchaseOrderInlinePosition, PurchaseOrderPostalAddress, PurchaseOrderPhoneAddress, PurchaseOrderEmailAddress]

class ProductPrice(admin.TabularInline):
   model = Price
   extra = 1
   classes = ('collapse-open',)
   fieldsets = (
      ('', {
         'fields': ('price', 'validfrom', 'validuntil')
      }),
   )
   allow_add = True

class OptionProduct(admin.ModelAdmin):
   list_display = ('productNumber', 'title',)
   list_display_links = ('productNumber',)
   fieldsets = (
      (_('Basics'), {
         'fields': ('productNumber', 'title', 'description')
      }),)
   inlines = [ProductPrice]
   
class ContactPostalAddress(admin.StackedInline):
   model = PostalAddressForContact
   extra = 1
   classes = ('collapse-open',)
   fieldsets = (
      ('Basics', {
         'fields': ('prename', 'name', 'addressline1', 'addressline2', 'addressline3', 'addressline4', 'zipcode', 'town', 'state', 'country', 'purpose')
      }),
   )
   allow_add = True
   
class ContactPhoneAddress(admin.TabularInline):
   model = PhoneAddressForContact
   extra = 1
   classes = ('collapse-open',)
   fieldsets = (
      ('Basics', {
         'fields': ('phone', 'purpose',)
      }),
   )
   allow_add = True
   
class ContactEmailAddress(admin.TabularInline):
   model = EmailAddressForContact
   extra = 1
   classes = ('collapse-open',)
   fieldsets = (
      ('Basics', {
         'fields': ('email', 'purpose',)
      }),
   )
   allow_add = True

class OptionCustomer(admin.ModelAdmin):
   list_display = ('id', 'name' )
   fieldsets = (('', {'fields': ('name',)}),)
   inlines = [ContactPostalAddress, ContactPhoneAddress, ContactEmailAddress]
   allow_add = True

class OptionDistributor(admin.ModelAdmin):
   list_display = ('id', 'name')
   fieldsets = (('', {'fields': ('name',)}),)
   inlines = [ContactPostalAddress, ContactPhoneAddress, ContactEmailAddress]
   allow_add = True


class OptionShipmentPartner(admin.ModelAdmin):
   list_display = ('id', 'name')
   fieldsets = (('', {'fields': ('name',)}),)
   inlines = [ContactPostalAddress, ContactPhoneAddress, ContactEmailAddress]
   allow_add = True

 
admin.site.register(Customer, OptionCustomer)
admin.site.register(Distributor, OptionDistributor)
admin.site.register(ShipmentPartner, OptionShipmentPartner)
admin.site.register(Quote, OptionQuote)
admin.site.register(Invoice, OptionInvoice)
admin.site.register(Contract, OptionContract)
admin.site.register(PurchaseOrder, OptionPurchaseOrder)
admin.site.register(Product, OptionProduct)
