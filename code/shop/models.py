from django import forms
from django.db import models
from django.urls import reverse
from mainapp.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainapp:product_list_by_category', args=[self.slug])

class Product(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/products/%Y/%m/%d')
    is_approved_by_admin = models.BooleanField(default=False)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainapp:product_detail', args=[self.id, self.slug])


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'price', 'quantity', 'image']
        name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product Name', 'class':'form-control'}), required=True)
        category = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), required=True)
        description = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Description", "class":"form-control"}), required=True)
        price = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}), required=True)
        quantity = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}), required=True)
        image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control newattr"}), required=True)

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'category', 'description', 'price', 'quantity', 'image' ]
        name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Product Name', 'class':'form-control'}), required=True)
        slug = forms.SlugField(widget=forms.TextInput(attrs={'placeholder':'Product Slug', 'class':'form-control'}), required=True)
        category = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), required=True)
        description = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Description", "class":"form-control"}), required=True)
        price = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}), required=True)
        quantity = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}), required=True)
        image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control"}), required=True)
