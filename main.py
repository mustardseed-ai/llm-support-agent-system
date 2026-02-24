import json
import os

# ----------------------------
# Load knowledge base
# ----------------------------

def load_knowledge_base(path="data/knowledge_base.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ----------------------------
# Simple intent classifier (rule-based v1)
# ----------------------------

def classify_intent(user_input):
    text = user_input.lower()

    if "wrong" in text:
        return "wrong_number"
    elif "failed" in text or "error" in text:
        return "failed_transfer"
    elif "pending" in text or "stuck" in text:
        return "pending_transfer"
    elif "withdraw" in text or "cashout" in text:
        return "cashout_help"
    else:
        return "unknown"


# ----------------------------
# Retrieval (RAG-lite)
# ----------------------------

def retrieve_knowledge(intent, knowledge_base):
    for item in knowledge_base:
        if item["id"] == intent:
            return item["content"]
    return None


# ----------------------------
# Structured response generator
# ----------------------------

def generate_response(intent, retrieved_content):
    response = {
        "intent": intent,
        "confidence": 0.8 if intent != "unknown" else 0.3,
        "next_action": "escalate_to_human" if intent == "unknown" else "provide_guidance",
        "message": retrieved_content if retrieved_content else "We need more details to assist you."
    }
    return response


# ----------------------------
# Basic validation
# ----------------------------

def validate_response(response):
    required_fields = ["intent", "confidence", "next_action", "message"]

    for field in required_fields:
        if field not in response:
            return False

    return True

import datetime

def log_response(user_input, response, path="logs/run_logs.jsonl"):
    log_entry = {
        "timestamp": datetime.datetime.now(datetime.UTC).isoformat(),
        "input": user_input,
        "output": response
    }

    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry) + "\n")

# ----------------------------
# Main pipeline
# ----------------------------

def run_pipeline(user_input):
    knowledge_base = load_knowledge_base()

    intent = classify_intent(user_input)
    retrieved = retrieve_knowledge(intent, knowledge_base)
    response = generate_response(intent, retrieved)

    if not validate_response(response):
        return {
            "intent": "fallback",
            "confidence": 0.0,
            "next_action": "escalate_to_human",
            "message": "System error — escalating to human support."
        }

    return response

def run_examples(path="examples/sample_inputs.json"):
    with open(path, "r", encoding="utf-8") as f:
        examples = json.load(f)

    results = []
    for ex in examples:
        user_input = ex["text"]
        output = run_pipeline(user_input)
        log_response(user_input, output)
        results.append({"id": ex["id"], "input": user_input, "output": output})

    return results

if __name__ == "__main__":
    print("LLM Support Agent Demo")
    mode = input("Choose mode: (1) single message, (2) run examples: ").strip()

    if mode == "2":
        results = run_examples()
        print("\nBatch Results (first 3 shown):")
        print(json.dumps(results[:3], indent=2))
        print(f"\nDone. Logged {len(results)} runs to logs/run_logs.jsonl")
    else:
        user_message = input("Enter user message: ")
        result = run_pipeline(user_message)
        log_response(user_message, result)
        print("\nStructured Output:")
        print(json.dumps(result, indent=2))