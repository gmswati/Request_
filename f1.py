# import requests
# import json

# link_1=requests.get('https://api.merakilearn.org/courses')
# jsonfile1=json.loads(link_1.text)

# f1=open('final_1.json','w')
# json.dump(jsonfile1,f1,indent=4)

# i=0
# for item in jsonfile1:
#     print(i+1,item['name'],end='  ')
#     print(item['id'])
#     i+=1

# serial_no=int(input('Enter the serial no. of desired course:'))
# course_id=jsonfile1[serial_no-1]['id']

# link_2=requests.get('https://api.merakilearn.org/courses/'+str(course_id)+"/exercises")
# jsonfile_2=json.loads(link_2.text)

# f2=open('final_2.json','w')
# json.dump(jsonfile_2,f2,indent=6)

# i=0
# for item in jsonfile_2:
#     j=0
#     k=0
#     m=1
#     print(i+1,jsonfile_2[item]['name'],end='  ')
#     print(jsonfile_2[item]['id'])
    
#     for item_2 in jsonfile_2[item]['exercises']:
#         if item_2['parent_exercise_id']==None:
#             print('  ',j+1,item_2['name'])
#             print("     ",item_2['slug'])
#             j+=1
#         elif item_2['parent_exercise_id']==item_2['id']:
#             m=1
#             print('      ',m,item_2['name'])
#             print('         ',item_2['slug'])
#             m+=1
#         #     print(jsonfile_2[item]['exercises'][item_2]['slug'])
#         else: 
#             print('      ',m,item_2['name'])
#             print('        ',item_2['slug'])
#             m+=1
#         # j+=1
        

#     i+=1