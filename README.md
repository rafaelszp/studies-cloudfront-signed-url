# cloudfront signed example

## References

1. https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudfront.html#generate-a-signed-url-for-amazon-cloudfront



## Steps

1. Generate keys
```shell
openssl genrsa -out private_key.pem 2048
openssl rsa -pubout -in private_key.pem -out public_key.pem
```

2. Create a new Cloudfront public key and attatch it to a Key group

3. Select the key and attatch to  your Origin Behavior

4. Create python env
```fish
cd ~
python -m venv aws

#load
source ~/aws/bin/activate.fish


```

5. CD to your project folder and install deps
```fish
cd ~/dev/cloudfront-signed-example
pip install -r requirements.txt
```

6. edit signed.py and update URL and KEY attributes

7. Run
```fish
python signed.py
```
