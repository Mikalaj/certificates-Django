from django.db import models
from django.utils.translation import ugettext as _


# Create your models here.

# class Dignity(models.Model):
#     name = models.CharField(verbose_name=_('Сан'), max_length=100, default="")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = _("Сан святара")
#         verbose_name_plural = _("Святарскія саны")


#
class Clergy(models.Model):
    DIGNITIES = (
        ('IE', _('іярэй')),
        ('PR', _('протаярэй')),
    )
    dignity = models.CharField(verbose_name=_('Сан'), max_length=2, choices=DIGNITIES, default='IE')
    name = models.CharField(verbose_name=_("Імя святара"), max_length=100, default="")

    def __str__(self):
        dignity_name = ''
        for (key, value) in self.DIGNITIES:
            if key == self.dignity:
                dignity_name = value
                break
        return "{} {}".format(dignity_name, self.name)

    class Meta:
        verbose_name = _("Святар")
        verbose_name_plural = _("Святары")
        unique_together = ('dignity', 'name')


# Parent general abstract class of certificates for Certificates of Baptism and Wedding
class Certificate(models.Model):
    class Meta:
        abstract = True
        ordering = ["-date"]

    date = models.DateField(verbose_name=_('Дата'))
    number = models.IntegerField(verbose_name=_('Нумар'), unique=True)
    priest = models.ForeignKey(Clergy, verbose_name=_('Святар'), on_delete=models.CASCADE)
    certificate = models.FileField(verbose_name=_('Файл пасведчання'), upload_to='certificates/%Y/%m/%d/',
                                   blank=True, null=True, unique=True)


class Baptism(Certificate):
    baptized_name = models.CharField(verbose_name=_("Імя ахрышчанага"), max_length=30)
    baptized_middle_name = models.CharField(verbose_name=_("Імя па бацьку ахрышчанага"), max_length=30, default='',
                                            blank=True)
    baptized_surname = models.CharField(verbose_name=_("Прозвішча ахрышчанага"), max_length=30)
    godfather = models.CharField(verbose_name=_("Хросны бацька"), max_length=100, null=True, blank=True)
    godmother = models.CharField(verbose_name=_("Хросная маці"), max_length=100, null=True, blank=True)
    saint_name = models.CharField(verbose_name=_("Імя святога"), max_length=300, null=True, blank=True)
    saint_date = models.DateField(verbose_name=_("Дзень Анёла"), null=True, blank=True)

    def __str__(self):
        return "{} {} {}".format(self.baptized_name,
                                 self.baptized_middle_name,
                                 self.baptized_surname)

    class Meta:
        verbose_name = _("Хрышчэнне")
        verbose_name_plural = _("Хрышчэнні")
        unique_together = ('baptized_name', 'baptized_middle_name', 'baptized_surname')
        ordering = ["-date"]


class Wedding(Certificate):
    fiance_name = models.CharField(verbose_name=_("Імя жаніха"), max_length=30)
    fiance_middle_name = models.CharField(verbose_name=_("Імя па бацьку жаніха"), max_length=30, default='', blank=True)
    fiance_surname = models.CharField(verbose_name=_("Прозвішча жаніха"), max_length=30)
    fiancee_name = models.CharField(verbose_name=_("Імя нявесты"), max_length=30)
    fiancee_middle_name = models.CharField(verbose_name=_("Імя па бацьку нявесты"), max_length=30, default='',
                                           blank=True)
    fiancee_surname = models.CharField(verbose_name=_("Прозвішча нявесты"), max_length=30)
    witness1 = models.CharField(verbose_name=_("Сведка №1"), max_length=100, null=True)
    witness2 = models.CharField(verbose_name=_("Сведка №2"), max_length=100, null=True)

    def __str__(self):
        return "{} {} {} і {} {} {}".format(self.fiance_name,
                                            self.fiance_middle_name,
                                            self.fiance_surname,
                                            self.fiancee_name,
                                            self.fiancee_middle_name,
                                            self.fiancee_surname)

    class Meta:
        verbose_name = _("Вянчанне")
        verbose_name_plural = _("Вянчанні")
        unique_together = (
            'fiance_name', 'fiance_middle_name', 'fiance_surname',
            'fiancee_name', 'fiancee_middle_name', 'fiancee_surname')
