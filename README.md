# python-aws-s3

Open [AWS Console](https://aws.amazon.com/console/) and log in.

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/1.png?token=AGNQQB4Q7sizjmFqsAVZq3V_sN8TMRFLks5YwerPwA%3D%3D "Logo Title Text 1")

Click the `Services` dropdown and select the `S3` service.

Click `Create Bucket`

Give it a name, region then hit next through each step.

Now click your new bucket

Upload a test image to your bucket

```


arn:aws:iam::281979644754:user/sample-user
```

```
{
    "Version": "2012-10-17",
    "Id": "Policy1488494182833",
    "Statement": [
        {
            "Sid": "Stmt1488493308547",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::281979644754:user/sample-user"
            },
            "Action": [
                "s3:ListBucket",
                "s3:ListBucketVersions",
                "s3:GetBucketLocation",
                "s3:Get*",
                "s3:Put*"
            ],
            "Resource": "arn:aws:s3:::img-bucket-00123"
        }
    ]
}
```

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:PutObject",
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::*"
            ]
        }
    ]
}
```

```
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>POST</AllowedMethod>
    <AllowedMethod>PUT</AllowedMethod>
    <MaxAgeSeconds>3000</MaxAgeSeconds>
    <AllowedHeader>Authorization</AllowedHeader>
  </CORSRule>
</CORSConfiguration>
```

https://aws.amazon.com/cli/

```
pip
aws configure
```

It access for access id and secret key.
Then region
then default output
