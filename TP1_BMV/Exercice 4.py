x = "Sa" # x= Sa     y= ?    Print(y)= ?
y = x+"lut" # x=Sa      y= lut     Print(y)= Salut
y = y+"\n\tCesart" # x= Sa      y= lut Cesart     Print(y)= Salut Cesart
x+= "lut "+"Jules" # x= Salut Jules     y= lut Cesart      Print(y)= Salut Cesart
y  = len(x) # x= Salut Jules      y= 11     Print(y)= 11
y = len("BonjourJuju") # x= Salut Jules     y= 11      Print(y)= 11
y = "Salut! "*2 # x= Salut Jules      y= Salut! Salut!      Print(y)= Salut! Salut!
x = len(y) # x= 14     y=  Salut! Salut!     Print(y)= Salut! Salut!
y.strip() # x= 14     y= Salut! Salut!      Print(y)= Salut! Salut!
y= y.strip() # x= 14     y= Salut! Salut!     Print(y)= Salut! Salut!



