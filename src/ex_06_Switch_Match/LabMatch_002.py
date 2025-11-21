print("Enter the which test you want to run")
test_type = input("Enter the test type:API, UI, Performance, Security ")
match test_type:
    case "API":
        print("We are running a Postman API Test case.")
    case "UI":
        print("We are running a Selenium Test case.")
    case "Performance":
        print("We are running a Performance Test case.")
    case "Security":
        print("We are running a Security Test case.")
    case _:
        print("Invalid Test")

      #  print("Enter which test you want to run")
       # test_type = input("Enter the test type (API, UI, Performance, Security): ").strip().lower()

       # if test_type == "api":
         #   print("We are running a Postman API Test case.")
       # elif test_type == "ui":
          #  print("We are running a Selenium UI Test case.")
       # elif test_type == "performance":
          #  print("We are running a Performance Test case.")
       # elif test_type == "security":
         #   print("We are running a Security Test case.")
       # else:
         #   print("Invalid Test")
# We can write it by using if else condition also.