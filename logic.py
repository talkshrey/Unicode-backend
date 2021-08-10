import collections as cl

n = int(input("Enter number of words: "))
arr = []
# taking inputs from the user and storing it in an array
for i in range(n):
    arr.append(input(("Enter a word: ")))

# calculating number of distinct words
distinct = len(cl.Counter(arr).values())
print(distinct)

# calculating the frequency of each word in an array
v = cl.Counter(arr).values()
print("Frequency of each word in the array:", end=" ")
for j in v:
    print(j, end=" ")
print()