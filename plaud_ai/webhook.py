import hashlib
import hmac

__all__ = ('is_valid_signature',)


def is_valid_signature(payload_body: bytes, signature_header: str, webhook_secret: str) -> bool:
    """Verify that the payload was sent from Plaud."""
    if not signature_header:
        raise ValueError('Signature header is missing.')

    hash_object = hmac.new(webhook_secret.encode('utf-8'), msg=payload_body, digestmod=hashlib.sha256)
    expected_signature = hash_object.hexdigest()

    return hmac.compare_digest(expected_signature, signature_header)