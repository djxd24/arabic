
word = ("أدخل أيَ كلمة لتعرف هل هي جمع مذكر سالم: ")
word += "\n اكتبْ أغلق لتنهي البرنامج"

def search():
    if "ون" in message:
        print(message + " جمع مذكر سالم")
    else:
        print("لا يوجد جمع مذكر سالم")

active = True
while active:
    message = input(word)

    if message == "أغلق":
        active = False
    else:
        search()





