docker run -d --restart=always -p 25500:25500 tindy2013/subconverter:latest
sleep 10
curl http://127.0.0.1:25500/version
python smart.py