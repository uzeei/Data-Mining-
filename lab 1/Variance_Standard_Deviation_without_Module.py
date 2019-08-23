y=[2.1,4.1,6.1,8.1,10.1,12.1,14.1,16.1,18.1,20.1]
x=[1,2,3,4,5,6,7,8,9,10]

#for x
mx= sum(x)/len(x)
pop_var = sum((xi - mx) ** 2 for xi in x) / len(x)
sam_var = sum((xi - mx) ** 2 for xi in x) / (len(x)-1)
pop_std = pop_var**0.5
sam_std = sam_var**0.5

print('Population Variance: ',pop_var) 
print('Sample Variance: ',sam_var)
print('Population Standard Deviation: ',pop_std)
print('Sample Standard Deviation: ',sam_std)

