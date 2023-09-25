"""KKK"""
from math import ceil as blyad

def books(books_amount, pages_amount, xxx, yyy):
    """blyad"""
    day_used, prev_read = 0, 0
    book_left = books_amount
    read = 0
    for _ in range(books_amount):
        current_day = 0
        book_pages = pages_amount
        while book_pages > 0 and read < pages_amount:
            read = blyad(((xxx + current_day + prev_read) / \
                    (yyy + current_day + prev_read)) * pages_amount)
            book_pages -= read
            current_day += 1
            day_used += 1
        book_left -= 1
        if read >= pages_amount:
            break
        prev_read += current_day
    print(day_used + book_left)
books(int(input()), int(input()), int(input()), int(input()))
