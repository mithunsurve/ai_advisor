from advisor import get_qa_chain

def main():
    print("🎓 Welcome to the MSCS Academic Advisor!")
    print("Type your question below (or type 'exit' to quit):\n")
    
    qa_chain = get_qa_chain()

    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        try:
            response = qa_chain.run(query)
            print(f"Advisor: {response}\n")
        except Exception as e:
            print(f"⚠️ Error: {e}\n")

if __name__ == "__main__":
    main()
