FROM mrismanaziz/man-userbot:buster

RUN git clone -b main https://github.com/Yansaii/BdrlUserbot /home/bdrluserbot/ \
    && chmod 777 /home/bdrluserbot \
    && mkdir /home/bdrluserbot/bin/

COPY ./sample_config.env ./config.env* /home/bdrluserbot/

WORKDIR /home/bdrluserbot/

CMD ["python3", "-m", "userbot"]
