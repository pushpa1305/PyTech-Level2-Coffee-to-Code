LIBRARY MANAGEMENT SYSTEM
----------------------------------------------------------------
PROBLEM CHOSEN:

 --Library Management System is choosen.
 --Managing a library manually can be time-consuming and error-prone.
 --This project solves the problem by providing a command-line based Library Management System that allows users to:

Add new books,,
Issue books to students,,
Return issued books,,
Delete books,,
View all available books

The system ensures proper tracking of issued and returned books using a structured text file.
------------------------------------------------------------------
DATASET SOURCE:
 
  --The project uses a local text file (data.txt) as the dataset to store book records.

Each record contains:
Book ID||
Title||
Author|| 
Issued To (student name if issued)||
Return Status||


The file is automatically created and updated by the program if it does not exist.
-------------------------------------------------------------------
HOW TO RUN THE PROJECT:

Make sure Python is installed, then run:
py main.py

You will see:
===== Library Management System =====
1. Add Book
2. Issue Book
3. Return Book
4. Delete Book
5. View Available Books
6. Exit

Enter the number corresponding to the operation you want.

