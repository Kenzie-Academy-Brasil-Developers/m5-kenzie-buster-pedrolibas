from django.db import models

class MovieRate(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    MC_17 = "NC-17"

class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(max_length=20, null=True, choices=MovieRate.choices, default=MovieRate.G)
    synopsis = models.TextField(null=True, default=None)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="movies", null=True)
    buyer = models.ManyToManyField("users.User", through="movies.MovieOrder", related_name="purchased_movies", null=True)


class MovieOrder(models.Model):
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name="users_buyers")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_buyer_movies")
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)