poetry install
wget https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth
mv s3fd-619a316812.pth Wav2Lip/face_detection/detection/sfd/s3fd.pth
wget https://get.station307.com/WhuFlIyLM2d/wav2lip.pth
mv wav2lip.pth Wav2Lip/checkpoints/
poetry run python voice/setup.py

