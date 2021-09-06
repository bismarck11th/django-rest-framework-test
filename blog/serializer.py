# Serializer はModelとAPI のデータ(json なと)間での相互変換を受け持つものであり、
# モデルを API のデータに変換したり、逆に API のデータをモデルに変換したりする。
# Serializer とURL は関係ない。

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
