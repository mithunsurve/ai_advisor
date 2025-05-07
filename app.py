from flask import Flask, request, jsonify
from advisor import get_qa_chain

app = Flask(__name__)

# Load QA chain once at startup
qa_chain = get_qa_chain()

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    query = data.get("query")
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    response = qa_chain.run(query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
