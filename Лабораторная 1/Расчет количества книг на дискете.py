# TODO Найдите количество книг, которое можно разместить на дискете
count_book = 100
count_string = 50
count_symbol = 25
symbol_bytes = 4
book_size = count_symbol * symbol_bytes * count_string * count_book
count_book_of_disc = int(1.44 * 1024 * 1024 // book_size)

print("Количество книг, помещающихся на дискету:", count_book_of_disc)
