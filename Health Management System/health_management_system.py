# Parameters for the functions are :- name_of_person, type(food or exercise)

from datetime import date

def add_food(name_of_person, food_item):
    """function for adding food item that he ate to his file"""
    f = open((name_of_person + "_food.txt"), "a+")
    f.write(food_item+str(date_time())+"\n")
    f.close()
    print("Food item added Successfully")
def add_exercise(name_of_person, exercise_type):
    """function for adding exercise he has done in file"""
    f = open((name_of_person + "_exercise.txt"), "a+")
    f.write(exercise_type+str(date_time())+"\n")
    print("Exercise type added Successfully")
    f.close()
def show_food(name_of_person):
    """Function for displaying All food eaten by that person """
    f = open((name_of_person + "_food.txt"), "r")
    print(f.read())
    f.close()
def show_exercise(name_of_person):
    """Function for displaying all exercise done by that person"""
    f = open((name_of_person + "_exercise.txt"), "r")
    print(f.read())
    f.close()

def date_time():
    today=date.today()
    return today.strftime("%d %B, %Y")



while True:
     print ("Health Management System\n")
     a= int(input("Enter choice for User as follows:\n1.Food\n2.Exercise\t"))
     print("You choose "+ str(a)+" option")
     if a == 1:
         z=int(input("What do you wanted to do:\n1.Add food item\n2.See all food items\t"))
         if z == 1:
             a=input("What is your name?")
             b=input("Which food item you have eaten?")
             add_food(a,b)
             continue
         elif z== 2:
             a = input("What is your name?")
             show_food(a)
             continue
         continue
     elif a == 2:
         x=int(input("What do you wanted to do:\n1.Add Exercise type\n2.See all exercise done"))
         if x == 1:
             a=input("What is your name?")
             b=input("What type of exercise have you done?")
             add_exercise(a,b)
             continue
         elif x == 2:
             a = input("What is your name?")
             show_exercise(a)
             continue
         continue