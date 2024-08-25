# Python3 code to demonstrate
# Bigram formation
# using list comprehension + enumerate() + split()

# initializing list 
original_list = ['LUX Academy is amazing', 'I am learning alot']

# printing the original list 
print ("Original: " + str(original_list))

# using list comprehension + enumerate() + split()
# for Bigram formation
res = [(x, i.split()[j + 1]) for i in original_list 
	for j, x in enumerate(i.split()) if j < len(i.split()) - 1]

# printing result
print ("Bigrams: " + str(res))
