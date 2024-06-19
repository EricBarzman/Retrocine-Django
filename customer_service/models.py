from django.db import models


class Topic(models.Model):
    label = models.CharField(max_length=255)
    label_text = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.label


class Issue_Message(models.Model):
    email = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, related_name='messages', on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.content