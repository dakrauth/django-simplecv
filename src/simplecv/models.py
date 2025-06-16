from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CVManager(models.Manager):
    def full_get(self, **kwargs):
        return self.prefetch_related(
            "skills",
            "links",
            "educations",
            "organizations",
            "organizations__positions",
        ).filter(**kwargs)


class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=50, db_index=True)
    full_name = models.CharField(max_length=50)
    summary = models.CharField(max_length=300, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=25, blank=True)
    image = models.CharField(max_length=150, blank=True)
    data = models.JSONField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    objects = CVManager()

    class Meta:
        unique_together = [["user", "label"]]
        ordering = ["-date_updated"]
        get_latest_by = "-date_updated"
        verbose_name = "CV"
        verbose_name_plural = "CV's"

    def __str__(self):
        return f"{self.user}: {self.label}"


class Skill(models.Model):
    category = models.CharField(max_length=20)
    values = models.CharField(max_length=150)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="skills")

    def __str__(self):
        return self.category

    def __iter__(self):
        for val in self.values.split(","):
            yield val.strip()


class Link(models.Model):
    label = models.CharField(max_length=12)
    url = models.URLField()
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="links")

    def __str__(self):
        return self.label


class Education(models.Model):
    institution = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    result = models.CharField(max_length=25, blank=True)
    focus = models.CharField(max_length=25)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="educations")


class Organization(models.Model):
    name = models.CharField(max_length=50)
    previous = models.CharField(max_length=50, blank=True)
    staffed_by = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="organizations")

    class Meta:
        ordering = ["-end_date", "-start_date"]

    def __str__(self):
        return self.name


class Position(models.Model):
    title = models.CharField(max_length=75)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    summary = models.CharField(max_length=500, blank=True)
    achievements = models.TextField(blank=True)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="positions")

    def date_format(self, dt):
        return dt.strftime("%m/%Y").lstrip("0")

    @property
    def started(self):
        return self.date_format(self.start_date or self.org.start_date)

    @property
    def ended(self):
        dt = self.end_date or self.org.end_date
        if not dt:
            return "Present"

        return self.date_format(dt)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return self.title

    @property
    def iter_achievements(self):
        for line in self.achievements.splitlines():
            yield line.strip()
