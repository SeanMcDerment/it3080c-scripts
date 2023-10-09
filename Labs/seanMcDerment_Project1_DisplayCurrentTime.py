import datetime

def timeNow():
    # Get the current time
    currentTime = datetime.datetime.now().time()

    # Format the time as a string
    time = currentTime.strftime("%H:%M:%S")

    return time

# Call the function directly
currentTime = timeNow()
print(f"The current time is: {currentTime}")
