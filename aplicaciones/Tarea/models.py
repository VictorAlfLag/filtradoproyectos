from django.db import models

# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField()  
    version = models.CharField(max_length=50) 
    image = models.ImageField(upload_to='technologies/', null=True, blank=True)  
    creation_date = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Technologies"

class Category(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    
    name = models.CharField(max_length=100)  
    description = models.TextField()  
    creation_date = models.DateTimeField(auto_now_add=True)  
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='active') 
    icon = models.ImageField(upload_to='categories/', null=True, blank=True) 

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Categories"  

class Tag(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()  
    creation_date = models.DateTimeField(auto_now_add=True)  
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='active')
    code = models.CharField(max_length=100, null=True, blank=True)  

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Tags"  

class Project(models.Model):
    name = models.CharField(max_length=200)  
    description = models.TextField() 
    start_date = models.DateField()  
    end_date = models.DateField()  
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects')  
    tags = models.ManyToManyField(Tag, related_name='projects') 
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='projects')  

    def __str__(self):
        return self.name
    class Meta:
        db_table = "Projects" 
        