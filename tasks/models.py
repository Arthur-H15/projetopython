from django.db import models




class task(models.Model):
    status=(
        ('doing','produzindo'),
        ('done','pronto'),
    )

    title=models.CharField(max_length=300)
    descriçao=models.TextField()
    done=models.CharField(max_length=5 ,choices=status)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

# Create your models here.
