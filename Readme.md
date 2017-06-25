


origin2 es github
origin es gitlab

# run full
docker run -p 5000:5000 -e PORT=5000  -v "$PWD":/root/face_recognition image/python python3 api.py

docker run -p 5000:5000 image/python



