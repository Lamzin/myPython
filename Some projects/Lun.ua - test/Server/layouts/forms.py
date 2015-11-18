from django import forms


class UploadFileForm(forms.Form):
    # title = forms.CharField()
    # cover = forms.ImageField()
    # image_title = forms.CharField()
    image_file = forms.FileField(
        label='Select a file',
    )