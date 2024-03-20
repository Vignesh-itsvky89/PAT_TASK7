def File():
# import module
    from datetime import datetime

# get current date and time
    current_datetime = datetime.now().strftime("%A,%d-%m-%y,%H-%M-%S %p")
    print("Current date & time : ", current_datetime)

# convert datetime obj to string
    str_current_datetime = str(current_datetime)

# create a file object along with extension
    file_name = str_current_datetime+".txt"
    file = open(file_name, 'x')
    print("File created : ", file_name)
    f= open(file_name, 'w') # write a file
    f.write(current_datetime)
    f= open(file_name, 'r') # read a file
    print((f.read()))
    f.close()
    file.close()
File()