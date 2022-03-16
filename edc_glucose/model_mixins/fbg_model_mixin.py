from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from edc_constants.constants import NOT_APPLICABLE
from edc_lab.choices import GLUCOSE_UNITS_NA, RESULT_QUANTIFIER
from edc_lab.constants import EQ

from ..constants import GLUCOSE_HIGH_READING


def fbg_model_mixin_factory(utest_id: str, **kwargs):
    class AbstractModel(models.Model):
        class Meta:
            abstract = True

    opts = {
        f"{utest_id}_value": models.DecimalField(
            verbose_name=format_html("FBG level"),
            max_digits=8,
            decimal_places=2,
            null=True,
            blank=True,
            help_text=f"A `HIGH` reading may be entered as {GLUCOSE_HIGH_READING}",
        ),
        f"{utest_id}_quantifier": models.CharField(
            verbose_name=format_html("FBG quantifier"),
            max_length=10,
            choices=RESULT_QUANTIFIER,
            default=EQ,
        ),
        f"{utest_id}_units": models.CharField(
            verbose_name="FBG units",
            max_length=15,
            choices=GLUCOSE_UNITS_NA,
            default=NOT_APPLICABLE,
        ),
        f"{utest_id}_datetime": models.DateTimeField(
            verbose_name=mark_safe("<u>Time</u> FBG level measured"),
            null=True,
            blank=True,
        ),
    }

    opts.update(**kwargs)

    for name, fld_cls in opts.items():
        AbstractModel.add_to_class(name, fld_cls)

    return AbstractModel


class FbgModelMixin(fbg_model_mixin_factory("fbg"), models.Model):
    """A model mixin of fields for the FBG"""

    # fbg_value = models.DecimalField(
    #     verbose_name=format_html("FBG level"),
    #     max_digits=8,
    #     decimal_places=2,
    #     null=True,
    #     blank=True,
    #     help_text=f"A `HIGH` reading may be entered as {GLUCOSE_HIGH_READING}",
    # )
    #
    # fbg_quantifier = models.CharField(
    #     verbose_name=format_html("FBG quantifier"),
    #     max_length=10,
    #     choices=RESULT_QUANTIFIER,
    #     default=EQ,
    # )
    #
    # fbg_units = models.CharField(
    #     verbose_name="FBG units",
    #     max_length=15,
    #     choices=GLUCOSE_UNITS_NA,
    #     default=NOT_APPLICABLE,
    # )
    #
    # fbg_datetime = models.DateTimeField(
    #     verbose_name=mark_safe("<u>Time</u> FBG level measured"),
    #     null=True,
    #     blank=True,
    # )

    class Meta:
        abstract = True
