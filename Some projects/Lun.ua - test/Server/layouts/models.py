from django.db import models

# Create your models here.
class image_result(models.Model):
    def __init__(self, url, result_straightforward, result_bfs):
        self.url = url
        self.default = result_straightforward
        self.bfs = result_bfs
        self.id = url.split("/")[-1].split(".")[0]

    def __str__(self):
        return self.url


class proceed_result(models.Model):
    name = models.CharField(max_length=64)
    proceed_default = models.CharField(max_length=64)
    proceed_bfs = models.CharField(max_length=64)
    url = models.URLField(max_length=128)

    def __unicode__(self):
        return self.name

class image_detail(models.Model):
    def __init__(self, url, ratio):
        self.url = url
        self.ratio = ratio

    def __unicode__(self):
        return self.url