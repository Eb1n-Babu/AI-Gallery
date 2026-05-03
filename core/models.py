from django.db import models

class Prompt(models.Model):
    text = models.TextField(max_length=12000)  # ~2000 words
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prompt {self.id} - {self.text[:50]}..."


class Image(models.Model):
    prompt = models.OneToOneField(Prompt, related_name="image", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/prompts/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} for Prompt {self.prompt.id}"
