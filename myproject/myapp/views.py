from django.shortcuts import render
from .forms import UserSubmissionForm
from .models import UserSubmission
def main(request):
    return render(request,'main.html')
def submit_view(request):
    if request.method == 'POST':
        form = UserSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            pdf_file = form.cleaned_data['pdf_file']
            pdf_content = pdf_file.read()
            UserSubmission.objects.create(name=name, pdf_file=pdf_content)
            return render(request, 'success.html', {'name': name})  # Отображаем страницу успеха
    else:
        form = UserSubmissionForm()
    return render(request, 'submit_form.html', {'form': form})
def main_sec(request):
    return render(request,'2main.html')