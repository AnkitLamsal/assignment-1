from typing import List, Dict

student = ["Ankit", "Lamsal", "Primo", "Ankit", "Primo", "Ankit"]
student_ = ["Ankit", "Lamsal", "Primo"]
marks = [50,60,70]
marks = [70, 45, 51, 91, 10, 20]


def return_index(list_:list)->dict:
    """This function returns the index of the repeated students.

    Args:
        list_ (list): List of Students

    Returns:
        dict: Dictionary having total count of repeition, list of position for each student.
    """    
    counter_dict = {}
    for x in range(len(list_)):
        if(list_[x] not in counter_dict.keys()):
            temp = list()
            counter_dict[list_[x]] = (1, temp+[x])
        else:
            counter, lista = counter_dict[list_[x]]
            counter_dict[list_[x]] = counter+1,lista+[x]
    return counter_dict

def unique_checker(student:list)->dict or list:
    """This function checks whether the list is unique.

    Args:
        student (list): List of Students

    Returns:
        dict or list: Dictionary if Student name is repeated, else returns same list.
    """    
    if(len(student)) != len(set(student)):
        dict_ = return_index(student)
        return dict_
    else:
        return student  

def fill_marks_dict(data:dict, marks:list)->dict:
    """Fills the marks into the repeated students.

    Args:
        data (dict): Dictionary with Students and their count, list of indices.
        marks (list): List of marks.

    Returns:
        dict: Returns Dictionary with list of marks
    """    
    dict_ = dict()
    for key, value in data.items():
        counter, list_ = value
        list_marks = list()
        for i in range(counter):
            # print()
            if(marks[list_[i]]>50):
                list_marks.append(marks[list_[i]])
        if(list_marks):
            dict_[key] = list_marks
    return dict_
            
             

def fill_marks(student:list, marks:list)->dict:
    """This function fills the marks in the data.

    Args:
        student (list): List of students
        marks (list): List of Marks

    Returns:
        dict: Dictionary with key being student and values being marks
    """                
    data = unique_checker(student)
    student_marks = {}
    if(isinstance(data,list)):
        for i in range(len(data)):
            if marks[i] > 50:
                student_marks[student[i]] = marks[i]
        # print(student_marks)
    else:
        student_marks = fill_marks_dict(data, marks)
        # print(student_marks)
    return student_marks

marks_dict_1  = fill_marks(student,marks)
marks_dict_2 = fill_marks(student_,marks)

print(marks_dict_1)
print(marks_dict_2)