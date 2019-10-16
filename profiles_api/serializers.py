from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    """Serializers a nam field for testing our API view"""

    name = serializers.CharField(max_length=10)