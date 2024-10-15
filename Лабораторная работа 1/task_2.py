# TODO Найдите количество книг, которое можно разместить на дискете

size = 1.44 * 1024 * 1024
pages = 100
lines = 50
symbols = 25
book = symbols * lines * pages  # книга
book_byte = book * 4
result = round(size / book_byte)
print("Количество книг, помещающихся на дискету:", result)
