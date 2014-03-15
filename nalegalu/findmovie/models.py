from django.db import models


class MovieEntry (models.Model):
    full_title = models.CharField(max_length=200)
    ipla = models.CharField(max_length=200, blank=True)
    iplex = models.CharField(max_length=200, blank=True)
    tvp = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        service = ""
        if self.ipla:
            service = u"ipla"
        elif self.iplex:
            service = u"iplex"
        elif self.tvp:
            service = u'tvp'
        return self.full_title + " " + service