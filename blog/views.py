# ViewSet -> WebAPIの本体。
# RestAPIのCRUD操作に対応する６種類のアクション（メソッド）が事前に用意されており、必要な部分をオーバーライドして使う。

# ModelViewSet -> ViewSetの拡張クラス。
# 特定のmodelを指定すると、modelのCRUD操作がViewSetのアクションとして暗黙的に実装される

# ViewSet は MVC2 におけるコントローラーの役割を担うもの。
# なお、ViewSet というのは DRF における名前であり、Django 的に言えば View です(ViewSet は View を継承)。
# Model をどのようにシリアライズするかを決めるのは Serializer の役目。

# queryset -> ソースとなるデータをクエリで指定
# serializer_class -> シリアライザの指定

from django.shortcuts import render
from rest_framework import viewsets, filters

from .models import User, Entry
from .serializer import UserSerializer, EntrySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    # APIの後ろに ?author = 1 のようにつければUserのid = 1が書いた記事のみが取れる。
    # APIの後ろに ?status = public のようにすれば公開のステータスの記事のみが取れる。
    filter_fields = ('author', 'status')
