from django.db import models
from django.utils.translation import ugettext as _


class Reference(models.Model):
    initials = models.CharField(max_length=50, verbose_name=_('Initials'),
                                null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name=_('Name'),
                            null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True,
                                   verbose_name=_('Description'))

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class CongressmanStatus(Reference):

    class Meta:
        verbose_name = _("Congressman Status")
        verbose_name_plural = _("Congressman Status")


class EventStatus(Reference):

    class Meta:
        verbose_name = _("Event Status")
        verbose_name_plural = _("Event Status")


class EventType(Reference):

    class Meta:
        verbose_name = _("Event Type")
        verbose_name_plural = _("Event Types")


class LegislativeBodyStatus(Reference):

    class Meta:
        verbose_name = _("Legislative Body Status")
        verbose_name_plural = _("Legislative Body Status")


class LegislativeBodyType(Reference):

    class Meta:
        verbose_name = _("Legislative Body Type")
        verbose_name_plural = _("Legislative Body Types")


class PropositionStatus(Reference):

    class Meta:
        verbose_name = _("Proposition Status")
        verbose_name_plural = _("Proposition Status")


class PropositionType(Reference):

    class Meta:
        verbose_name = _("Proposition Type")
        verbose_name_plural = _("Proposition Types")


class State(Reference):

    class Meta:
        verbose_name = _("State")
        verbose_name_plural = _("States")


class Legislature(models.Model):

    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = _("Legislature")
        verbose_name_plural = _("Legislatures")

    def __str__(self):
        return self.id


class LegislativeBody(models.Model):

    initials = models.CharField(max_length=50)
    name = models.CharField(max_length=150)
    legislative_body_type = models.ForeignKey(
        LegislativeBodyType, related_name='legislative_bodies')

    class Meta:
        verbose_name = _("Legislative Body")
        verbose_name_plural = _("Legislative Bodies")

    def __str__(self):
        return self.initials


class Party(models.Model):

    name = models.CharField(max_length=150)
    initials = models.CharField(max_length=50)

    class Meta:
        verbose_name = _("Party")
        verbose_name_plural = _("Parties")

    def __str__(self):
        return self.initials


class Congressman(models.Model):

    name = models.CharField(max_length=150)
    photo_url = models.CharField(max_length=255)
    party = models.ForeignKey(Party, related_name='congressmen')
    state = models.ForeignKey(State, related_name='congressmen')
    legislature = models.ForeignKey(Legislature, related_name='congressmen')

    class Meta:
        verbose_name = _("Congressman")
        verbose_name_plural = _("Congressmen")

    def __str__(self):
        return '{0} - {1}'.format(self.party.initials, self.name)
