from django.db import models
from django.urls import reverse


class Post(models.Model):
    """
    A model representing a blog post.

    Attributes:
        title (str): The title of the blog post.
        author (ForeignKey): The author of the blog post.
        body (str): The content of the blog post.
    """

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        """
        Returns a string representation of the blog post.

        Returns:
            str: The title of the blog post.
        """
        return self.title
    
    def get_absolute_url(self):
        """
        Returns the absolute URL of the blog post.

        Returns:
            str: The absolute URL of the blog post.
        """
        return reverse("post_detail", kwargs={"pk": self.pk})