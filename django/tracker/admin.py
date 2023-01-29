from django.contrib import admin
from .models import Category, Pair, Cryptocurrency, Trade, ValueBars

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class PairAdmin(admin.ModelAdmin):
    list_display = ('name', 'base_currency', 'quote_currency')

class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')

class TradeAdmin(admin.ModelAdmin):
    list_display = ('pair', 'isBuyerMaker', 'price', 'quantity', 'quoteQty', 'timestamp')

class ValueBarsAdmin(admin.ModelAdmin):
    list_display = ('pair', 'timestamp', 'value_bars')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Pair, PairAdmin)
admin.site.register(Cryptocurrency, CryptocurrencyAdmin)
admin.site.register(Trade, TradeAdmin)
admin.site.register(ValueBars, ValueBarsAdmin)
