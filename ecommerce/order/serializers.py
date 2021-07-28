from rest_framework import serializers

from .models import Order, OrderItem

from product.serializers import ProductSerializers


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )


class OrderSerializers(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "place",
            "phone",
            "stripe_token",
            "items",
        )

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        print(items_data)
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order


class MyOrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializers()

    class Meta:
        model = OrderItem
        fields = (
            "price",
            "product",
            "quantity",
        )


class MyOrderSerializers(serializers.ModelSerializer):
    items = MyOrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "address",
            "zipcode",
            "place",
            "phone",
            "stripe_token",
            "items",
            # "paid_amount",
        )
