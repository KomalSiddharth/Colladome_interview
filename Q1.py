# Q.1.Frequency Counter 
# Write a Python function that takes a list of numbers and returns a dictionary with the count of each number. 
# Example input: [1, 2, 2, 3, 1, 4] Expected output: {1: 2, 2: 2, 3: 1, 4: 1}



def count(numbers):
  dict_count={}
  for num in numbers:
    if num in dict_count:
      dict_count[num]+=1
    else:
      dict_count[num]=1

  return dict_count
input=[1,2,3,1,5,6]
print(count(input))