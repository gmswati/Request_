import requests
import json

# link_1=requests.get('https://www.merakilearn.org/courses')
Link_1=requests.get('https://api.merakilearn.org/courses')
Link=Link_1.text
jsonfile1=json.loads(Link)

f1=open('file1.json','w')
json.dump(jsonfile1,f1,indent=4)
# f1.write(jsonfile1)

# print('r')

# my_file=open('file1.json','r')
i=0
# for item in my_file:
# list=[]
for item in jsonfile1:
    print(i+1,item['name'],end='  ')
    print(item['id'])
    # list.append(item['id'])
    i+=1

my_course_id=int(input('Enter the course id: '))
# print(list[my_course_id-1],jsonfile1[my_course_id-1]['name'])
# print(jsonfile1[my_course_id-1]['id'],jsonfile1[my_course_id-1]['name'])
# print(jsonfile1[my_course_id-1]["id"])
course_id=jsonfile1[my_course_id-1]["id"]
Link_2=requests.get('https://api.merakilearn.org/courses/'+str(course_id)+"/exercises")

jsonfile2=json.loads(Link_2.text)

f2=open('file2.json','w')
json.dump(jsonfile2,f2,indent=6)

j=0
for item in jsonfile2:
# ['courses']['exercise']:
    k=0
    # print(jsonfile2[item])
    print(j+1,jsonfile2[item]['name'])

    # print(' ',k+1,item['exercises'][k])
    # ['name'],item['id'])
    # print(item['exercise'][])
    j+=1


