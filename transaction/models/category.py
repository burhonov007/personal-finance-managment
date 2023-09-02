from django.db import models

class Category(models.Model):
    name = models.CharField("name", max_length=255)
    parent_category = models.ForeignKey("self", related_name="children", null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name
