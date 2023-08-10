# Function to grab the initial user input
def get_copywrite():
    # Get user input for topic, keywords and writer type
    topic = input("Enter the topic of the blog post: ")
    keywords_input = input("Enter the keywords for the blog post (separated by commas): ")
    
    not_found = True
    
    while not_found:
        writer_type = input("Enter the writer type (type 'avail_types' to see the available writer types): ")
    
        if writer_type == "avail_types":
            not_found = True
            print("Types available are: \n General \n Tech \n Food \n Music \n Gaming \n Fashion \n Entertainment (Movies and TV) \n Sports")
        
        if writer_type.lower() in ("general", "tech", "food", "music", "gaming", "fashion", "entertainment", "sports"):
            not_found = False

        else:
            not_found = True
            print("INCORRECT WRITER TYPE")

    # Parse the keywords input into a list
    keywords = [keyword.strip() for keyword in keywords_input.split(",")]

    return topic, keywords, writer_type

def get_editor():
    editor_type = input("Enter the editor type (type 'avail_types' to see the available editor types): ")
    
    if editor_type == "avail_types":
        print("Types available are: \n General \n Tech \n Food \n Music \n Gaming \n Fashion \n Entertainment (Movies and TV) \n Sports")
        editor_type = input("Please enter the editor type: ")
        
    return editor_type