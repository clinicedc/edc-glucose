#!/usr/bin/env python
import logging
from pathlib import Path

from edc_constants.constants import IGNORE
from edc_test_utils import DefaultTestSettings, func_main

app_name = "edc_glucose"

base_dir = Path(__file__).absolute().parent

project_settings = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    SUBJECT_VISIT_MODEL="edc_visit_tracking.subjectvisit",
    LIST_MODEL_APP_LABEL="edc_glucose",
    EDC_NAVBAR_VERIFY_ON_LOAD=IGNORE,
    EDC_AUTH_SKIP_SITE_AUTHS=True,
    EDC_AUTH_SKIP_AUTH_UPDATER=True,
    EXTRA_INSTALLED_APPS=[
        "edc_glucose.apps.AppConfig",
        "edc_dx.apps.AppConfig",
        "edc_dx_review.apps.AppConfig",
        "visit_schedule_app.apps.AppConfig",
    ],
    EDC_DX_LABELS=dict(dm="Diabetes"),
    EDC_DX_REVIEW_LIST_MODEL_APP_LABEL="edc_glucose",
    add_dashboard_middleware=True,
    add_lab_dashboard_middleware=True,
    use_test_urls=True,
).settings


def main():
    func_main(project_settings, *[f"{app_name}.tests"])


if __name__ == "__main__":
    logging.basicConfig()
    main()
