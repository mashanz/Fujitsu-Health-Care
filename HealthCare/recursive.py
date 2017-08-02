input  = 10
output = 0

def recur(input,output):
 output=5
 #return output

if "__main__"==__name__:
 recur(input,output)
 recur(output,output)
 recur(output,output)
 print(output)