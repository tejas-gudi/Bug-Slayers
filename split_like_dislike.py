import json

# Load the JSON data from the file (replace 'your_file.json' with the actual filename)
with open('1.json', 'r') as f:
    data = json.load(f)

# Loop through each survey response in the JSON array
with open('likes.txt', 'a', encoding='utf-8') as output_file, open('dislikes.txt', 'a', encoding='utf-8') as dislikes_file:

    # Loop through each survey response in the JSON array
    for response in data:
        # Extract the values for "like" and "dislike"
        like = response["attributes"].get("comment_answers", {}).get("love", {}).get("value")
        dislike = response["attributes"].get("comment_answers", {}).get("hate", {}).get("value")

        # Convert to a single line if the value is not None
        if like is not None:
            like = ' '.join(like.splitlines())
        if dislike is not None:
            dislike = ' '.join(dislike.splitlines())

        # Append the values to the output file, handling missing values gracefully
        output_file.write(f"{like}\n")
        dislikes_file.write(f"{dislike}\n")

print("Extraction and appending to file completed!")