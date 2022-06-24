import requests
import json

url=requests.get('https://api.merakilearn.org/courses')
# print(url.text)
r=json.loads(url.text)
with open("requts.json","w") as f:
    json.dump(r,f,indent=4)

i=0
while i<len(r):
    print(i+1,r[i]["name"],r[i]["id"])
    i+=1
course_no=int(input("select which course you want display  :"))
print(course_no,r[course_no-1]["name"])
course_id=r[course_no-1]["id"]

url1=requests.get('https://api.merakilearn.org/courses/'+str(course_id)+"/exercises")
r1=json.loads(url1.text)
with open("parent.json","w") as f2:
    json.dump(r1,f2,indent=6)
print(r[course_no-1]['name'],"-",r[course_no-1]["id"])
serial=1
serial1=1
list=[]
list1=[]
n=1




for i in r1["course"]["exercises"]:
    if i["parent_exercise_id"]==None:
        print(serial,i["name"])
        print(" ",serial1,i["slug"])
        serial+=1
        list.append(i)

        list1.append(i)
    elif i["parent_exercise_id"]==i["id"]:
        print(serial,i["name"])
        serial+=1
        list.append(i)
    elif i["parent_exercise_id"]!=i["id"]:
        print(" ",n,i["name"])
        n+=1
        list1.append(i)
t=open("l.json","w")
json.dump(list,t,indent=3)
t=open("l1.json","w")
json.dump(list1,t,indent=3)



parent_id=int(input("enter enter no: "))
serial=1
for i in list1:
    if i["parent_exercise_id"]==i["id"]:
        print(serial,list1[parent_id-1]["name"])
        serial+=1
        break
    else:
        if i["parent_exercise_id"]!=i["id"]:
            print(serial,list1[parent_id-1]["name"])
            print("",list1[parent_id-1]["content"])
            serial+=1
            break











































# import json
# import requests
  
# url=requests.get('https://www.merakilearn.org/')

# convert_json=url.json()

# with open('courses.json','w') as file:
#     json.dump(convert_json,file,indent=4)

# reading=open('courses.json','r')
# read=reading.read()
# data=json.loads(read)
# print(data)







# file=open('courses.txt','w')
# courses_file=json.load()
# # file.write(a)
# b=json.loads(file)
# print(b)

# # a = requests.get('https://w3schools.com/python/demopage.htm')

# # print(a)
# print(a)



# dict={'phy':82,'maths':75,'history':65}
# max=0
# for item in dict:
#     if dict[item]>max:
#         max=dict[item]
#         key=item
# print(key)


# dic={'phy':82,'maths':75,'history':65}
# max = 0
# min=dic['phy']
# for i in dic:
#     if dic[i]>max:
#         max = dic[i]
#         max_key = i
#     if dic[i]<min:
#         min=dic[i]

# print('min = ',min)
# print('max = ',max)
# print(max_key)

