"""Celery settings for WayToHome project."""

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DevelopsTodayTest.settings")

CELERY_APP = Celery("DevelopsTodayTest", include=["utils.celery_tasks"])
CELERY_APP.config_from_object("django.conf:settings", namespace="CELERY")
