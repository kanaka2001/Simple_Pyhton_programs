def enter_the_marks_of_student(subject1 : int ,subject2 : int , subject3 : int , subject4 : int , subject5 : int) ->float :
    total_marks = subject1 + subject2 + subject3 + subject4 + subject5
    percentage = (total_marks /250) * 100
    
    if (percentage >70):
        print("distingstion")
    elif (percentage >60):
        print(" first class")
    elif (percentage > 35):
        print(" secong class")
    else:
        print("failed")

subject1 = int (input ( "enter the subject1 marks"))
subject2 = int (input ( "enter the subject2 marks"))
subject3 = int (input ( "enter the subject3 marks"))
subject4 = int (input ( "enter the subject4 marks"))
subject5 = int (input ( "enter the subject5 marks"))
enter_the_marks_of_student(subject1,subject2,subject3,subject4,subject5)