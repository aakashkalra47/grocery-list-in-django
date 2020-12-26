from django import forms
class ItemForm(forms.Form):
    item_name=forms.CharField(max_length=50)
    item_quantity=forms.CharField(max_length=20)
    item_status=forms.CharField(max_length=20)
    addedAt=forms.DateField()
   