#[1,2,3,8,6,2] --> [1,2,6,2,3,8]
#[] --> []
#[2,3,8,6,9] --> []
#[7,5,3,8] --> [7,5,8,3]
#[4,6,3,5,3,6,3,3,8,7,6,5,4,3,2]

def getAnswerRaw(A):
    print('Input=%s'%A)
    if sorted(A, reverse=True)==A:
        # Handling special case
        return A
    for i in reversed(range(len(A))):
        print('checking %s' %A[i-1])
        if A[i-1]<A[i]:
            # An element to the right is higher than me
            smallest_greater_than_me = i

            for j in range(i, len(A)):
                print('Check %s with %s' %(A[i], A[j]))
                if A[j]< A[smallest_greater_than_me] and A[j]>A[i-1]:
                    smallest_greater_than_me = j
            A[i-1], A[smallest_greater_than_me] = A[smallest_greater_than_me], A[i-1]
            indices = list(range(i, smallest_greater_than_me)) + list(range(smallest_greater_than_me+1, len(A)))
            to_sort = [A[k] for k in indices]
            to_sort = sorted(to_sort, reverse=True)
            for idx in indices:
                A[idx] = to_sort.pop()
            print('Final Answer = %s' %A)
            return A
        else:
            pass

def getAnswer(A):
    print('Input=%s'%A)
    A = [int(s) for s in ' '.join(str(A)).split()]
    if sorted(A, reverse=True)==A:
        # Handling special case
        return 'No Higher Number can be formed'
    for i in reversed(range(len(A))):
        if A[i-1]<A[i]:
            # An element to the right is higher than me
            smallest_greater_than_me = i
            for j in range(i, len(A)):
                if A[j]< A[smallest_greater_than_me] and A[j]>A[i-1]:
                    smallest_greater_than_me = j
            to_sort = [A[i-1]]+A[i:smallest_greater_than_me] + A[smallest_greater_than_me+1:len(A)]
            A[i-1] = A[smallest_greater_than_me]
            A[i:] = sorted(to_sort)
            A = int(''.join([str(i) for i in A]))
            print('Final Answer = %s' %A)
            return A
        else:
            pass

if __name__=='__main__':
    # getAnswerRaw([1,2,3,8,6,2])
    getAnswer(218765)
