from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=50, db_index=True)
    data = models.JSONField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['user', 'label']]
        ordering = ['-date_updated']
        get_latest_by = '-date_updated'
        verbose_name = "CV"
        verbose_name_plural = "CV's"

    def __str__(self):
        return f'{self.user}: {self.label}'
