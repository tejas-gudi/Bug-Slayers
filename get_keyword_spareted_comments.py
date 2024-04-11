import os
def segregate(comments):
    keywords = {
        'application performance': ['performance', 'slow', 'lag', 'speed'],
        'user experience': ['user experience', 'UX', 'usability', 'intuitive'],
        'missing functionality': ['missing functionality', 'feature', 'lack'],
        'bugs': ['bug', 'issue', 'error', 'crash']
    }


    # Initialize a dictionary to store the segregated comments
    segregated_comments = {category: [] for category in keywords}

    # Process each comment
    for comment in comments:
        # Check for matches with the keywords in each category
        for category, words in keywords.items():
            for word in words:
                if word in comment:
                    segregated_comments[category].append(comment)
                    # break  
    return segregated_comments

def make_dir(input_file, output_dir):
    # Load the comments from a text file (replace 'comments.txt' with the actual filename)
    with open(input_file, 'r', encoding='utf-8') as comments_file:
        liked_comments = comments_file.read().splitlines()
    
    segregated_comments = segregate(liked_comments)
    
    output_directory = output_dir

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Process each comment
    for category, comments in segregated_comments.items():
        # Create a file for the current category
        file_path = os.path.join(output_directory, f"{category}.txt")

        # Write the comments to the file
        with open(file_path, 'w', encoding='utf-8') as category_file:
            for comment in comments:
                category_file.write(comment + '\n')

def main():
    make_dir('likes.txt', './likes_output_dir')
    make_dir('dislikes.txt', './dislikes_output_dir')

main()