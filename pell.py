def pell(n):
    index = 2
    pell_val =[0,1]
    adding = 1
    for index in range(n-1):
        if n<0:
            return
        adding =(2 * adding + pell_val[-2])
        pell_val.append(adding)                 
        # print(index)
   return print(adding)
