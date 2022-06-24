import requests
import json

link=requests.get('http://saral.navgurukul.org/api/courses')
url_text=link.text
# print(url_text)
json_file=json.loads(url_text)

with open('courses_1.json','w') as file:
    json.dump(json_file,file,indent=4)

for key in json_file:
    # print(key)
    # #if key=='availableCourses':
    i=0
    while i<len(json_file[key]):
        # print(json_file[key][i])
        # #for key_3 in json_file[key][i]:
        print(i+1,'.',end='')
        print(json_file[key][i]['name'],end='')
        print(json_file[key][i]['id'])
        i+=1

course_no=int(input('enter the course no.: '))
print(course_no,json_file['availableCourses'][course_no-1]['name'],json_file['availableCourses'][course_no-1]['id'])
course_id=json_file['availableCourses'][course_no-1]['id']
# print(json_file['availableCourses'][course_no-1]['id'])

url_2=requests.get('http://saral.navgurukul.org/api/courses/'+str(course_id)+'/exercises')
# print(url_2.status_code)
json_file_2=json.loads(url_2.text)

with open('parentExercise.json','w') as file_2:
    json.dump(json_file_2,file_2,indent=6)

# if course_id==parent_








# print(course_id)
# j=0
# list1=[]
# list2=[]
# for item in json_file_2:
#     # print(item)
    
#     if item[j]['parent_exercise_id']==None:
        
        

#         list1.append(item['course']['exercises'])
#         list2.append(item['course']['exercises'])

#     if item[j]['id']==item[j]['parent_exercise_id']:
#         print(j+1,'.',item[j]['name'])
#         list1.append(item['course']['exercises'])
        

#     elif item[j]['id']!=item[j]['parent_exercise_id']:
#         print(j+1,'.',item[j]['name'])
#         list2.append(item)
#     j+=1
















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














# #with open('')

# import requests


# url=requests.get('http://saral.navgurukul.org/api/courses/195/exercises')
# print(url.text)
