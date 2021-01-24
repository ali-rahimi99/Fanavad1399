# FANAVARD 3.11.99


# number of objects
n = int(input('Enter number of objects = '))

# number of boxes
m = int(input('Enter number of boxes = '))

# size of boxes
k = int(input('Enter size of boxes = '))

ai = []
# each object size
for item in range(n):
    ai.append(int(input("a("+str(item+1)+") = ")))


# size arrays should be equal to number of objects
if (len(ai) != n):
    print('wrong input')

j = 1
size = k

while (j<=n):
    # check if there is a box left
    if (m > 0):
        # check if the box has empty place
        if (ai[n-j] <= size):

            size = size-ai[n-j]
            j = j+1
        else:
            m = m-1    
            size = k
    else:
        break

# print result
res = j-1
print("Output = " + str(res))