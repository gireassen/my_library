                                                # Основы асинхронности в Python #6: Корутины и yield from
# Корутины или сопрограммы - это генераторы, которые в процессе работы могут принимать из вне данные
# при помощи метода send

def subgen():
    message = yield
    print("Subgen rec: ", message)