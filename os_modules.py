import os 
from datetime import datetime 
"""
print(os.getcwd()) # shows the current directory

os.chdir("C:/Users/mertk/Documents") # changes directory

for i in os.listdir(): # shows the directory
    print(i)
"""
"""
print(os.getcwd())
print(os.name) #If the operating system is windows nt will return, if linux it will return posix
"""
# os.mkdir("deneme") #creates file

# os.makedirs("Deneme2/Deneme3") #creates nested file

# os.rmdir ("Deneme2/Deneme3") #only deletes the given file.

# os.removedirs("Deneme2/Deneme3") #deletes all subfiles of the given file 

# os.rename("datetime","datetime_modules.py") # renames the given file
"""
print(os.stat("datetime_modules.py")) #looks at the properties of the given file
sta_time = os.stat("datetime_modules.py").st_atime #we got the modified time of the file
print(sta_time) 
date_time = datetime.fromtimestamp(sta_time) # here we convert seconds to dates
print(date_time)
"""
"""
for klasör_yolu,klasör_isimleri,dosya_isimler  in os.walk("C:/Users/mertk/Desktop") : #We see all the files and folders in the directory we gave by typing
    for i in dosya_isimler :
        print(i)
"""
"""
for klasör_yolu,klasör_isimleri,dosya_isimler  in os.walk("C:/Users/mertk/Desktop") : #prints the files with the extension we give by typing
    for i in dosya_isimler :
        if(i.endswith(".py")):
            print(i)
os.rmdir("sys_moodules.py")
"""
# print(os.path.exists("C:/Users/mertk/Desktop")) #returns true if such a file exists, false otherwise
"""
print(os.path.isdir("C:/Users/mertk/Desktop")) #returns true if it is a directory, false otherwise
print(os.path.isfile("C:/Users/mertk/Desktop/advanced_modules/os_modules.py")) #returns true if it is a file, false otherwise

a,b = os.path.split("C:/Users/mertk/Desktop/advanced_modules/sys_modules.py")
print(a)
print(b)
print(os.path.splitext(b))
"""

print(os.getcwd())
os.startfile("deneme.txt")