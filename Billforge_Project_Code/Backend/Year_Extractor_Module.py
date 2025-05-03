import docx2txt

def yearsemextractor(doc_path):

# Specify the path to your .doc file
 docx_file_path = doc_path

# Extract and display the content
 text = docx2txt.process(docx_file_path)
#print(text)

 start_index = text.find("List of Bills")
 end_index = text.find("Question Paper Setter & Script Examiner")

 desired_string = "demo"

# Print the first line of text between the specified indices
 if start_index != -1 and end_index != -1:
    Examiners_of_SessionalClasses = text[start_index:end_index]
    lines = Examiners_of_SessionalClasses.split('\n')
    if lines:
        #print(lines[0])
        desired_string=lines[0]

        
    else:
        print("No lines found in the specified range.")
 else:
    print("Text not found.")


 return desired_string







def nameextractor(doc_path):

# Specify the path to your .doc file
 docx_file_path = doc_path

# Extract and display the content
 text = docx2txt.process(docx_file_path)
#print(text)

 start_index = text.find("Department of ")
 end_index = text.find("Question Paper Setter & Script Examiner")

 desired_string = "demo"

# Print the first line of text between the specified indices
 if start_index != -1 and end_index != -1:
    Examiners_of_SessionalClasses = text[start_index:end_index]
    lines = Examiners_of_SessionalClasses.split('\n')
    if lines:
        #print(lines[0])
        desired_string=lines[0]
        
        str=desired_string
        result = str.split(' ')
        d2=""
        for xx in result:
             d2+=xx
        desired_string=d2
        
    else:
        print("No lines found in the specified range.")
 else:
    print("Text not found.")


 return desired_string

