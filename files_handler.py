import shutil
import os

def copy(path1,path2):
    
    try:
        ask=int(input("Press 1 for copying Folder and 2 for file:"))
        if (ask==1):
            shutil.copytree(path1,path2)
        elif (ask==2):
            shutil.copy(path1,path2)  
        else:
            print("Enter 1 or 2")  
    except Exception as e:
        print(e)

def move(path1,path2):
    try:
        shutil.move(path1,path2)
    except Exception as e:
        print(e)

def delete_folder(path):
    shutil.rmtree(path)

def delete_file(path):
    os.remove(path)

def main():
    print('Press 1 for Copy \n Press 2 for Move \n Press 3 for Delete folder \n Press 4 for Delete file') 
    k=int(input())
    if k==1:
        p1=input("Enter or paste the address from where you want to copy(Old address):")
        p2=input("Enter or paste the address to where you want to paste(New address):")
        copy(p1,p2)
    elif k==2:
        p1=input("Enter or paste the address from where you want to move(old address):")
        p2=input("Enter or paste the address to where you want to move(new address):")
        move(p1,p2)    
    elif k==3:
        p=input("Enter the path of folder:")
        delete_folder(p)
    elif k==4:
        p=input("Enter the path of file:")
        delete_file(p) 
    
    else:
        print("Enter a valid number")

main()        