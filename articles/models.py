import re
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
# from articles.managers import UserProfileManager

# Create your models here.

ARTICLE_STATUS = (
    ("draft", "draft"),
    ("inprogress", "in progress"),
    ("published", "published"),
)


class UserProfile(AbstractUser):
    pass
    # email = models.EmailField(_("email adress"), max_length=225, unique =True)

    # objects = UserProfileManager()

    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []

    # @property
    # def article_count(self):
    #     return self.articles.count()
    
    # @property
    # def written_words(self):
    #     return self.articles.aggregate(models.Sum("word_count"))["word_count__sum"] or 0

class Article(models.Model):
    
    # class Meta:
    #     verbose_name = _("Article")
    #     verbose_name_plural = _("Article")
    
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, default="")
    word_count = models.IntegerField(blank=True, default="")
    twitter_post = models.TextField(blank=True, default="")
    status = models.CharField(
        max_length=20,
        choices=ARTICLE_STATUS,
        default="draft",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        # verbose_name = _("creator")
        on_delete=models.CASCADE,
        related_name="articles")
    
    def save(self, *args, **kwargs):
        text = re.sub(r"<[^>]*>", "", self.content).replace("&nbsp;", " ")
        self.word_count = len(re.findall(r"\b\w+\b", text))
        super().save(*args, **kwargs)


