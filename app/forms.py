












from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'content']

















# ---Deprecated file---


# ---For Bootstap modal---
# from .models import Category
# from bootstrap_modal_forms.forms import BSModalModelForm

# class BookModelForm(BSModalModelForm):
#     class Meta:
#         model = Category
#         fields = '__all__'

# ---For Popup Library---
# from django import forms
# from .popups import CategoryPopupCRUDViewSet

# from .models import *


# class PostForm(forms.ModelForm):

#     class Meta:
#  	    model = Post
#  	    fields = ['title', 'category']
#  	    widgets = {
#  		    'category': CategoryPopup.get_fk_popup_field()
#  	    }



