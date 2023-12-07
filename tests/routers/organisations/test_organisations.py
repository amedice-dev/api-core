import pytest
from django.test import TestCase
from app.users.models import User
from app.organisations.models import Organisation
from django.db import transaction


@pytest.mark.django_db
class YourTestCase(TestCase):
    @transaction.atomic
    def setUp(self):
        # Ваш код инициализации данных для теста
        pass

    @transaction.atomic
    def tearDown(self):
        # Ваш код очистки данных после теста
        pass
