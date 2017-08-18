def ages(age):
    age = int(age)
    if age <=13:
        return "primary school"
    elif age <=18:
        return "secondary school"
    else: 
          return "tartiary"
user_input = input("what is the student age?:")
summarised_age = ages(user_input)
print("The student is in {}".format(summarised_age))
