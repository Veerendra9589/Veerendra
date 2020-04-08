
print("                  -: THE STUDENT RECOMMENDER SYSTEM :-")
print("This recommender system recommends to the students for their study."
      "What should they have to study for prepration dor exam.In this program students"
      "will enter their numbers in the basis of numbers it will provides that in which subject"
      "they have to more fouce.")
print("Enter how many subect you have")
x=int(input())
list1 = []
print("Enter your subjects")
for i in range (x):
    s=input()
    list1.append(s)
print(list1)
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
count =0
for i in range (x):
    print("Enter the marks of ",list1[count])
    
    print("CA1 MARKS")
    t=int(input())
    list2.append(t)
    
    print("CA2 MARKS")
    t=int(input())
    list3.append(t)
    
    print("CA3 MARKS")
    t=int(input())
    list4.append(t)
    
    print("MET MARKS")
    u=int(input())
    list5.append(u//2+1)

    list6.append(list2[count])
    list6.append(list3[count])
    list6.append(list4[count])
    total_marks_casum=(sum(list6))
    total_marks_camin= min(list6)
    total_marks_cataken=total_marks_casum-total_marks_camin
    marks_ca = 25*(total_marks_cataken/60)
    list7.append(marks_ca)
    list6.clear()
    count=count+1
    
count1=0
for i in range (x):
    if list7[count1]<=10 and list5[count1]<=10 :
        print("You are bellow avg so you have to work hard on this ",list1[count1],"subject")
        
    if list7[count1]<10 and list5[count1]>10 and list5[count1]<=15:
        print("You shoud work hard for this ",list1[count1],"subject. you can do better.")
    if list7[count1]<10 and list5[count1]>15:
        print("you can work hard for this ", list1[count1],"subject . you can improve your marks.")
    if list7[count1]>10 and list5[count1]<=10: 
        print("you are not too good in this ",list1[count1],"subject. you should do more focus.")
    if list7[count1]>10 and list5[count1]>10 and list5[count1]<=15:
        print("this is good for you.Do more effort to incress your marks in this ",list1[count1],"subject")
    if list7[count1]>10 and list5[count1]>15:
        print("your command on this ", list1[count1], "subject. if you will do little more effort"
              " you can get very good marks.")

    count1=count1+1        
