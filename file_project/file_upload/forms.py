from django import forms
from .models import File


class FileUploadForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    upload_method = forms.CharField(label='Upload Method', max_length=20,
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_file(self):
        file = self.cleaned_data['file']
        ext = file.name.split('.')[-1].lower()
        if ext not in ['jpg', 'pdf', 'xlsx','png']:
            raise forms.ValidationError('Only jpq,pdf and xlsx files are allowed.')
        return file

class FileUploadModelForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('file','upload_method',)

        widgets = {
            'upload_method': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

        def clean_file(self):
            file = self.cleaned_data['file']
            ext = file.name.split('.')[-1].lower()
            if ext not in ['jpq','py','pdf']:
                raise forms.ValidationError('only jpq')
            return file