from django.db import models

# Create your models here.


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return "{} ({})".format(self.city, self.code)


# class Flight(models.Model):
#     # provide properties of each flight
#     origin = models.CharField(max_length=64)
#     destination = models.CharField(max_length=64)
#     duration = models.IntegerField()

#     def __str__(self):
#         return "{}: {} to {}".format(self.id, self.origin, self.destination)
class Flight(models.Model):
    # provide properties of each flight
    # related_name provides a wasy of accessing th relationship in the reverse order
    # flight.origin, reverse relationship is airport.related_name, i.e. airport.departures (for origin)
    # and airport.arrivals for destination, given an airport object (will provide all flights that correspond to the origin / destination)
    origin = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return "{}: {} to {}".format(self.id, self.origin, self.destination)
