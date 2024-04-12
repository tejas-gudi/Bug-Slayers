from transformers import pipeline
def answers(question):
    model_name = "distilbert-base-cased-distilled-squad"
    qa_model = pipeline("question-answering", model=model_name, revision="626af31")

    with open("./dislikes_output_dir/missing functionality.txt", "r") as fl:
        context = fl.read()
    with open("./dislikes_output_dir/bugs.txt", "r") as fl:
        context += fl.read()
    ans = qa_model(question = question, context = context)
    print(question)
    print(ans["answer"])

def main():
    questions = [
    "Which functionalities are not currently available?",
    "What features are users most frequently requesting?",
    "what is the critical features absent from the current version?",
    "Can you list the top five features users are asking for but are not yet implemented?",
    "What functionality do users find lacking?",
    "Are there any specific features mentioned in user feedback as missing?",
    "What functionalities are conspicuously absent compared to competitors?",
    "Which features would improve user experience but are not present in the current version?",
    "what are the features that users wants but are not available?",
    "What is the gap in functionality?"
    ]
    for question in questions:
        answers(question)

main()