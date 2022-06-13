#Gradebook Project

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

subjects = ["Physics", "Calculus", "Poetry", "History"]
grades = [98, 97, 85, 88]
gradebook = [["Physics", 98], ["Calculus", 97],["Poetry",85], ["History", 88]]
gradebook.append(["Computer Science", 100])
gradebook.append(["Visual Arts", 93])
gradebook[-1][-1] = 98
gradebook.remove(["Poetry",85])
gradebook.append(["Poetry", "Pass"])
print(gradebook)

full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)
