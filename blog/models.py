# 「モデルを作る ≒ 管理画面を作る」(+ admin.py)
# 「モデルを作る ≒ CRUD API を作る」(ModelViewSet + Serializer)

from django.db import models


# Create your models here.
class User(models.Model):
    """
    ユーザーモデル
    """
    name = models.CharField(max_length=32)
    mail = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    """
    記事モデル
    """
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
        (STATUS_DRAFT, "下書き"),
        (STATUS_PUBLIC, "公開中"),
    )
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
    author = models.ForeignKey(User, related_name='entries', on_delete=models.CASCADE)
