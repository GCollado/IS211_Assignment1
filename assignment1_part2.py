#!/usr/bin/env python
#! -*- coding: utf-8 -*-
"""Class that creates instances containing the book title and author. Includes
 functions that displays the book title and author.
"""


class Book():
    def __init__(self, author, title):
        self.author = author
        self.title = title


    def get_author(self):
        return self.author


    def get_title(self):
        return self.title


    def display(self):
        print("'{}' written by {}".format(self.get_title(), self.get_author()))


if __name__ == "__main__":
    Book('John Steinbeck', 'Of Mice and Men').display()
    Book('Harper Lee', 'To Kill a Mockingbird').display()