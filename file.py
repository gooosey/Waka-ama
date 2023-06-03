import os
import os.path

def select_files_with_keyword(folder_path: str, keyword: str, keyword_two: str) -> list:

    absolute_folder_path = os.path.abspath(folder_path)


    #Create empty list for the files to be in

    selected_files = []
    selected_files2 = []

    #Find files that contains a keyword before going into the subfiles

    for root, dirs, files in os.walk(absolute_folder_path): 

    #Find file with a certain name

        for file_name in files:

            if keyword in file_name:

                file_path = os.path.join(root, file_name) 

                #Check for if keyword_two is in file

                file_name = os.path.dirname(file_path)

                #Find subfile with certain name

                for root, dirs, files in os.walk(file_name):
                    
                    if keyword_two in file_name:
                        
                #Appends the file to the apporipate list

                        if os.path.isfile(file_path):

                            selected_files.append(file_path)    

                        else:
                            if os.path.isfile(file_path):
                                selected_files2.append(file_path)

    #Returns the files to selected list

    return selected_files , selected_files2



# Change for path location and keywords
folder_path = "resources"

keyword = "Final"
keyword_two = "2018"

#Opening the file

selected_files, selected_files2 = select_files_with_keyword(folder_path, keyword, keyword_two)

if selected_files:
    for file_path in selected_files:
        try:
            with open(file_path, 'r') as file:
                try:
                    file_content = file.read()
                    print(f"Content of selected file '{file_path}':")
                    print(file_content)
                except UnicodeDecodeError:
                    print(f"Unable to decode file '{file_path}' with UTF-8 encoding.")
        except IOError:
            print(f"Unable to open file '{file_path}'.")
else:
    print(f"No files with the keyword '{keyword_two}' found in the folder.")

#Get count of files

listoffiles = len(selected_files)

print (listoffiles)
