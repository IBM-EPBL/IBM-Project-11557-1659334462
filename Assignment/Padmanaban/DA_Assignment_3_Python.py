#!/usr/bin/env python
# coding: utf-8

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[1]:


pow(7,4)


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[35]:


s="Hi there Sam!"
print(x)


# In[36]:


print(s.replace("Sam!","dad!"))
x=s.split()


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[4]:


txt1="The diameter of Earth is {planet},{diameter} kilometers.".format(planet="Earth",diameter="12742")


# In[5]:


print(txt1)


# ** Given this nested list, use indexing to grab the word "hello" **

# In[ ]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[7]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a=lst[3][1][2];
print(a)


# ** Given this nest dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[ ]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[8]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]["tricky"][3]['target'][3])


# ** What is the main difference between a tuple and a list? **

# In[9]:


# Tuple is immutable
#Tuples operations are safe.
#Tuples consumes less memory.


# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[11]:


def domainGet(email):
    print("Your domain is: " + email.split('@')[-1])

email = input("Please enter your email: >")
domainGet(email)


# In[13]:


domainGet('user@domain.com')


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[14]:


def findDog(st):
    if 'dog' in st.lower():
        print("True")
    else:
        print("False")

st = "Is there a dog here?"
findDog(st)


# In[15]:


findDog('Is there a dog here?')


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[16]:


value = 'This dog runs faster than the other dog dude!';

def countdogs(value):
    count = 0
    for word in value.lower().split():
        if word == 'dog' or word == 'dogs':
            count = count + 1
            print(count)

countdogs(value)


# ### Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[ ]:


def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'


# In[17]:


def caught_speeding(speed, is_birthday):
    pass


# In[18]:


caught_speeding(81,True)


# Create an employee list with basic salary values(at least 5 values for 5 employees)  and using a for loop retreive each employee salary and calculate total salary expenditure. 

# In[20]:


def weeklyPaid(hours_worked, wage):
    if hours_worked > 40:
        return 40 * wage + (hours_worked - 40) * wage * 1.5
    else:
        return hours_worked * wage
 
 
hours_worked = 50
wage = 100
 
pay = weeklyPaid(hours_worked, wage)
 
print(f"Total gross pay: Rs.{pay:.2f} ")


# Create two dictionaries in Python:
# 
# First one to contain fields as Empid,  Empname,  Basicpay
# 
# Second dictionary to contain fields as DeptName,  DeptId.
# 
# Combine both dictionaries. 

# In[31]:


def Merge(dict1,dict2):
    res={**dict1, **dict2}
    return res
dict1 = {"Empid": "001","EmpName": "Murugan","Basicpay": "2000"}
dict2 = {"DeptName": "Web Designer","DeptID": "07"}


# In[32]:


dict3=Merge(dict1,dict2)


# In[33]:


print(dict3)


# In[ ]:




