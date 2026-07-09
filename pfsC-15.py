'''
nums = [23,4,6,23,7,4]
empty_=[]
def removes_(nums, empty):
    for j in nums:
        if j not in empty_:
            empty_.append(j)
    print(empty_)
removes_(nums,empty_)


eg:prime number
prime_=5
count=0
def prime_not(prime_,count):
    for j in range(1,prime_+1):
        if prime_ % j == 0:
            count+=1
    if count == 2:
        print(f"{prime_} is a prime number")
    else:
        print(f"{prime_} is not prime")
prime_not(prime_,count)


eg:counting the numbr of words in a sentence
some="python is a programming language"
count=0
def counting(some,count):
    so = some.split(' ')
    for j in so:
        count += 1
    print(count)
counting(some,count)


eg:
some="Python Is a ProGraMming LanGuagE"
cap_count=0
small_count=0
space_count=0
def cap_small(some,cap_count,small_count,space_count):
    for j in some:
        if j.isupper():
            cap_count += 1
        elif j.islower():
            small_count += 1
        else:
            space_count += 1
    print(f"There are total {cap_count} number cap")
    print(f"There are total {small_count} number small")
    print(f"There are total {space_count} number spaces")
cap_small(some,cap_count,small_count,space_count)

eg:Palindrome
def palindrome(so):
    empty_ = ""
    for j in so:
        empty_ = j + empty_
    if empty_ == so:
        print(f"{so} is a palindrome")
    else:
        print(f"{so} is not a palindrome")
palindrome("Garikapati")


eg:perfect number
num = 28
sum_ = 0
def perfect(num, sum_):
    for j in range(1, num):
        if num % j == 0:
            sum_ += j
    if sum_ == num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")

perfect(num, sum_)
'''


















