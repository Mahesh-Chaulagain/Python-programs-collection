from plyer import notification
import datetime

# set the alaram time
alarm_time = datetime.datetime.now().replace(hour=11, minute=25,second=0, microsecond=0)

# calculate the remaining time until the alarm goes off
remaining_time = alarm_time - datetime.datetime.now()

# convert the remaining time to seconds
remaining_time_seconds = remaining_time.total_seconds()

# set up the notification message
if remaining_time_seconds > 0: 
    message = "It's' not yet time to go home. Only " + str(int(remaining_time_seconds/60)) + " minutes left."

else:
    message = "It's time to go home"

# set up the notification using plyer
notification.notify(
    title="Work Reminder",
    message=message,
    timeout=10  # Display the notification for 10 seconds
)