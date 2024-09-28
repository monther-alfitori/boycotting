from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=400)
    link = models.URLField()
    source = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']


class Phrase(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Brand(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='images/%y/%m/%d')
    menu = models.FileField(upload_to='files/%y/%m/%d', blank=True)
    number = models.CharField(max_length=400, blank=True)
    location = models.CharField(max_length=500, null=True)


    def __str__(self):
        return self.name



class Social(models.Model):
    SOCIAL_CHOICES = (
        ("Facebook", "Facebook"),
        ("Instagram", "Instagram"),
        ("X", "X"),
        ("Tiktok", "Tiktok"),
    )
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    link = models.URLField()
    platform = models.CharField(max_length=12, choices=SOCIAL_CHOICES, default="Facebook")

    def __str__(self):
        return self.brand.name + ' ' + self.platform



class Share(models.Model):
    SOCIAL_CHOICES = (
        ("Facebook", "Facebook"),
        ("Instagram", "Instagram"),
        ("X", "X"),
        ("Tiktok", "Tiktok"),
    )
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)    
    link = models.CharField(max_length=10000)
    platform = models.CharField(max_length=12, choices=SOCIAL_CHOICES, default="Facebook")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.platform

    class Meta:
        ordering = ['-created_at']



class Company(models.Model):
    TYPE_CHOICES = (
        ("Boycotted", "Boycotted"),
        ("Alternative", "Alternative"),
    )
    logo = models.ImageField(upload_to='images/%y/%m/%d')
    link = models.URLField()
    kind = models.CharField(max_length=12, choices=TYPE_CHOICES, default="Alternative")

    def __str__(self):
        return self.kind + '-' + str(self.id)


class Question(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['id']

