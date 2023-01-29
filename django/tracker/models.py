from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField
import pandas as pd

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Cryptocurrency(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='cryptocurrency_icons/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    twitter_account = models.CharField(max_length=255, blank=True, null=True)
    website_link = models.URLField(max_length=255, blank=True, null=True)
    blockchain_link = models.URLField(max_length=255, blank=True)
    mcap = models.DecimalField(max_digits=20, decimal_places=8)
    total_supply = models.DecimalField(max_digits=20, decimal_places=8)
    circulating_supply = models.DecimalField(max_digits=20, decimal_places=8)

    def __str__(self):
        return self.name

class Pair(models.Model):
    base_currency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE, related_name='base')
    quote_currency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE, related_name='quote')
    symbol = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.base_currency.symbol}/{self.quote_currency.symbol}"

class Trade(models.Model):
    tradeId = models.BigIntegerField(unique=True)
    pair = models.ForeignKey(Pair, on_delete=models.CASCADE)
    isBuyerMaker = models.BooleanField()
    isBestPriceMatch = models.BooleanField()
    price = models.DecimalField(max_digits=20, decimal_places=8)
    quantity = models.DecimalField(max_digits=20, decimal_places=8)
    quoteQty = models.DecimalField(max_digits=20, decimal_places=8)
    timestamp = models.DateTimeField()

    @classmethod
    def to_dataframe(cls, queryset):
        data = queryset.values()
        column_labels = ['tradeId', 'pair', 'isBuyerMaker', 'isBestPriceMatch', 'price', 'quantity', 'quoteQty', 'timestamp']
        df = pd.DataFrame.from_records(data, columns=column_labels)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df

    def __str__(self):
        return f"{self.pair.symbol} trade at {self.price} on {self.timestamp}"

class ValueBars(models.Model):
    pair = models.ForeignKey(Pair, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    value_bars = ArrayField(ArrayField(models.DecimalField(max_digits=20, decimal_places=8), size=8), size=60)

    @classmethod
    def to_dataframe(cls, queryset):
        data = queryset.values()
        df = pd.DataFrame.from_records(data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        value_bars_df = pd.DataFrame(df['value_bars'].tolist(), columns=['time', 'open', 'high', 'low', 'close', 'number_of_trades', 'volume', 'isBuyerMaker_by_number', 'isBuyerMaker_by_value'])
        df = pd.concat([df, value_bars_df], axis=1).drop(columns=['value_bars'])
        return df

