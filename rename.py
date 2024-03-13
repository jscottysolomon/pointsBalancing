import os

def search_and_replace(oldString, newString):
    userDir = os.listdir(path='.')

    for y in userDir:
        if("." in y):
            pass
        else:
            filename = "./" + y + "/"
            userFiles = os.listdir(path=filename)

        
            for x in userFiles:
                fileName = "./" + y + "/" + x
                with open(fileName, 'r') as file:
                    fileContent = file.read()

                replaceContent = fileContent.replace(oldString,newString)

                with open(fileName, 'w') as file:
                    file.write(replaceContent)

if __name__ == '__main__':
    search_and_replace("username","UserName")