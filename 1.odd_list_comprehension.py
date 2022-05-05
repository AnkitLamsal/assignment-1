from typing import List
list_a = [1,2,3,4,5,6]
list_b = [10,20,30,40,50,60]

def odd_index_comprehension(lista:List, listb:List)->List:
    """Appends Content of Second List (listb) with  odd index to the first list (lista)

    Args:
        lista (List): List which will append the odd indices content of 'listb'. 
        listb (List): List whose odd index content is appended to 'lista'.

    Returns:
        List: returns lista with appended content of listb.
    """
    [lista.append(listb[i+1]) for i in range(0,len(listb),2)]
    return lista

list_a = odd_index_comprehension(list_a,list_b)
print(list_a)
        