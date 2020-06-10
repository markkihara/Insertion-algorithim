import os 
#os.system("")
list_A =[5,5,6,7,7,5,4,6,2,3]
def insertation_fun(list_A):
       indexing_length=range(1,len(list_A))
       
       for i in indexing_length:
         
              value_to_sort=list_A[i]
              while list_A[i-1]> value_to_sort and i>0:
                     list_A[i], list_A[i-1]=list_A[i-1], list_A[i]
                     i=i-1
       return list_A

print(insertation_fun(list_A))