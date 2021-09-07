# Serializer -> オブジェクトとJSON(XML)間の変換ルールやバリデーション処理を定義する。

# ModelSerializer -> Serializerの拡張クラス。
# 特定のmodelを指定すると、modelのフィールド設定が、Serializerのフィールド設定として暗黙的に実装される


from rest_framework import serializers

from .models import User, Entry


# fieldsに与えるのはAPIとして出力したいフィールド名のタプル
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')


class EntrySerializer(serializers.ModelSerializer):
    # authorのserializerを上書き
    author = UserSerializer()

    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author')
