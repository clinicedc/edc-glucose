from django.db import models
from edc_constants.choices import YES_NO
from edc_model.models import hm_validator


class FastingModelMixin(models.Model):
    """A model mixin of fields about fasting.

    Used together with mixins for glucose measurements.
    """

    fasting = models.CharField(
        verbose_name="Has the participant fasted?",
        max_length=15,
        choices=YES_NO,
        null=True,
        blank=False,
    )

    fasting_duration_str = models.CharField(
        verbose_name="How long have they fasted in hours and/or minutes?",
        max_length=8,
        validators=[hm_validator],
        null=True,
        blank=True,
        help_text="Duration of fast. Format is `HHhMMm`. For example 1h23m, 12h7m, etc",
    )

    fasting_duration_minutes = models.IntegerField(
        null=True, help_text="system calculated value"
    )

    class Meta:
        abstract = True
