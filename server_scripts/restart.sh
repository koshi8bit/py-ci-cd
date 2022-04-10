python abc.py
docker load < ~/dockers/back_automatic_build.tar.gz
docker stop back && docker rm back
docker run -p 5000:5000 -d --name back koshi8bit/back_automatic_build:latest