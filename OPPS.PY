class Accounts:
    def __init__ (self , bal ,acc):
        self.baclance=bal
        self.account_no= acc
        
    def debits(self , ammount):
        self.baclance-=ammount
        print("RS." , ammount , "was debits")
        print("total blance is", self.baclance)
    def credits(self, ammount):
        self.baclance += ammount
        print("RS.", ammount , "is cridets")
        print("total blances is ", self.baclance)
        
    def get_balance(self):
        return self.baclance
          
acc1=Accounts(10000, 9823221)
acc1.debits(1000)
acc1.credits(1)


class Cricle:
    
    def __init__ (self, redies):
        self.redies=redies
        
    def area(self):
        return (22/7)* self.redies ** 2
    
    def perameter(self):
        return 2 * (22/7) * self.redies
    
    
c1 = Cricle(21)
print (c1.perameter())
print (c1.area())

class Empolyee:
    def __init__ (self , dept , role , salary):
        self.dept=dept
        self.role=role
        self.salary=salary
        
    def show_details(self):
        print("dept :" , self.dept)
        print("role :" , self.role)
        print("salary :", self.salary)
e1 = Empolyee("IT", "Software Developer", 70000)
e1.show_details()


ef sum_of_array(array):
    sum=0
    for i in range(len(array)):
        sum+=array[i]
    return sum
array=[25,24,26,25]
print(sum_of_array(array))

def mul_of_array(array):
    mul=1
    for i in range(len(array)):
        mul*=array[i]
    return mul
array=[1,2,3,4,5]
print(mul_of_array(array))

def even_odd(array):
    results=[]
    for i in range(len(array)):
        if i % 2 == 0:
            results.append("even")
        else:
            results.append("odd")
    return results

array=[1,2,3,4,5,6]
print(even_odd(array))

def sum_of_even(array):
    sum=0
    for i in array:
        if i % 2 == 0:
            sum+=i
    return sum
array=[1,2,3,4,5,6]
print(sum_of_even(array))

def sum_of_array(array):
    sum_even = 0
    for num in array:
        if num % 2 == 0:  # Check if the number is even
            sum_even += num
    return sum_even

array = [1, 2, 3, 4, 5, 6]
print(sum_of_array(array)) 

def sort_arr(array):
    return sorted(array)
array=[23,21,23,44,332,2,12,3432,2343,34,32,344,2]
sort_array=sort_arr(array)
print("sort_array:",sort_array[-1])

def bubble_sort(array):
    for r in range(1,len(array)):
        for i in range(len(array)-r):
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
                
array=[1,3,4,5,6,33,2,32,9]
bubble_sort(array)
print("BubbleSort :", array)




def bubble_sort(array):
    for l in range(1 ,len (array)):
        for i in range(len(array)-l):
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
array=[23,11,21,211,112,42,33]
bubble_sort(array)
print(array)

def bubble_sort(array):
    for l in range(1,len(array)):
        for i in range(len(array)-l):
            if array[i]>array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
array=[1,2322,232,13,144,23,24,11,21,22]
bubble_sort(array)
print(array)

def find_maxvalue(array):
    l=array[0]
    for i in range(len(array)):
        if array[i]>l:
            l=array[i]
    return l
array=[2,23,22,222,3221,221]
print(find_maxvalue(array))

def find_minivalue(array):
    l=array[0]
    for i in range(len(array)):
        if array[i]<l:
            l=array[i]
    return l
array=[2,33,44,55,66,23]
print(find_minivalue(array))
        
def swap_array(array,first,secound):
        temp=array[first]
        array[first]=array[secound]
        array[secound]=temp
array=[1,2,3,4,5,6]
swap_array(array ,1,3)
print(array)

def swap(array,fir,sec):
    array[fir],array[sec]=array[sec],array[fir]
array=[1,2,3,4,5,6]
swap(array, 2 ,4)
print(array)

def liner_search(array, target):
    for i in range(len(array)):
        if array[i]==target:
            return i
    return -1
arr=[1,22,33,443,54,36,37,34,33,33,2,3,34,43,2,2,3]
tar=43
index=liner_search(arr,tar)
if index !=-1:
    print(f"target value {tar} find index of {index}")
else:
    print(f"target value is not in array sorry")
    
def sum_array(array):
    sum=0
    for i in range(len(array)):
        sum+=array[i]
    return sum
arr=[1,2,3,4,5]
print(sum_array(arr))

def mul_array(array):
    mul=1
    for i in range(len(array)):
        mul*=array[i]
    return mul
arr=[1,2,3,4]
print(mul_array(arr))

def reverse_array(array):
    start=0
    last=len(array)-1
    while start<last:
        arr[start],arr[last]=arr[last],arr[start]
        start+=1
        last-=1
arr=[1,2,3,4,5]
print("original array:",arr)
reverse_array(arr)
print("reverse array :",arr)

def duplicate(array):
    x = []
    y = []
    for i in array:
        if i not in x:
            x.append(i)
    for i in x:
        if array.count(i) > 1:
            y.append(i)
    return y
arr=[1,2,3,4,4,4,32,2,1]
print(duplicate(arr))

def min_value(array):
    min=array[0]
    for i in range(len(array)):
        if array[i]>min:
            min=array[i]
    return min 
array=[10,2,3,4,5]
print(min_value(array))

def even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
arr = [1,2,4,5,6]
for num in arr:
    print(f"{num} is {even_odd(num)}")
    
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def missing_no(array):
    n=len(array)+1
    total_sum=(n*(n+1)) //2
    sum_of_array=sum(arr)
    miss_no = total_sum - sum_of_array
    return miss_no
arr=[1,2,3,4,5,6,8]
print(missing_no(arr))

def samllar_value(array ,x):
    count=0
    for i in range(len(array)):
        if array [i] < x:
            count+=1
    return count
arr=[1,2,3,2,22]
x=22
print(samllar_value(arr,x))

def alternate_value(array):
    for i in range(len(array)):
        if i % 2 ==0:
            print(array[i], end=" ")
array=[1,2,44,5,4,3]
alternate_value(array)
            
def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)  # Recursive call to print numbers from 1 to n-1
        print(n)

# Example usage:
N = 10
print_numbers(N)


def rotate(array,n):
    i=0
    j=n-1
    while i != j:
        array[i],array[j]=array[j],array[i]
        i=i+1
    pass
array=[1,2,3,4,5]
n=len(array)
rotate(array, n) 
print ("rotatr array is")
for i in range(0, n):
    print (array[i], end = ' ')
    




def sumsqure_of_array(array):
    sum=0
    for i in range(len(array)):
        if i % 2 == 0:
            sum+=i**2
    return sum 

array=[1,2,3,4,5,6,7,8,9,10]
print(sumsqure_of_array(array))

def perfect_no(n):
    if n<=0:
        return False
    sum=0
    for i in range (1,n):
        if n % i == 0:
            sum += i
    return sum == n
n=28
print(perfect_no(n))
