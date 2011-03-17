from django.forms import ModelForm
from echelon.models import Category, Page, SiteSettings, SiteVariable
from django.forms import HiddenInput, TypedChoiceField

class CategoryForm(ModelForm):

    class Meta:
        model = Category
        exclude = ('order', 'created', 'updated',)

class PageForm(ModelForm):

    class Meta:
        model = Page
        exclude = ('created', 'updated')

class CategoryOrderForm(ModelForm):

    class Meta:
        model = Category
        fields = ['order']
        widgets = {
            'order': HiddenInput(),
        }

class PageOrderForm(ModelForm):

    class Meta:
        model = Page
        fields = ['order']
        widgets = {
            'order': HiddenInput(),
        }

class SiteSettingsForm(ModelForm):

    class Meta:
        model = SiteSettings

class SiteVariableForm(ModelForm):
    # TODO:
    # Fix this. This is nasty. This goes along with how site variables are
    # created and destroyed on the settings_form.html page.
    delete = TypedChoiceField(coerce=bool,
                choices=((True, 'Yes'), ('', 'No')),
                required=False
                )

    class Meta:
        model = SiteVariable
        exclude = ('site',)
