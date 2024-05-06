from django.db import models
from django.utils.text import slugify
import uuid
# Create your models here.





class Category(models.Model):
    name = models.CharField(max_length=120)
    create_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=360)
    slug = models.SlugField(unique=True ,null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quentity = models.IntegerField(default=1)
    regular_price = models.IntegerField(default=1)
    discount_price = models.IntegerField(default=0)
    Product_image = models.ImageField(upload_to='product')
    video_thumbnel = models.ImageField(upload_to='thumbnel', null=True, blank=True)
    video_id = models.CharField(max_length=260, null=True, blank=True)
    is_new = models.BooleanField(default=False)
    product_details = models.TextField()
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) + str(uuid.uuid4())
        super(Product, self).save(*args, **kwargs)
    
    
    def __str__(self) -> str:
        return self.name
    
    
class Order(models.Model):
    customar_name = models.CharField(max_length=260)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    location_area = models.CharField(max_length=200)
    
    
    def __str__(self) -> str:
        return self.customar_name
    
    

