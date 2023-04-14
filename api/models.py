from django.db import models


class Joke(models.Model):
    id = models.AutoField(primary_key=True)
    joke = models.TextField()

    def __str__(self):
        return self.joke
