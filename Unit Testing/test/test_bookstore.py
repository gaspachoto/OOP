import unittest
from unittest import TestCase

from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(100)

    def test_init__raises_error_when_book_limit_below_or_equal_to_zero(self):
        value = -3
        with self.assertRaises(ValueError) as error:
            self.bookstore.books_limit = value
        self.assertEqual(f"Books limit of {value} is not valid", str(error.exception))
        value1 = 0
        with self.assertRaises(ValueError)as error:
            self.bookstore.books_limit = value1
        self.assertEqual(f"Books limit of {value1} is not valid", str(error.exception))

    def test_init_with_correct_data(self):
        book_name = 'Tripwire'
        availability = 10
        books_sold = 20
        bookstore = Bookstore(200)
        bookstore._Bookstore__total_sold_books = books_sold
        bookstore.availability_in_store_by_book_titles = {book_name: availability}
        self.assertEqual(200, bookstore.books_limit)
        self.assertEqual({book_name: availability}, bookstore.availability_in_store_by_book_titles)
        self.assertEqual(books_sold, bookstore._Bookstore__total_sold_books)

    def test_total_sold_books(self):
        books_sold = 20
        bookstore = Bookstore(200)
        bookstore._Bookstore__total_sold_books = books_sold
        self.assertEqual(books_sold, bookstore._Bookstore__total_sold_books)

    def test_len(self):
        bookstore = Bookstore(200)
        book_name1 = 'Tripwire'
        book_name2 = 'Shinning'
        bookstore.receive_book(book_name1, 0)
        self.assertEqual(0, bookstore.availability_in_store_by_book_titles[book_name1])
        bookstore.receive_book(book_name2, 10)
        self.assertEqual(10, bookstore.availability_in_store_by_book_titles[book_name2])
        result = len(bookstore)
        self.assertEqual(10, result)

    def test_receive_books_not_enough_space_raises_error(self):
        book_name = 'Shinning'
        number_of_books = 300
        bookstore = Bookstore(200)
        with self.assertRaises(Exception) as error:
            bookstore.receive_book(book_name, number_of_books)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))

    def test_receive_book_with_just_enough_space(self):
        book_name = 'Shinning'
        number_of_books = 10
        bookstore = Bookstore(10)
        result = bookstore.receive_book(book_name, number_of_books)
        self.assertEqual(number_of_books, len(bookstore))
        self.assertEqual(
            f"{bookstore.availability_in_store_by_book_titles[book_name]} copies of {book_name} are available in the bookstore.", result)
        self.assertTrue(book_name in bookstore.availability_in_store_by_book_titles)

    def test_receive_books_with_enough_space(self):
        book_name = 'Shinning'
        number_of_books = 50
        bookstore = Bookstore(200)
        result = bookstore.receive_book(book_name, number_of_books)
        self.assertTrue(book_name in bookstore.availability_in_store_by_book_titles)
        self.assertEqual(f"{bookstore.availability_in_store_by_book_titles[book_name]} copies of {book_name} are available in the bookstore.", result)
        self.assertEqual(50, bookstore.availability_in_store_by_book_titles[book_name])
        result1 = bookstore.receive_book(book_name, number_of_books)
        self.assertTrue(book_name in bookstore.availability_in_store_by_book_titles)
        self.assertEqual(f"{bookstore.availability_in_store_by_book_titles[book_name]} copies of {book_name} are available in the bookstore.", result1)
        self.assertEqual(100, bookstore.availability_in_store_by_book_titles[book_name])

    def test_sell_book_raises_error_if_doesnt_exist(self):
        book_name = 'Tripwire'
        book_title = 'Shinning'
        availability = 10
        bookstore = Bookstore(200)
        bookstore.availability_in_store_by_book_titles = {book_name: availability}
        with self.assertRaises(Exception) as error:
            bookstore.sell_book(book_title, 10)
        self.assertEqual(f"Book {book_title} doesn't exist!", str(error.exception))

    def test_sell_book_if_there_are_not_enough_copies(self):
        book_title = 'Shinning'
        availability = 10
        bookstore = Bookstore(200)
        bookstore.availability_in_store_by_book_titles = {book_title: availability}
        with self.assertRaises(Exception) as error:
            bookstore.sell_book(book_title, 15)
        self.assertEqual(f"{book_title} has not enough copies to sell. Left: {bookstore.availability_in_store_by_book_titles[book_title]}", str(error.exception))

    def test_sell_book_with_enough_copies(self):
        book_title = 'Shinning'
        availability = 10
        number_of_books = 5
        bookstore = Bookstore(200)
        bookstore.availability_in_store_by_book_titles = {book_title: availability}
        result = bookstore.sell_book(book_title, number_of_books)
        self.assertEqual(f"Sold {number_of_books} copies of {book_title}", result)
        self.assertEqual(number_of_books, bookstore._Bookstore__total_sold_books)
        self.assertEqual(5, bookstore.availability_in_store_by_book_titles[book_title])

    def test_sell_book_with_exact_amount(self):
        book_title = 'Shinning'
        availability = 10
        number_of_books = 10
        bookstore = Bookstore(200)
        bookstore.availability_in_store_by_book_titles = {book_title: availability}
        result = bookstore.sell_book(book_title, number_of_books)
        self.assertEqual(f"Sold {number_of_books} copies of {book_title}", result)
        self.assertEqual(number_of_books, bookstore._Bookstore__total_sold_books)
        self.assertEqual(0, bookstore.availability_in_store_by_book_titles[book_title])
        self.assertEqual(0, len(bookstore))

    def test_str(self):
        book_title = 'Shinning'
        availability = 10
        bookstore = Bookstore(200)
        bookstore.availability_in_store_by_book_titles = {book_title: availability}
        actual_result = str(bookstore)
        expected_result = [f"Total sold books: {bookstore._Bookstore__total_sold_books}"]
        expected_result.append(f'Current availability: {availability}')
        expected_result.append(f" - {book_title}: {availability} copies")
        self.assertEqual('\n'.join(expected_result), actual_result)


if __name__ == '__main__':
    unittest.main()