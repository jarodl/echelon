from django.db import models

class Category(models.Model):
    """
    * If the CMS was a file system then a `Category` would be a folder
    * Can display a block of formatted text like a Page
    * Stores other `Pages` (or 'files' if viewed as a file system)

    """
    title = models.CharField(max_length=255)
    desc = models.TextField(max_length=140, blank=True)
    content = models.TextField(blank=True)
    parent = models.ForeignKey('self', blank=True, null=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    slug = models.SlugField()
    path = models.CharField(max_length=155, editable=False, unique=True)

    hide_content = models.BooleanField(default=False)
    hide_links = models.BooleanField(default=False)

    order = models.IntegerField(blank=True, null=True)

    @models.permalink
    def get_absolute_url(self):
        """
        Should return the URL to the Category.

        """
        return ('echelon:show_category', [self.path])

    def save(self, *args, **kwargs):
        """
        The path field is used to pretify the urls to a Category. Everytime
        a Category is saved the parents are traversed then their names are
        added to a list and joined by slashes.

        """
        parent = self
        path = list()
        while parent is not None:
            path.insert(0, parent.slug)
            parent = parent.parent
        self.path = '/'.join(path)
        super(Category, self).save(*args, **kwargs)

    def root_category(self):
        """
        Returns the highest level category that this instance belongs in.
        """
        if not self.parent:
            return None
        parent = self.parent
        while parent.parent is not None:
            parent = parent.parent
        return parent

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ('order',)

    def __unicode__(self):
        return self.title

class Page(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=140)
    categories = models.ManyToManyField(Category)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    script = models.TextField(blank=True)

    order = models.IntegerField(blank=True, null=True)

    def root_category(self):
        """
        Returns the highest level category that this page belongs in.

        """
        parent = self.categories.all()[0]
        while parent.parent is not None:
            parent = parent.parent
        return parent

    @models.permalink
    def get_absolute_url(self):
        """
        Should return the URL to the `Page`.

        """
        return('echelon:show_page', [self.id])

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('order',)

class SiteSettings(models.Model):
    global_javascript = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        """
        Overload save to make this class a Singleton.

        """
        SiteSettings.objects.all().delete()
        self.id = 1
        super(SiteSettings, self).save(*args, **kwargs)

class SiteVariable(models.Model):
    name = models.CharField(max_length=20)
    value = models.TextField(blank=False)

    site = models.ForeignKey(SiteSettings)
