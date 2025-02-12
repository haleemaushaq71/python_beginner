import random
choices=['rock','paper','scissor']

computer_choice=random.choice(choices)
user_choice='paper'


def get_choices():

    choices={"Computer Choice":computer_choice,'User Choice':user_choice}
    return choices

print(get_choices())


def check_age(age):
    return True if age>=18 else False

print(f"The age is verified: {check_age(18)}")

name="Blah"
print(name)
name.lower()
print(name)