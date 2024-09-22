from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
    

    def __str__(self):
        return self.username
    
class CustomUser(AbstractUser):
    following = models.ManyToManyField(
        'self', 
        through='UserFollow', 
        related_name='followers',
        symmetrical=False
    )

    def __str__(self):
        return self.username

class UserFollow(models.Model):
    user = models.ForeignKey(CustomUser, related_name='following_set', on_delete=models.CASCADE)
    followed_user = models.ForeignKey(CustomUser, related_name='followers_set', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'followed_user')

    def __str__(self):
        return f'{self.user} follows {self.followed_user}'

    
    

