from django.db import models

class UserSubmission(models.Model):
    name = models.CharField(max_length=100)
    pdf_file = models.BinaryField()
    

    def __str__(self):
        return self.name
        
    
