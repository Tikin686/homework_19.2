from django.core.cache import cache
from config.settings import CACHE_ENABLED
from catalog.models import Product
def get_product_from_cache():
    """
    Получаем данные по продуктам из кэша.(Если кэш пуст, то данные из бд.)
    """
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    product = cache.get(key)
    if product is not None:
        return product
    product = Product.objects.all()
    cache.set(key, product)
    return product
