poetry install
wget https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth
mv s3fd-619a316812.pth Wav2Lip/face_detection/detection/sfd/s3fd.pth
poetry run python Real-Time-Voice-Cloning/setup.py

