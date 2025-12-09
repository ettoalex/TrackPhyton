# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44 * 1024 * 1024
amount_of_pages = 100
amount_of_line = 50
amount_of_symbols_in_line = 25
volume_of_symbol = 4
volume_of_symbols_in_line = amount_of_symbols_in_line * volume_of_symbol
volume_of_symbols_on_page = amount_of_line * volume_of_symbols_in_line
volume_of_symbols_in_book = amount_of_pages * volume_of_symbols_on_page
number_of_books = volume // volume_of_symbols_in_book
print("Количество книг, помещающихся на дискету:", int(number_of_books))
