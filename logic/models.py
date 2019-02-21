from django.db import models


# Create your models here.
class Faculty(models.Model):
    faculties = (
        ("LE", "Lassonde"),
        ("SC", "Science"),
        ("GL","Glendon"),
    )
    name = models.CharField(max_length=100, choices=faculties, default=("LE", "Lassonde"))

    def __str__(self):
        return self.name


class Course(models.Model):
    langs = (("En", "English"), ("Fr", "French"))

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    credit = models.IntegerField()
    lang = models.CharField(max_length=15, choices=langs, default=("En", "English"))
    about = models.TextField(blank=True)

    def __str__(self):
        if self.nickname:
            return self.nickname
        return self.name + " " + self.code


class Prerequisite(models.Model):
    pre = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="pre")
    post = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="post")
    alt = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.pre.name + " -> " + self.post.name
    def __str__(self):
        return str(self.pk) + " ) " + self.pre.nickname + " ---> " + self.post.nickname


class Program(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(Faculty, models.CASCADE)
    mandatory = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.name
