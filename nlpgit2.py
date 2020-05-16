promptMessage = """
أدخل أيَ كلمة لتعرف هل هي جمع مذكر سالم: 
\n اكتبْ أغلق لتنهي البرنامج
"""


def isJam3MothakarSalem(message):
    if "ون" in message:
        return True
    else:
        return False


if __name__ == "__main__":


    while True:
        sentence = input(promptMessage)

        if isJam3MothakarSalem(sentence):
            print(sentence + " جمع مذكر سالم")
        elif sentence == "أغلق":
            break
        else:  # not jam3 mothakar salem or close
            print(sentence + " لا يوجد جمع مذكر سالم")



