import os
import time

nil = None

datastore = [nil,nil,nil,nil,
             nil,nil,nil,nil, 
             nil,nil,nil,nil] #Can store up to 3X4 bytes.
             
cval = 0 #Counted value, helps you figure what column you are at.

while True:
  shellinput = input('['+str(cval)+']:') #input uses Counted value.
  shell = str(shellinput).lower()#Turns the "shellinput" input into an input that is all lower. 
  
  #Commands for the datastore
  if shell == 'cls':
    os.system('cls')
  
  elif '>'in shell:
    column = 0
    for vals in datastore:
      column += 1
    pass
    
    if cval >= column:
      os.system('cls')
      pass
    
    else:
      cval += 1
      os.system('cls')

  elif '<' in shell:
    if cval <= 0:
      os.system('cls')
      pass
    else:
      cval -= 1
      os.system('cls')
  
  elif 'add()' in shell:
    val = shell[shell.find("(")+1:shell.find(")")]
    datastore[int(cval)] = str(val)

  
  
  else:
      print('Error:'+str(shell)+" is not a valid datastore command yet!")
  
