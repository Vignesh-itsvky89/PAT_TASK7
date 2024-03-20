def File(file_name):
# import module
    from datetime import datetime

# get current date and time
    current_datetime = datetime.now().strftime( " ,%d-%m-%y,%H-%M-%S %p")
    
# create a file object along with extension
    file_name = file_name+current_datetime+".txt"
    file = open(file_name, 'x')
    print("File created : ", file_name)
    f= open(file_name, 'w') # write a file
    f.write("This is python class training file. Task 7 -  Function and File Handling")
    f= open(file_name, 'r') # read a file
    print((f.read()))
    f.close()
    file.close()
File("Function_File_Handling")