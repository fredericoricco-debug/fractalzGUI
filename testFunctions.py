def initialize(angle, iterations, values, scale, speed = 0):
  #######################Define variables#################################
  templist = list(values)
  ########################Construct list##################################
  for i in range(iterations):
      #List multiplies by three
      templist += templist + templist
      #Go through first third of list
      for n in range(int(len(templist)/3)):
          #Modifies value with angle
          templist[n] = templist[n] + angle
      #Go through last third of list
      for n in range(int(len(templist)/3)):
          n = len(templist) - n - 1
          #Modifies value with angle
          templist[n] = templist[n] - angle
    return templist

def initialize2(angle, iterations, values, scale, speed = 0):
  #######################Define variables#################################
  templist = list(values)
  ########################Construct list##################################
  for i in range(iterations):
       #List multiplies by three
      templist += templist + templist
      #Go through first third of list
      for n in range(int(len(templist)/3)):
          #Modifies value with angle
          templist[n] = templist[n] - angle
      #Go through last third of list
      for n in range(int(len(templist)/3)):
          n = len(templist) - n - 1
          #Modifies value with angle
          templist[n] = templist[n] + angle
  return templist


def draw(templist):
    #######################Define variables#################################
    sideLength = (scale/((iterations) * 2 * ((len(templist)/3)+1)*2))
    ##############################Draw######################################
    for i in range(len(templist)):
        if i % 3 == 0:
            t.color(color1)
        if i % 3 == 1:
            t.color(color2)
        if i % 3 == 2:
            t.color(color3)
        t.setheading(templist[i])
        t.forward(sideLength)
