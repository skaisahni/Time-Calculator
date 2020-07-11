def add_time(start, duration, initialday='None'):

#Getting the initial time
#First, let's get the hour
  start_h = int(start.split(':')[0])
  #Second, let's get the initial minute
  start_m = int(start.split(':')[1].split()[0])
  #Last, but not least, finding out if we are talking about time ante or post meridiem
  meridiem = start.split(':')[1].split()[1]

  #Now, let's get the duration
  addedh = int(duration.split(':')[0])
  addedm = int(duration.split(':')[1].split()[0])

  #let's start by adding the minutes. The range of the minutes will be between 0 and 60. 
  newminute = start_m + addedm
  #if we go over 60, we will add an hour to the addedh. 
  if newminute > 59:
      newminute = newminute - 60 
      addedh = addedh + 1
      
  #Let's make sure that we transform anything bigger that 24 h into something inside the range of 0 and 24. Also, let's start taking into consideration how many days are we gonna be shifting in time. 
  ndays=0
  while addedh >= 24:
      ndays = ndays+1
      addedh = addedh - 24
      

  #Let's handle with the result of the newh after modifying the addedh, for the first case
  #When we add 12 hours, we will be just changing the AM or PM for the opposite. 
  if addedh==12:
      newh=start_h
      #If we add 12 or more hours and we start let's say at noon, we will jump to the next day. 
      if meridiem == "PM":
          print("Heeeeello")
          ndays = ndays + 1
          meridiem = "AM"
      else:
          meridiem = "PM"
  #When we add more than 12 hours, the change in AM or PM depends in the initial hour too.         
  if addedh>12:
      addedh = addedh-12
      newh=start_h + addedh
      if newh<12:
          if meridiem == "PM":
              ndays = ndays + 1
              meridiem = "AM"
          else:
              meridiem = "PM"
      
      if newh==12:
          ndays = ndays + 1
      
      if newh>12:
          newh=newh-12
          if meridiem == "PM":
              ndays = ndays + 1
              meridiem = "AM"
          else:
              meridiem = "PM"
      
  #Now, let's do the case when we add less than 12 hours
  if addedh<12:
  #A little something that I add because it was giving me trouble when the initial time was 12. 
      if start_h==12:
          start_h=0
          newh=start_h+addedh
      else:
        newh=start_h+addedh
      if newh == 12:
          if meridiem == "PM":
              ndays = ndays + 1
              meridiem = "AM"
          else:
              meridiem = "PM"
          
      if newh>12:
          newh = newh-12
          if meridiem == "PM":
              ndays = ndays + 1
              meridiem = "AM"
          else:
              meridiem = "PM"

   #I create a list with the week of the days.    
  daysoftheweek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

  stringh = str(newh)

  if newminute<10:
    stringm = "0" + str(newminute)
  else:
    stringm= str(newminute)

  auxndays = ndays
  if initialday != "None":
  #Creating an auxiliar parameter
    y = initialday.lower().capitalize()
  #With this, I can look for the index of the day of interest in my daysoftheweek list
    indexa = daysoftheweek.index(y) 
    

    if ndays==0:
      new_time = stringh + ":" + stringm + " " + meridiem + ", " + daysoftheweek[indexa]
    elif ndays<=7:
      newindex = indexa + ndays
      if ndays == 1:
        new_time = stringh + ":" + stringm + " " + meridiem +", " + daysoftheweek[newindex] + " (next day)"
      else:
        new_time = stringh + ":" + stringm + " " + meridiem +", " + daysoftheweek[newindex] + " (" +str(auxndays)+ " days later)"
    elif ndays>7:
      while ndays > 7:
        ndays = ndays -7
      newindex = indexa + ndays
      new_time = stringh + ":" + stringm + " " + meridiem +", " + daysoftheweek[newindex] + " (" +str(auxndays)+ " days later)"
  else:
    if ndays==0:
      new_time = stringh + ":" + stringm + " " + meridiem
    elif ndays <=7:
      if ndays == 1:
        new_time = stringh + ":" + stringm + " " + meridiem +  " (next day)"
      else:
        new_time = stringh + ":" + stringm + " " + meridiem + " (" +str(auxndays)+ " days later)"
    elif ndays>7:
      while ndays > 7:
        ndays = ndays -7
      new_time = stringh + ":" + stringm + " " + meridiem + " (" +str(auxndays)+ " days later)"

  return new_time