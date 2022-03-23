#!/bin/bash

celery -A checkmate worker --beat --scheduler django_celery_beat.schedulers.DatabaseScheduler -l info