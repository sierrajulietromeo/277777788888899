def per(n, steps=0, resultArray=None):
    if resultArray == None:
      resultArray=[]
  
    if n < 10:
      
      return "TOTAL STEPS: " + str(steps), resultArray
      

  
    digits = [int(i) for i in str(n)]
    
 
    
    result = 1
    
  
    for j in digits:
      result *= j

    steps = steps + 1
    resultArray.append(result)
    #print(resultArray)
    return per(result, steps, resultArray)


print(per(99999999999999999999999999999999999999))