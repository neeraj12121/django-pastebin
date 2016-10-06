from django.db import models
from django.db.models import permalink
import datetime

class Pastebin(models.Model):
    SYNTAX=(
        (0, "Plain"),
        (1, "Python"),
        (2, "HTML"),
        (3, "SQL"),
        (4, "Javascript"),
        (5, "CSS"),
    )

    content=models.TextField()
    title=models.CharField(blank=True, max_length=40)
    syntax=models.IntegerField(max_length=30,choices=SYNTAX, default=0)
    poster=models.CharField(blank=True, max_length=30)
    timestamp=models.DateTimeField(default=datetime.datetime.now,blank=True)


    class Meta:
        ordering=('-timestamp',)

    def __unicode__(self):
        return "%s (%s)" (self.title or "#%s" %self.id , self.get_syntax_display())

    @permalink
    def get_absolute_url(self):
        return ('django.views.generic.list_detail.object_detail', None, {'object_id':self.id})





