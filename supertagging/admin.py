from django.contrib import admin
from supertagging.models import SuperTag, SuperTaggedItem, SuperTagRelation, SuperTaggedRelationItem, SuperTagProcessQueue, SuperTagExclude
from django.contrib.contenttypes.models import ContentType


def lock_items(modeladmin, request, queryset):
    queryset.update(locked=True)
lock_items.short_description = "Lock selected Queue Items"

def unlock_items(modeladmin, request, queryset):
    queryset.update(locked=False)
unlock_items.short_description = "Unlock selected Queue Items"


class SuperTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'substitute', 'stype', 'properties' )
    ordering = ('name', )
    search_fields = ('stype', 'name', )
    list_filter = ('stype', )
    
    raw_id_fields = ('substitute',)
    
    
class SuperTaggedItemAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'tag', 'field', 'process_type', 'relevance', 'instances')
    list_filter = ('process_type',)
    search_fields = ('tag__name',)
    
class SuperTaggedRelationItemAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'relation', 'field', 'process_type','instances')  
    list_filter = ('process_type',)
    
    
class SuperTagRelationAdmin(admin.ModelAdmin):
    list_display = ('tag', 'name', 'stype', 'properties')
    ordering = ('tag', )
    search_fields = ('stype', 'name', 'tag')
    list_filter = ('stype', 'name', )
    
    
class SuperTagProcessQueueAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'locked')
    actions = [lock_items, unlock_items]
    
    
class SuperTagExcludeAdmin(admin.ModelAdmin):
    list_display = ('tag',)
    
    raw_id_fields = ('tag',)
    

admin.site.register(SuperTag, SuperTagAdmin)
admin.site.register(SuperTaggedItem, SuperTaggedItemAdmin)
admin.site.register(SuperTagRelation, SuperTagRelationAdmin)
admin.site.register(SuperTaggedRelationItem, SuperTaggedRelationItemAdmin)
admin.site.register(SuperTagProcessQueue, SuperTagProcessQueueAdmin)
admin.site.register(SuperTagExclude, SuperTagExcludeAdmin)
