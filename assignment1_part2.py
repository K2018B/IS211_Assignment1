#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment Part 2"""


class Book(object):
    """A printed work book with defination of title and author"""

    author = " "

    title = " "

    def __init__(self, author, title):
        """Constructor for the Book() class.
        Args:
            author (str): The author of the book
            title (str): The title of the book
        Attributes:
            author (str): The author of the book
            title (str): The title of the book
        """
        self.author = author
        self.title = title

    def display(self):
        """Displays the book title and author"""

        bookinfo = '"{}, written by {}"'.format(self.title, self.author)
        print bookinfo

BOOK_1 = Book('John Steinbeck', 'Of Mice and Men')

BOOK_2 = Book('Harper Lee', 'To Kill a Mockingbird')

BOOK_1.display()
BOOK_2.display()
