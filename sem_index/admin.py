from django.contrib import admin
from models import (AdminUserInfo,
                    Company,
                    Event,
                    App,
                    Product,
                    CompeteApp,
                    CompeteCompany,
                    CompeteProduct,
                    CompanyInfluenceInfo,
                    SemMonitorCrawlInfo)
# Register your models here.


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_name']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_id', 'company_name']


class EventAdmin(admin.ModelAdmin):
    list_display = ['event_id', 'event_name']
    # pass


class AppAdmin(admin.ModelAdmin):
    list_display = ['app_id', 'app_name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_name']


class CompeteAppAdmin(admin.ModelAdmin):
    list_display = ['compete_app_id', 'compete_app_name']


class CompeteCompanyAdmin(admin.ModelAdmin):
    list_display = ['compete_company_id', 'compete_company_name']


class CompeteProductAdmin(admin.ModelAdmin):
    list_display = ['compete_product_id', 'compete_product_name']


class CompanyInfluenceInfoAdmin(admin.ModelAdmin):
    pass


class SemMonitorCrawlInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'monitor_type_id', 'data_source_type', 'data_source_id']
    ordering = ['id']

admin.site.register(AdminUserInfo, UserInfoAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(App, AppAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CompeteProduct, CompeteProductAdmin)
admin.site.register(CompeteApp, CompeteAppAdmin)
admin.site.register(CompeteCompany, CompeteCompanyAdmin)
admin.site.register(CompanyInfluenceInfo, CompanyInfluenceInfoAdmin)
admin.site.register(SemMonitorCrawlInfo, SemMonitorCrawlInfoAdmin)
