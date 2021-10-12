
def findMinAndMax(l):

        min = l[0]

        max = l[0]

        for a in l:

            if min > a:

                min = a

            if max < a:

                max = a

        return (min, max)

print(findMinAndMax([1,2,3,4]))