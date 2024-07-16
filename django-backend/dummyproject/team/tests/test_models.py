"""Tests for the models of the team app."""
import pytest

from dummyproject.utils import mixer

pytestmark = pytest.mark.django_db

class TestMember:
    def test_model(self):
        obj = mixer.blend('team.Member')
        assert obj.pk, (
            'Should create an instance of Member'
        )

    def test_get_member_since_str(self):
        # TODO: implement tests in this single test function that guarantee 100%
        # test coverage for the models.py file
        pass
