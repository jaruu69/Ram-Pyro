FROM hitokizzy/geezram:slim-buster

RUN git clone -b main https://github.com/zarszs/Ram-Pyro /home/rams/
WORKDIR /home/rams

RUN wget https://raw.githubusercontent.com/zarszs/Ram-Pyro/main/requirements.txt \
    && pip3 install --no-cache-dir --use-deprecated=legacy-resolver -r requirements.txt \
    && rm requirements.txt

CMD bash start
