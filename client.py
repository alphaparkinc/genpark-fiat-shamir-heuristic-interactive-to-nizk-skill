"""Fiat-Shamir Heuristic Engine.
100% Python Standard Library.
"""

import hashlib

class FiatShamirTransform:
    """Fiat-Shamir heuristic generating non-interactive challenges from transcript."""
    PRIME = 2147483647

    def generate_challenge(self, transcript_items):
        data = ":".join(str(item) for item in transcript_items).encode("utf-8")
        h = int(hashlib.sha256(data).hexdigest()[:8], 16)
        return h % self.PRIME
