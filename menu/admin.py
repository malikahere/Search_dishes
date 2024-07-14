from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ['name', 'location', 'items']  # Enable searching by name, location, and items
    list_display = ['restaurant_name', 'location', 'aggregate_rating_display', 'menu', 'view_details']  # Display fields in the list view
    ordering = ['-full_details__user_rating__aggregate_rating']  # Order by aggregate rating in descending order
    change_list_template = 'admin/menu/restaurant/change_list.html'
    
    def restaurant_name(self, obj):
        return obj.name

    restaurant_name.short_description = 'Restaurant Name'

    def aggregate_rating_display(self, obj):
        return obj.aggregate_rating() 

    aggregate_rating_display.short_description = 'Aggregate Rating'
    
    def menu(self, obj):
        items_list = [f'{item}: {price}' for item, price in obj.items.items()]
        return ', '.join(items_list)

    menu.short_description = 'Menu (Items)'
    
    def view_details(self, obj):
        url = reverse('admin:menu_restaurant_change', args=[obj.pk])
        return format_html(f'<a href="{url}">View Details</a>')

    view_details.short_description = 'Details'

admin.site.register(Restaurant, RestaurantAdmin)




