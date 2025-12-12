student_infor1 = {
    "name": "Deepsa",
    # "age": 65,
    "age": 35,
    "address": {
        "home_address": "BBSR",
        "office_address": "KA"
    }
}

student_infor2 = {
    "name": "Byom",
    # "age": 65,
    "age": 38,
    "address": {
        "home_address": "Sambalpur",
        "office_address": "KA"
    }
}

student_infor3 = {
    "name": "Murthy",
    # "age": 65,
    "age": 120,
    "address": {
        "home_address": "PODI",
        "office_address": "vizag"
    }
}

student_list = [student_infor1,student_infor2,student_infor3]
print(student_list)
print(student_list[2]["address"]["office_address"])