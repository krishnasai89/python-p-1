from turtle import*
title('Jai Shree Ram')
bgcolor('black')
pensize(6)
pencolor("orange")
Ram_name =["జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్",
"జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్",
"జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్",
"జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్",
"జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్",
"జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్",
"జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్",
"జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్",
"జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్",
"జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్",
"జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్",
"జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్",
"జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్","జై శ్రీరామ్"]

angle=360/49
penup()
sety(-1)
for i in range(50):
    left(angle)
    forward(260)
    write(Ram_name[i],align="right",font=('Arial',12,"bold"))
    backward(260)