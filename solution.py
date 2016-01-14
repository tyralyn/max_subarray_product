def solution(A):
    totalMax = A[0]
    currentMin = A[0]
    currentMax = A[0]
    current = A[0]
    for i in range (1,len(A)):
        current = A[i];
        currentMaxTemp = max(currentMin*current, currentMax*current, current)
        currentMinTemp = min(currentMin*current, currentMax*current, current)
        currentMin = currentMinTemp
        currentMax = currentMaxTemp
        if currentMax > totalMax:
            totalMax=currentMax
    return totalMax
