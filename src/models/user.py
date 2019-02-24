from django.db import models

class User(models.Model):

    user_id   = models.AutoField(primary_key=True)
    name      = models.CharField(max_length=200, default="")
    email     = models.EmailField(max_length=200, default="")
    password  = models.CharField(max_length=200, default="")
    salt      = models.CharField(max_length=200, default="")
    created   = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)

    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def save(self, *args, **kwargs):
        return super(User, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.user_id)

    class Meta:
        db_table = 'user'
        app_label = 'src'