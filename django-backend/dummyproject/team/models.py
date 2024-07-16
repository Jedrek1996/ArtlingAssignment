"""Models for the team app."""

from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Member(models.Model):
    """
    A member of the team.

    :name: String representing the name of the member.
    :image: Filename of the image of the member.
    :date_joined: The date when the member joined the team.
    :bio: String representing a mini-bio of the member.

    """
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    date_joined = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):  # pragma: nocover
        # too trivial to test
        return self.name

    def get_member_since_str(self):
        if not self.date_joined:
            return 'Date Joined'
        current_date = datetime.now().date()
        member_duration = relativedelta(current_date, self.date_joined)
        return f'{member_duration.years} years, {member_duration.months} months, {member_duration.days} days'