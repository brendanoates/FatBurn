__author__ = 'boates'
from django.forms.util import ErrorList

class ParagraphErrorList(ErrorList):
    def __unicode__(self):
        return self.as_paragraphs()

    def as_paragraphs(self):
        return "<p>%s</p>" % (
            ",".join(e for e in self.errors)
        )