import os 

def select_files_with_keyword(folder_path: str, keyword: str) -> list: 
    #find file location

    absolute_folder_path = os.path.abspath(folder_path) 
    #put inside list

    selected_files = [] 

     

    

    for root, dirs, files in os.walk(absolute_folder_path): 

        for file_name in files: 

            if keyword in file_name: 

                # Find file 

                file_path = os.path.join(root, file_name) 

  

                # make sure its a file

                if os.path.isfile(file_path): 

                    selected_files.append(file_path) 

     

    return selected_files 

# Change for path location and keyword

folder_path = "/Users/goose/Desktop/3.7B resource files" 

keyword = "Final"  

selected_files = select_files_with_keyword(folder_path, keyword) 


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
    print(f"No files with the keyword '{keyword}' found in the folder.")