from unittest import TestCase
from app import app

app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class IntegrationTestCase(Testcase):
    """Unit tests."""

    def test_base_route(self):
        with app.test_client() as client:
            