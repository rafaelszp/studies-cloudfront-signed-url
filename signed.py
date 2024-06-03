import datetime

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from botocore.signers import CloudFrontSigner


def rsa_signer(message):
    with open('key.pem', 'rb') as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key.sign(message, padding.PKCS1v15(), hashes.SHA1())

key_id = 'K3BA9WK3Z3D4DN'
url = 'https://d2ex1w7h9byyb5.cloudfront.net/teste.html'
expire_date = datetime.datetime(2025, 1, 1)

cloudfront_signer = CloudFrontSigner(key_id, rsa_signer)

# Create a signed url that will be valid until the specific expiry date
# provided using a canned policy.
signed_url = cloudfront_signer.generate_presigned_url(
    url, date_less_than=expire_date)
print(signed_url)
