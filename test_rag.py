from app.rag_pipeline import load_and_process, ask_question

db = load_and_process("data/docs/sample.pdf")

while True:
	question = input("Enter your question (or type 'quit' to exit): ").strip()
	if question.lower() in {"quit", "exit", "q"}:
		print("Goodbye!")
		break
	if not question:
		continue
	answer = ask_question(db, question)
	print("\nANSWER:\n", answer)