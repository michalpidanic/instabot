1. vim secrets.json
```
{
  "USERNAME":"username",
  "PASSWORD":"password"
}
```
2. docker build -t bot .
3. docker run -v /home/ubuntu/instabot/InstaPy/:/root/InstaPy -d --name=instabot --restart=unless-stopped bot