import time
def bubble(data, drawData, timer): 
    n = len(data) 
  
    for i in range(n): 
     
        for j in range(0, n-i-1): 

            if data[j] > data[j+1] : 
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['Green' if x == j + 1 else 'Red' for x in range(len(data)) ])
                time.sleep(timer)
                
    drawData(data, ['Green' for x in range(len(data))])