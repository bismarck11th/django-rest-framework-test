# URL Pattern はその名の通り URL と View(ViewSet) を結びつけるもの。
# (リクエストのHTTPメソッドとエンドポイントを判別し、対応するViewSetのアクションを実行する)
# ただし、ここで使用するのはURLのうち PATH だけで、クエリ文字列やドメインは URL Pattern では使用しない。

from rest_framework import routers
from .views import UserViewSet, EntryViewSet

app_name = 'blog'

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('entries', EntryViewSet)
