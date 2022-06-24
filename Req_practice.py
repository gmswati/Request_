book={}
book['Tom']={'name':'Tom',
                'address':'1 red street,NY',
                'Phone':9877486998}

book['bob']={'name':'bob',
                'address':'1 green street,NY',
                'Phone':9898785456}

import json
s=json.dumps(book)
print(s)
print(type(s))

with open('data_stu.txt','w') as f:
    f.write(s)

book=json.loads(s)
print(book)
print(type(book))