"""Tests for the models of the team app."""
import pytest
from datetime import datetime
from dateutil.relativedelta import relativedelta

from dummyproject.utils import mixer

pytestmark = pytest.mark.django_db

class TestMember:
    def test_model(self):
        obj = mixer.blend('team.Member')
        assert obj.pk, (
            'Should create an instance of Member'
        )

    def test_get_member_since_str(self):
        current_date = datetime.now().date()
        obj = mixer.blend('team.Member', date_joined=current_date)
        date_joined = relativedelta(current_date, current_date)
        expected_str = f'{date_joined.years} years, {date_joined.months} months, {date_joined.days} days'
        assert obj.get_member_since_str() == expected_str, 'Should return correct member since string'

    def test_team_list_view_get(self, client):
        member1 = mixer.blend('team.Member', name='Xuan', image='test.jpg')
        member2 = mixer.blend('team.Member', name='Kim', image='test.jpg')
        member3 = mixer.blend('team.Member', name='Tal', image='test.jpg')
        member4 = mixer.blend('team.Member', name='Pengyu', image='test.jpg')

        response = client.get('/team/')
        assert response.status_code == 200, 'Should return 200 status code'
        assert 'data' in response.json(), 'Response should contain data key'
        data = response.json()['data']
        assert len(data) == 4, 'Should return four members'
        assert data[0]['name'] == member1.name, 'First member should be Xuan'
        assert data[1]['name'] == member2.name, 'Second member should be Kim'
        assert data[2]['name'] == member3.name, 'Third member should be Tal'
        assert data[3]['name'] == member4.name, 'Fourth member should be Pengyu'
