from django import forms

class UserSubmissionForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя')
    pdf_file = forms.FileField(label='Загрузите PDF файл')

    def clean_pdf_file(self):
        pdf_file = self.cleaned_data.get('pdf_file')
        if pdf_file:
            if pdf_file.content_type != 'application/pdf':
                raise forms.ValidationError('Файл должен быть в формате PDF.')
            if pdf_file.size > 5 * 1024 * 1024:
                raise forms.ValidationError('Размер файла не должен превышать 5MB.')
            return pdf_file
        else:
            raise forms.ValidationError('Необходимо загрузить файл.')
