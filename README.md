
# USER FILE MANAGER

# Configure to run locally

```dotenv
AWS_ENDPOINT_URL=http://localhost:4566
AWS_ACCESS_KEY_ID=d811e872-ab30-45e3-8736-752f98688d1d
AWS_SECRET_ACCESS_KEY=22b018ad-12ce-4268-b565-b803ce97967d
AWS_DEFAULT_REGION= sa-east-1
```

# Exemples of curls to call routes

```bash
curl -X PUT "http://localhost:8000/uploadfile" \
-H "Content-Type: multipart/form-data" \
-F "filename=example.txt" \
-F "user_name=JohnDoe" \
-F "file=@/README.md"


```