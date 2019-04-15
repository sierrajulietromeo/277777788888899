function per(n, steps=0) {

    if (n < 10)  {
      return console.log("TOTAL STEPS: " + steps)
    } 
  
  numString = n.toString(10)
  result = 1
  
    for (i = 0; i < numString.length; i++) { 
      
      result *= numString[i]
      
    }
  
  steps = steps + 1
  console.log(result)
  per(result, steps)  
  
  } 
  
  per(77)