FROM mrismanaziz/man-userbot:buster

RUN git clone -b main https://github.com/Yansaii/Bdrl-Ubot /home/bdrlubot/ \
    && chmod 777 /home/cilikuserbot \
    && mkdir /home/bdrlubot/bin/

COPY ./sample_config.env ./config.env* /home/bdrlubot/

WORKDIR /home/bdrlubot/

CMD ["python3", "-m", "userbot"]
