# Semester evaluator
# Author: Kevin Wong
# 6 November 2023

# Greet the User
print("Hi my friend how are you? I shall be evaluating your semester.")

# Ask the questions

courses_taking = int(input(f"How many courses are you taking?"))
 
courses_num=0

for courses in range(courses_taking):
    courses_num += int(input(f"How do you rate course {courses} out of 5?"))

# Average rating
if courses_num/courses_taking <= 1:
    print(f"{courses_num/courses_taking}? Wow thats horrible")

elif 1<courses_num/courses_taking <3:
    print(f"{courses_num/courses_taking}? Not a bad semeseter")

else:
    print(f"{courses_num/courses_taking}? Glad to hear that!") 
