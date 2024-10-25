from django.db import models

class WardrobeItem(models.Model):
    CATEGORY_CHOICES = [
        ('top', 'Top'),
        ('bottom', 'Bottom'),
        ('shoes', 'Shoes'),
        ('accessory', 'Accessory'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    color = models.CharField(max_length=50, blank=True)
    tags = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='wardrobe_images/', blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.category})"