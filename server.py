from flask import Flask, request, jsonify
import re
import test_chatbot           # your helper module

app = Flask(__name__)

# ──────────────────────────────────────────────────────────
@app.post("/v1/outlet-lookup")
def outlet_lookup():
    """
    Body  : { "query": "Koramangala" }
    Return: { "primary_name": "...", "address": "..." }
    """
    query = (request.get_json(force=True).get("query") or "").strip()

    # ── Call your own lookup function ─────────────────────
    raw = test_chatbot.lookup(query)          # whatever it returns

    # ── CASE A – lookup already returns correct dict ─────
    if isinstance(raw, dict) and "primary_name" in raw and "address" in raw:
        return jsonify({
            "primary_name": raw["primary_name"],
            "address"     : raw["address"]
        }), 200

    # ── CASE B – parse the sentence you showed ───────────
    if isinstance(raw, dict) and "response" in raw:
        sentence = raw["response"]

        # Regex: Is the correct outlet: <NAME> located at <ADDRESS>?
        m = re.search(
            r"outlet:\s*(.+?)\s+located\s+at\s+(.+?)\s*\?",
            sentence,
            flags=re.I
        )
        if m:
            name, addr = m.group(1).strip(), m.group(2).strip()
            return jsonify({
                "primary_name": name,
                "address"     : addr
            }), 200

    # ── Fallback – at least return something ─────────────
    return jsonify({
        "primary_name": query or "Unknown Outlet",
        "address"     : "Address not found"
    }), 404
# ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
