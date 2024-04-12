import os
from transformers import T5Tokenizer, T5ForConditionalGeneration

final_summary = ""

def summary(title, path):
    global final_summary

    tokenizer = T5Tokenizer.from_pretrained('t5-base')
    model = T5ForConditionalGeneration.from_pretrained('t5-base')

    with open(path, "r", encoding="UTF-8") as fl:
        input_text = fl.read()

    inputs = tokenizer.encode("summarize: " + input_text, return_tensors='pt')

    summary_ids = model.generate(inputs, num_beams=4, max_length=100, early_stopping=True)
    summary = tokenizer.decode(summary_ids.squeeze(), skip_special_tokens=True)

    final_summary += f"__________________________________________________________\n{title} : {summary}\n"

def main():
    my_dict = {
        "Positive application performance": "./likes_output_dir/application performance.txt", 
        "Negative reviews on application performance": "./dislikes_output_dir/application performance.txt", 
        "Positive reviews on Bugs": "./likes_output_dir/bugs.txt",
        "Negative reviews on Bugs": "./dislikes_output_dir/bugs.txt",
        "Positive reviews on missing functionality": "./likes_output_dir/missing functionality.txt",
        "Negative reviews on missing functionality": "./dislikes_output_dir/missing functionality.txt",
        "Positive reviews on user experience": "./likes_output_dir/user experience.txt",
        "Negative reviews on user experience": "./dislikes_output_dir/user experience.txt"
    }

    for title, path in my_dict.items():
        summary(title, path)

    os.system('cls')
    print(final_summary)
    with open("final output.txt", "w", encoding="UTF-8") as fl:
        fl.write(final_summary)

main()