try:
    age=int(input("enter your age "))
    result=10/age
    print(f"100/{age} result={result}")
except ValueError:
      print("Please enter a valid number")   
except ZeroDivisionError: 
      print("Cannot divide by zero")  
except Exception as e:
      print(f"somthing went wrong: {e}")   

finally:
        print("exectution completed")

