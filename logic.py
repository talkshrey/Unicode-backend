import collections as cl

n = int(input("Enter number of words: "))
arr = []
# taking inputs from the user and storing it in an array
for i in range(n):
    arr.append(input(("Enter a word: ")))

# calculating the frequency of each word in an array
v = cl.Counter(arr).values()
for j in v:
    print(j, end=" ")
print()
# bonus
new_v = []
for i in v:
    new_v.append(i)

print(new_v.sort())