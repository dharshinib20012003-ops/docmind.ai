from app.rag_pipeline import load_and_process, ask_question


def main():
    pdf_path = "data/docs/sample.pdf"
    print(f"Loading document from: {pdf_path}")

    try:
        db = load_and_process(pdf_path)
    except Exception as e:
        print(f"Failed to load PDF: {e}")
        print("Make sure a valid PDF file exists at data/docs/sample.pdf")
        return

    print("\nThe document is loaded. You can now ask questions.")
    print("Type 'quit' or 'exit' to stop.\n")

    while True:
        question = input("Question: ").strip()
        if question.lower() in {"quit", "exit", "q"}:
            print("Goodbye!")
            break
        if not question:
            continue

        try:
            answer = ask_question(db, question)
            print(f"Answer: {answer}\n")
        except Exception as e:
            print(f"Error generating answer: {e}\n")


if __name__ == "__main__":
    main()
