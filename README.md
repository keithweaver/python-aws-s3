# python-aws-s3

## About

This is a demo of setting up an Amazon Web Service (AWS) S3 bucket and uploading a file with Python.

## Setting Up Bucket

Open [AWS Console](https://aws.amazon.com/console/) and log in.

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/1.png?token=AGNQQB4Q7sizjmFqsAVZq3V_sN8TMRFLks5YwerPwA%3D%3D "Logo Title Text 1")

Click the `Services` dropdown and select the `S3` service.

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/2.png?token=AGNQQNz_t6F17wj-SFdtfMyDoIajZS_0ks5YweyxwA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/3.png?token=AGNQQJstPfN74ZaU0DAGs48onSsPTqsjks5YwezAwA%3D%3D "Logo Title Text 1")

Click `Create Bucket`. Give it a name, region then hit next through each step.

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/4.png?token=AGNQQLW_rjSbf4dhVQzVyf9K82ftwDGXks5YwezYwA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/5.png?token=AGNQQD4kg2EX_ZXz6jNEQOl03rXmi4g6ks5YwezIwA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/6.png?token=AGNQQBiuGeGun0prBmDnWfCGS7txhGqCks5YweztwA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/7.png?token=AGNQQKrDpZNUvJ_1BSsAxBTL4z-F-9yzks5Ywez6wA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/8.png?token=AGNQQLY2H-I-DXKgioN3a_sSZa0RvA9vks5Ywe0RwA%3D%3D "Logo Title Text 1")

Now click your new bucket

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/9.png?token=AGNQQIF3ijNHUArFfOIKmDqQLesD-0xDks5Ywe06wA%3D%3D "Logo Title Text 1")

Upload a test image to your bucket

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/10.png?token=AGNQQNvBtD2xdq2lEv-0nPOSd4lr_HcUks5Ywe1IwA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/11.png?token=AGNQQJ7uOOASpUpWvH17LFx1hUf2gn-Nks5Ywe1UwA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/12.png?token=AGNQQJ5neNpGcIPRJruFgoLHluLHjfzSks5Ywe1pwA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/13.png?token=AGNQQPvo-Kz8gzLdfDzuJFTDqHOw7zZ9ks5Ywe12wA%3D%3D "Logo Title Text 1")

You can find your new file. If you click it, you should see a link. Open the link in a new tab.

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/14.png?token=AGNQQPBk3nKWXD5dLMty1mbSz_wq4Towks5Ywe2MwA%3D%3D "Logo Title Text 1")

As you can see, you'll get "Access Denied".

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/15.png?token=AGNQQBPsYqTSH6PhLfvI_JcpDzkuZE3pks5Ywe2bwA%3D%3D "Logo Title Text 1")

Click the file, and under "more" press make public. Refresh the link.

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/16.png?token=AGNQQNKjd5GvP2Wnh8f5JGTYV1AfVIhfks5Ywe2mwA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/17.png?token=AGNQQB9N71ROMur-mOpgYYbJnD8_tGiHks5Ywe2zwA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/18.png?token=AGNQQDZfL40P0kDRLMraNNS1gNjT15ARks5Ywe27wA%3D%3D "Logo Title Text 1")


Now click `Services` then go to `IAM` dashboard.

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/19.png?token=AGNQQMLc53mftbit-GS4dB848a1P0wxxks5Ywg5PwA%3D%3D "Logo Title Text 1")


You should see your `IAM` dashboard. On the left menu, you can click `Users`.

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/20.png?token=AGNQQFZWACEcI0OCPGlI8VFfKYojrNOdks5Ywg5cwA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/21.png?token=AGNQQHJ8cTd2pp9gjLJFo-9YP9M26CjJks5Ywg5pwA%3D%3D "Logo Title Text 1")


Click the `Add User`.

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/22.png?token=AGNQQHb97i8061Z8yyk7wgNoBzKEdjWCks5Ywg54wA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/23.png?token=AGNQQGmUhdp8lvITugT3O6QuF95bDecxks5Ywg6GwA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/24.png?token=AGNQQEfgNzexuJsc6SrmSQ3Op6Z2hjpeks5Ywg6YwA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/25.png?token=AGNQQBJMq9cmkWyerv0lKoiK7FLyQrVMks5Ywg6swA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/26.png?token=AGNQQK_yGtNWgoPTm-PVRMaUY4SPN80bks5Ywg7EwA%3D%3D "Logo Title Text 1")


Now click your new user from the list of users.

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/27.png?token=AGNQQP44HDGnKbF_qF55ERkBp2qZ9w6-ks5Ywg7UwA%3D%3D "Logo Title Text 1")


Copy the User ARN

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/28.png?token=AGNQQOphRJzEZzkfFy8zNwowoQmk3SXOks5Ywg7hwA%3D%3D "Logo Title Text 1")


Reopen the S3 dashboard

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/29.png?token=AGNQQFxnq6FxO5TyZuI7stDN4sicpf4lks5Ywg7swA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/30.png?token=AGNQQMNL9wrpk7q59xyNIsYGEh3QdTwyks5Ywg8KwA%3D%3D "Logo Title Text 1")


Now click the permissions tab.

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/31.png?token=AGNQQPPvYEoQ5UYrW1gC66w_fPVrTZjEks5Ywg8UwA%3D%3D "Logo Title Text 1")


Then click Bucket Policy.

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/32.png?token=AGNQQNpX1_U-waAnhxbVZlxZW4PZk8liks5Ywg8iwA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/33.png?token=AGNQQMXZnAR1uU1IG-2_HztGgvg8xId7ks5Ywg87wA%3D%3D "Logo Title Text 1")


Set your Bucket Policy to be the same as below. Change `arn:aws:iam::281979644754:user/sample-user` to be your User ARN. Also change `arn:aws:s3:::img-bucket-00123` to your Bucket ARN. The bucket ARN is above the textarea.
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

Click CORS configuration and add the following policy:
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


Reopen the `IAM` dashboard.

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/34.png?token=AGNQQHJ_DYvOXj-GDK0M6tOSzChGt18rks5Ywg9NwA%3D%3D "Logo Title Text 1")


Open your new user.

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/35.png?token=AGNQQLB9HYxUyOs324GT_gIT72Kp-aLUks5Ywg9lwA%3D%3D "Logo Title Text 1")


Click on the `New inline policy`

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/36.png?token=AGNQQMBE1OAZSRrf6GA2X-lYyNKAMh_hks5Ywg9xwA%3D%3D "Logo Title Text 1")

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/37.png?token=AGNQQGWZA9403bBqVmocrO2D2Ht3cgATks5Ywg-FwA%3D%3D "Logo Title Text 1")


Update the policy to be as follows:
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
git clone https://github.com/keithweaver/python-aws-s3.git
cd python-aws-s3
python example.py
```

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/40.png?token=AGNQQLDaMw4p1lrb003wBahAe_bRngFqks5Ywg-5wA%3D%3D "Logo Title Text 1")

```
python example-w-folder-create.py
```

![alt text](https://raw.githubusercontent.com/keithweaver/python-aws-s3/master/images-for-setup/41.png?token=AGNQQOElPIcg_RfAje3l2ZJSFjqA4Umrks5Ywg_BwA%3D%3D "Logo Title Text 1")
