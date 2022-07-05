FROM python:3.10.0

WORKDIR /app

COPY requirements.txt .

####### I had some erros and I found a solution instolling opencv-python
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install opencv-python
#######

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]