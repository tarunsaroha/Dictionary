
#  city_population = {
#     "NewYorkCity":8550405,
#     "LosAngeles":3971883, 
#     "Toronto":2731571, 
#     "Chicago":2720546, 
#     "Houston":2296224, 
#     "Montreal":1704694, 
#     "Calgary":1239220, 
#     "Vancouver":631486, 
#     "Boston":667137
# }

# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population))



# student=dict(name= "Ravina",age= 20)
# print(student)




# Dic= {
#  1: 'NAVGURUKUL',
#  2: 'IN',  
#  3:{
#      'A' : 'WELCOME',
#      'B' : 'To', 
#      'C' : 'DHARAMSALA'
#      }
# }
# print(Dic)




# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:{
#         'organisation':'navgurukul','place':'dharamsala'
#         }
#     }
# print(person['gender'])

# print(person[4])

# result = person[4]['place']

# print(result) 





 
# dic= {
#     'Name': 'RAM', 
#     'Age': 17,
#     }

# dic['ORGANIZATION'] = "NAV GURUKUL"

# dic['place'] = 'dharamsala'

# print(dic)




# dic= {
#    'Name': 'RAM',
#    'Age': 17,
#     }
# dic['student']={
#        'id':22, 
#        'place':'dharamsala'
#    }
# print(dic) 


 
# person= {'1': 'RAM', '2': 17,}
# person[3] = 'male'
# print(person) 



# details={
#     'Name': 'RAM',
#      'Age': 17, 
#      'student': {
#       'id': 22,
#       'place': 'dharamsala'
#       }
#      } 
# details['student']['id']=35
# print(details)





# classes ={
#     "room1":  "6th",
#     "room2":  "7th",
#     "room3":  "8th"
#         }
# mydict=classes.copy()
# print(mydict) 





# CAR_DETAILS={
#     "brand": "Ford",
#     "model": "jason",
#     "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS) 

 


 
# person={
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }
# person.popitem()
# print(person)






# states_capitals = {
#   'Gujarat' : 'Gandhinagar',
#   'Maharashtra' : 'Mumbai',
#   'Rajasthan' : 'Jaipur',
#   'Bihar' : 'Patna'
#   }
# for state in states_capitals:
#       print(state)






 
# details ={
#     "name":  "Bijender",
#     "age":  17,
#     "class":  "10th"
#     }
# for x in details.values():
#     print(x) 




# movie ={
#     "name":  "Puli",
#     "hero":  "Vijay",
#     "rating":  7.5
#     }
# for x,y in movie.items():
#     print(x,y)





# meal ={
#     "monday":  "Chole chawal",
#     "sunday":  "Fried rice",
#     "wednesday":  "dosa"
#     }
# print(len(meal))






# fruit = {}

# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1

# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')

# print (len(fruit))
# print(fruit) 




# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age

# print (len(Details["Student"]))






# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12

# sum = 0
# for k in my_dict:
#     sum += my_dict[k]

# print (sum)
# print(my_dict) 



 
 
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print (len(crates[box]))



 
# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec

# rec = {
#     "Name" : "Python", 
#     "Age":"20", 
#     "Addr" : "NJ", 
#     "Country" : "USA"
#     }
# id2 = id(rec)
# print(id1 == id2)




# details={
#     "name":"Shanti",
#     "age":12,
#     "email":"shanti@navgurukul.org",
#     }

# print(details["name"])
# print(details["age"])
# print(details["email"])





# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():    
#     sum=sum+1
# print(sum) 





# c=dict()
# for i in range(1,16):
#     c=i*i
# print(c)  







# details ={
#     "name":  "Bijender",
#     "age":  17,
#     "class":  "10th"
#     }
# for x in details.values():
#     print(x) 







# dict = {"name1":"Rakesh", "name2":"Ramesh", "name3":"Kamalesh"}
# print(dict["name1"])
# print(dict["name2"])
# print(dict["name3"])






# dict = {"name1":"Rakesh", "name2":"Ramesh", "name3":"Kamalesh"}
# dict["name1"] = "Nagesh"

# print(dict["name1"])
# print(dict)






# dict = {"name1":"Rakesh", "name2":"Ramesh", "name3":"Kamalesh"}
# print("Before Changing Key :")
# print(dict)
# dict["name4"] = dict.pop("name1")
# print("After Changing Key :")
# print(dict)






# dict = {"name1":"Rakesh", "name2":"Ramesh", "name3":"Kamalesh"}
# print("Before Changing Key :")
# print(dict)
# dict["name4"] = dict.pop("name1")
# print("After Changing Key :")
# print(dict)





# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)



# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])



# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict.update({"year": 2020}))


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["model"])



# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# x = thisdict.keys()

# print(x) #before the change

# thisdict["color"] = "white"

# print(x) #after the change




# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change 






# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the chang






# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary") 





# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)




# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)






# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict) 






# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)







# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = dict(thisdict)
# print(mydict) 






# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# print(child1,child2,child3,myfamily)








# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# print(child1,child2,child3)





# thistuple = ("apple",)
# print(type(thistuple))
# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))




# thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
# print(thistuple)





# fruit = {}

# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1

# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')

# print (len(fruit))
# print(fruit) 





# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)









# fruit = {}

# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1

# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')

# print (len(fruit))
# print(fruit)



# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age

# print (len(Details["Student"]))




 
 
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12

# sum = 0
# for k in my_dict:
#     sum += my_dict[k]

# print (sum)
# print(my_dict) 




 
 
# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec

# rec = {
#     "Name" : "Python", 
#     "Age":"20", 
#     "Addr" : "NJ", 
#     "Country" : "USA"
#     }
# id2 = id(rec)
# print(id1 == id2)






# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():    
#     sum=sum+1
# print(sum)






# c=dict()
# for i in range(1,16):
#     c=i*i
# print(c) 


   

# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age

# print (len(Details["Student"])) 





 
# my_dict = {}
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12

# sum = 0
# for k in my_dict:
#     sum += my_dict[k]

# print (sum)
# print(my_dict)





# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change 







# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary") 







# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change





# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change 




# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["color"] = "red"

# print(x) #after the change 






# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict) 






# classes ={
#     "room1":  "6th",
#     "room2":  "7th",
#     "room3":  "8th"
#         }
# mydict=classes.copy()
# print(mydict) 





# details={
#     'Name': 'RAM',
#      'Age': 17, 
#      'student': {
#       'id': 22,
#       'place': 'dharamsala'
#       }
#      } 
# details['student']['id']=35
# print(details); 





# CAR_DETAILS={
#     "brand": "Ford",
#     "model": "jason",
#     "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS) 






# states_capitals = {
#   'Gujarat' : 'Gandhinagar',
#   'Maharashtra' : 'Mumbai',
#   'Rajasthan' : 'Jaipur',
#   'Bihar' : 'Patna'
#   }
# for state in states_capitals:
#       print(state)






# movie ={
#     "name":  "Puli",
#     "hero":  "Vijay",
#     "rating":  7.5
#     }
# for x,y in movie.items():
#     print(x,y) 




