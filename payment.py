from flask import request, jsonify

def process_payment():
    data = request.json

    amount = data.get("amount")
    card = data.get("card")

    # ❌ No validation
    # ❌ No error handling
    # ❌ No security

    if amount:
        return jsonify({"status": "success"})
    
    return jsonify({"status": "failed"})
