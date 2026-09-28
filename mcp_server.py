import sys
import json
from client import FiatShamirTransform

fs = FiatShamirTransform()

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "fiat_shamir_challenge",
                        "description": "Generate deterministic non-interactive challenge from public proof transcript",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "transcript": {"type": "array", "items": {"type": "string"}}
                            },
                            "required": ["transcript"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "fiat_shamir_challenge":
            chal = fs.generate_challenge(args["transcript"])
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"challenge": chal})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
