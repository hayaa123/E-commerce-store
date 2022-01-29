from email.policy import default
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel ,TreeForeignKey

class Category(MPTTModel):
    """
    category table implemented with mptt
    """

    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text= _("Requierd and unique"),
        max_length=255,
        unique=True,
    )

    slug = models.SlugField(
        verbose_name=_("Category safe url"),
        max_length=255,
        unique=True
        )

    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("store:category_list",args=[self.slug])

    def __str__(self):
        return self.name

class ProductType(models.Model):
    """
    Product type table this table will give us all 
    product types that are for sale  
    """
    name = models.CharField(
        verbose_name = _("Product Name")
        ,help_text=_("Required"),
        max_length=225)

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")
        
    def __str__(self) :
        return self.name

class ProductSpecification(models.Model):
    """
    product specification table contains 
    specifications for each category
    """

    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.RESTRICT)

    name = models.CharField(
        verbose_name = _("Name"),
        help_text = _("Required"),
        max_length=225)

    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Spesifications")
        
    def __str__(self) :
        return self.name

class Product(models.Model) :
    """
    the products table
    """
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.RESTRICT)

    category = models.ForeignKey(Category , on_delete=models.RESTRICT) 
    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("Required"),
        max_length=255,
    )

    description = models.TextField(
        verbose_name=_("description"),
        help_text=_("Not required"),
        blank=True)

    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=_("Regular price"),
        help_text=_("Maximum 999.99"),
        max_digits=5,
        decimal_places=2,
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99.")
                }
                }
    )
    decimal_price = models.DecimalField(
        verbose_name=_("Decimal price"),
        help_text=_("Maximum 999.99"),
         error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2
    )
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=True
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created_at"),
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated_at"),
        auto_now=True
    )

    class Meta:
        ordering = _("-created_at"),
        verbose_name =_("Product"),
        verbose_name_plural =_("Products")
    def get_absolute_url(self):
        return reverse("store:product_detail",args=[self.slug])
    def __str__(self):
        self.title

class ProductSpecificationValue(models.Model):
    """
    the product specificaion value table represebt each of the 
    products individua specification or bespoke features
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(ProductSpecification,on_delete=models.RESTRICT)

    class Meta :
        verbose_name  = _("specification_Value")
        verbose_name_plural = _("specification_Values")

class ProductImage(models.Model):
    """
    the product image table
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="product_image")
    image = models.ImageField(
        verbose_name=_("image"),
        help_text = _("uploade a product image"),
        upload_to = "images/",
        default = "images/default.png",
    )
    alt_text = models.CharField(
        verbose_name =("Alturnative text"),
        help_text=_("lease add alternative text"),
        max_length=255,
        null=True,
        blank=True
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(
        verbose_name=_("Created_at"),
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated_at"),
        auto_now=True
    )
    class Meta :
        verbose_name  = _("Product Image")
        verbose_name_plural = _("Product Images")
