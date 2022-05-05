from typing import List
import json

#  Making List of dictionaries, dictionaries of each books, 
# which contain name, author and published year as keys.

books = [{"name":"Machine Learning", "author": "Ankit Lamsal", "published year": 2002},
         {"name":"Deep Learning", "author": "Andrew NG", "published year": 2010 },
         {"name":"Reinforcement Learning", "author": "Rick Sutton", "published year": 1993 },
         {"name":"Sci-Kit Learn", "author": "Anjit", "published year": 2003},
         {"name":"Tensorflow", "author": "Andrew NG", "published year": 2015 },
         {"name":"Graph Learning", "author": "Mark Zukerburg", "published year": 2021 },
         {"name":"Keras", "author": "Anil", "published year": 2009},
         {"name":"Tf Lite", "author": "Laurence Mooroney", "published year": 2011 },
         {"name":"Graph Approach", "author": "Marc Spector", "published year": 2020 },
         {"name":"Pytorch", "author": "Benedict C.", "published year": 2019 },
         ]

def swap(list_:list, position1:int, position2:int)->list:
    """This function swaps the elements in the

    Args:
        list_ (list): List whose element  swapped
        position1 (int): Swap Position first
        position2 (int): Swap Position second

    Returns:
        list: Returns swapped list.
    """    
    temp = list_[position1]
    list_[position1] = list_[position2]
    list_[position2] = temp
    return list_


def sort(book:list)->list:
    """This function sorts the list of books based on published year. 
    Used Bubble sort in sorting an element of an list. 

    Args:
        book (list): List of Dictionaries, each dictionaries having "name", "author" and "published year" as keys.

    Returns:
        list: Returns the sorted list of books.
    """    
    for i in range(0, len(book)):
        for j in range(0, len(book)-i-1):
            if(book[j]["published year"] > book[j+1]["published year"]):
                book = swap(book, j, j+1)
    return book
    
sorted_books = sort(books)

def write_json(book:list):
    """This function writes the Previously sorted list in JSON format.

    Args:
        book (list): Sorted List.
    """    
    with open ('books_list.json', "w+") as bookwrite:
        bookwrite.write(json.dumps(book))

write_json(sorted_books)
