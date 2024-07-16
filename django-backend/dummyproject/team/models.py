"""Models for the team app."""

from django.db import models

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
        # TODO: use relativedelta to compute a string like this based on the
        # date_joined field:
        return '1 year, 10 months, 4 days'