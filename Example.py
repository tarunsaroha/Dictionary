# my_dict = {
#     'name': 'John',
#      1: [2, 4, 3]
#     } 
# print(my_dict)





# person={
#     'name':'jack',
#     'age':20,
#     'gender':'male',
#     4:'organisation'}

# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(result)





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







# 
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





# car ={
#     "brand":  "ford",
#     "model":  "mustang",
#     "year":  1964
# }
# if "model" in car:
#     print("Yes, 'model' is one of the keys in the car dictionary.")

# else:
#     print("No, 'model' key dictionary mai nahi hai.")






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




#  person = {
#     'name':'jack',
#     'id':22,
#     'place':'dharamsala'
# }

# del person('place')
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




# meal ={
#     "monday":  "Chole chawal",
#     "sunday":  "Fried rice",
#     "wednesday":  "dosa"
#     }
# print(len(meal))




# a = {(1,2):1,(2,3):2}
# print(a[1,2])





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






# city_population = {
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






# i = 1
# while(i <= 10):
#     if(i == 5):
#          print("Skipped Element :", i)
#          continue
#     print(i) 








# counter = 0
# string = "navgurukul"
# while (counter < len(string)):
#     counter += 1

#     if string[counter] == "a":
#         continue

#     if string[counter] == "u":
#         continue

#     print(string[counter])

# print("The end", string[counter])



# data  = {'Name' : 'Danish Ali' , 'Age' : 17 }

# print(data['Name'])
# print(data['Age'])





# data  = {'Name' : 'Danish Ali' , 'Age' : 17 }

# remove_pop = data.pop('Age')

# print('Remove Data Using Pop Function is {} '.format(remove_pop))





# data  = {'Name' : 'Danish Ali' , 'Age' : 17 }
# get_data = data.get('Name')
# print(get_data)





# data  = {'Name' : 'Danish Ali' , 'Age' : 17 }
# data.clear()
# print(data)





# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)





# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)








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
#    'Name': 'RAM',
#    'Age': 17,
#     }
# dic['student']={
#        'id':22, 
#        'place':'dharamsala'
#    }
# print(dic) 




# counter = 1
# while counter < 100:
#     if counter % 2 == 0:
#         print(counter)
#     counter = counter + 1 





# print ("NavGurukul")

# def say_hello():
#     print ("Hello!")
#     print ("Aap kaise ho?")

# say_hello()
# print ("Python is awesome")
# say_hello()
# print ("Hello…")
# say_hello() 





# def definition_say_hello():
#     print ("NavGurukul")
#     print ("NavGurukul mei humein apni learning ki responsibility leni padti hai.")

# definition_say_hello()


