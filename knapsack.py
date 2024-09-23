def knapSack(W, wt, val, n): 
    K = []
    for _ in range(n + 1):
        K.append([0] * (W + 1))

    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] 
                            + K[i-1][w-wt[i-1]], 
                            K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 

    return K[n][W] 

if __name__ == '__main__': 
    n = int(input("Enter the number of items: "))
    
    weight = []
    profit = []
    
    print("Enter the weights of the items:")
    for _ in range(n):
        w = int(input())
        weight.append(w)
    
    print("Enter the values of the items:")
    for _ in range(n):
        v = int(input())
        profit.append(v)
    
    W = int(input("Enter the maximum weight capacity of the knapsack: "))
  
    print("Maximum value in Knapsack =", knapSack(W, weight, profit, n))
