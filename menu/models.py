from django.db import models

class Restaurant(models.Model):
    restaurant_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    items = models.JSONField()
    full_details = models.JSONField(blank=True, null=True)
    
    def __str__(self):
        return self.name

    def aggregate_rating(self):
        if self.full_details and 'user_rating' in self.full_details:
            return self.full_details['user_rating'].get('aggregate_rating', None)
        return None