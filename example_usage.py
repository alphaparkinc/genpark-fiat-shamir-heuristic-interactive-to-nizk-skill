from client import FiatShamirTransform

fs = FiatShamirTransform()
transcript = ["comm_r_9981", "public_key_A", "statement_val_42"]
challenge = fs.generate_challenge(transcript)
print(f"Synthesized Fiat-Shamir Verifier Challenge: {challenge}")
