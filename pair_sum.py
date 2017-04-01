#Question - 2: Write a function to find pair sum in a list.
#Example - list = [2, 5, 4, 3, 8, 7, 6, 1]  and k = 9
#Output - {(1, 8), (2, 7), (3, 6), (4, 5)}

def pairSum(list, k):
    if len(list)<2 and len(list) >1000:
        return
    seen=set()
    output=set()
    for num in list:
        target = k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add( (min(num, target), max(num, target)) )
    return output