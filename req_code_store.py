from turtle import forward
import requests
import json

link_1=requests.get('https://api.merakilearn.org/courses')
jsonfile1=json.loads(link_1.text)

f1=open('final_1.json','w')
json.dump(jsonfile1,f1,indent=4)

i=0
for item in jsonfile1:
    print(i+1,item['name'],end='  ')
    print(item['id'])
    i+=1

def choose_course():
    serial_no=int(input('Enter the serial no. of desired course:'))
    course_id=jsonfile1[serial_no-1]['id']

    link_2=requests.get('https://api.merakilearn.org/courses/'+str(course_id)+"/exercises")
    jsonfile_2=json.loads(link_2.text)

    f2=open('final_2.json','w')
    json.dump(jsonfile_2,f2,indent=6)

    i=0
    global sr_list
    global list_1
    global list_3
    list_1=[]
    sr_list=[]
    list_3=[]
    for item in jsonfile_2:
        j=0
        k=0
        m=1
        print(i+1,jsonfile_2[item]['name'],end='  ')
        print(jsonfile_2[item]['id'])
        
        for item_2 in jsonfile_2[item]['exercises']:
            if item_2['parent_exercise_id']==None:
                print('  ',j+1,item_2['name'])
                print("     ",item_2['slug'])

                list_1.append(item_2)
                sr_list.append(j+1)
                j+=1
            elif item_2['parent_exercise_id']==item_2['id']:
                # m=1
                # print('      ',m,item_2['name'])
                j+=1
                print('  ',j,item_2['name'])
                print('         ',item_2['slug'])
                list_1.append(item_2)
                sr_list.append(j)
                # m+=1
                # j+=1
                m=1
            #     print(jsonfile_2[item]['exercises'][item_2]['slug'])
            else: 
                print('      ',m,item_2['name'])
                print('        ',item_2['slug'])
                list_3.append(item_2)
                
                m+=1
            # j+=1
            

        i+=1
    # forward_or_backward()
choose_course()
print('sr_list=',sr_list)


def forward_or_backward():
    c=0
    next_or_pre=input("Want to go next or previous,enter 'n' for next and 'p' for previous: ")

    next_or_previous=input("Want to go next or previous,enter 'n' for next and 'p' for previous: ")
    if next_or_previous=='n':
        if c==0:
            pass
        else:
            if next_or_pre == 'p':
                forward_or_backward()
            else:
                subcourses()
        def subcourses():
            # How to and where to add this next_or_pre so that it wo'nt repeate and work correctly. 
            # if next_or_pre=='n':
            choose_subcourse=int(input('enter the subcourse no.:'))
            print(sr_list[choose_subcourse-1],list_1[choose_subcourse-1]['name'])
            if list_1[choose_subcourse-1]['parent_exercise_id']==None:
                print(list_1[choose_subcourse-1]['content'])

                def y_n():
                    next_or_previous=input("Want to go next or previous,enter 'n' for next and 'p' for previous: ")
                    if next_or_previous=='n':
                        print("You are at last position in this series...,so can't move further")
                        subcourses()

                    elif next_or_previous=='p':
                        subcourses()

                    else:
                        print("please read and enter your input correctly in 'y' or 'n' form !")
                        y_n()
                y_n()
            else:
                sr_no=0
                # i=0
                subcourses_list=[]
                for item_3 in list_3:
                    if item_3['parent_exercise_id']==list_1[choose_subcourse-1]['parent_exercise_id']:
                        print(sr_no+1,item_3['name'])
                        subcourses_list.append(item_3)
                        sr_no+=1
                    # i+=1
                for item_3 in list_3:
                    if item_3['parent_exercise_id']==list_1[choose_subcourse-1]['parent_exercise_id']:
                        def N_or_p():
                            n_or_p=input("Want to go next or previous,enter 'n' for next and 'p' for previous respectively: ").lower()
                            
                            if n_or_p=='n':
                                def sub_course():
                                    sub_course_no=int(input("Enter the desired content no. within the subcourse :"))
                                    if sub_course_no<=sr_no:
                                        # if item_3['name']==
                                        # print(item_3['content'])
                                        print(subcourses_list[sub_course_no-1]['content'])
                                        learn_more=input("Do you want to learn more?,enter 'y' or 'n': ").lower()
                                        if learn_more=='y':
                                            N_or_p()
                                        else:
                                            print('Ok, Take rest.')
                                            print('Have a great day!')
                                                # break
                                            # here I want to break/stop my code but using break is giving Syntax error: 'break' outside loop
                                        # added here
                                    else:
                                        print('there is no course available of this serial no.')
                                        sub_course()
                                sub_course()
                            elif n_or_p=='p':
                                # forward_or_backward()
                                subcourses()
                            else:
                                print("please read and enter your input correctly in 'y' or 'n' form !")
                                N_or_p()

                        N_or_p()
            
            # code/curser will never reach at line 143.it will continue it's own looping .
        # elif next_or_pre=='p' :
                # forward_or_backward()           
                        
                               
        subcourses()
    else:
        choose_course()
        forward_or_backward()

forward_or_backward()
# After calling choose_course again ,how to call forward_or_backward() inside choose_course. 
  
  
  



















  
  
                # n_or_p=input("Want to go next or previous,enter 'n' for next and 'p' for previous respectively: ")
                # if n_or_p=='n':
                #     print(item_3[choose_subcourse-1]['content'])
                # else:
                #     # print()
                #     forward_or_backward()

        # if c==0:     
        #     print('here is no subcourses available for this :')
        #     def content():
        #         con=input("Do you want to see content: Enter 'y' or 'n' :  ").lower()
        #         if con=='y':
        #             print(item_3[choose_subcourse-1]['content'])
        #         elif con=='n':
        #             print('ok,as you wish.')
        #         else:
        #             print("please read and enter your input correctly in 'y' or 'n' form !")
        #             content()
        #     content()