# TODO Найдите количество книг, которое можно разместить на дискете
bytes = 4
chars = 25
lines = 50
pages = 100

total_size = pages * lines * chars * bytes
diskette_size = disk_size = 1.44 * 1024 * 1024
books_number = int(diskette_size // total_size)

print("Количество книг, помещающихся на дискету:", books_number)
