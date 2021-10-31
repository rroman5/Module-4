currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait")

currentTimeInt = int(currentTimeStr)  #<---- ____ Not necessary also letters are not the same as above
waitTimeInt = int(waitTimeStr)  #____ Not necessary also letters are not the same as above

'''
Logic error
finalTimeInt = (currentTimeInt + waitTimeInt) %24
'''
finalTimeInt = (currentTimeInt + waitTimeInt)
print (finalTimeInt)
