import requests
import json

link=requests.get('http://saral.navgurukul.org/api/courses')
url_text=link.text
# print(url_text)
json_file=json.loads(url_text)

with open('courses_10.json','w') as file:
    json.dump(json_file,file,indent=4)

list_id=[]
for key in json_file:
    # print(key)
    # #if key=='availableCourses':
    i=0
    while i<len(json_file[key]):
        # print(json_file[key][i])
        # #for key_3 in json_file[key][i]:
        print(str(i+1) + '.' ,end='')
        print(json_file[key][i]['name'],end='  ')
        list_id.append(json_file[key][i]['id'])
        print(json_file[key][i]['id'])
        i+=1

course_no=int(input('enter the course no.: '))
# print(course_no,json_file['availableCourses'][course_no-1]['name'],json_file['availableCourses'][course_no-1]['id'])
# course_id=json_file['availableCourses'][course_no-1]['id']
course_new_id=list_id[course_no-1]
url_2=requests.get('http://saral.navgurukul.org/api/courses/'+str(course_new_id)+'/exercises')
json_file_3=json.loads(url_2.text)

with open('myExercise.json','w') as file_3:
        # list.append(json_file_3)
        json.dump(json_file_3,file_3,indent=6)

j=0
for item in json_file_3:
    if item[j]["parent_exercise_id"]=='Null':
        print('given None')
    if course_new_id==item[j]["parent_exercise_id"]:

        print(j+1,item[j]['name'])
        print(item[j]['slug'])
    





    j+=1








# print(json_file['availableCourses'][course_no-1]['id'])

# i=1
# list=[]
# while i<=200:
#     course_id=json_file['availableCourses'][i-1]['id']
#     url_2=requests.get('http://saral.navgurukul.org/api/courses/'+str(course_id)+'/exercises')
#     # print(url_2.status_code)
#     json_file_2=json.loads(url_2.text)

#     with open('myExercise.json','w') as file_2:
#         list.append(json_file_2)
#         json.dump(list,file_2,indent=6)
    
#     i+=1
# # my=open('my_file_view','w')
# # json.loads(list,my,indent=8)










# print(course_id)
# j=0
# for i in json_file_2:
#     print(str(j)+'.',i['course']['exercises']['name'])
    
# #     j+=1



























# list1=[]
# list2=[]
# serial_no=0
# serial=1
# for i in json_file_2['data']['exercises']:
#     if i["parent_exercise_id"]==None:
#         print(serial,i['name'])
#         # serial_no+=1
#         # list1.append(serial)
#         # list2.append(i['name'])
#     # elif i["parent_exercise_id"]==i['id']:
#     #     print(serial,i['name'])
#     #     # list1.append(i["name"])
#     # else:
#     #     print(serial,i['name'])