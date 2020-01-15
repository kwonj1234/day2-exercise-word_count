#Dictionary tidbits
our_dict = {"key1" : 12, "key2" : 45.9, "key4" : "string"}

for i in our_dict:
    print(i)

#keys are immutable

print(len(our_dict)) #will give you a list of the keys
print(our_dict["key1"]) #12
#our_dict['key90'] #keyError

print('key90' in our_dict) # to avoid key error, gives a boolean
print(our_dict.get('90', False)) #by default, this will give none. You can change the default by adding False or something.
print(our_dict.keys())
print(our_dict.values())

###########
#list tidbits
our_list = [12,45.9,"string"]
# print(our_list.sort()) #can't sort int and string

last_element = our_list.pop()
print(last_element)

#our_list.append([1,9,100]) #[12,45.9, [1, 9, 100]]
our_list.extend([1,9,100]) #[12, 45.9, 1, 9, 100]

def sample():
    return 3,10
print(sample()) #functions can only return 1 value. All returns are tuples which are single values 
                #that are at the same time more than one value

print(type(3,)) #this is a tuple. A comma after an element without anything after creates a tuple

enum_list = enumerate(our_list) #creates a list of tuples with index and element.