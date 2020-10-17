FROM python:3

#RUN git clone https://github.com/

COPY src parcial

RUN https://github.com/Martin-Ruggeri-Bio/TP11.git && \
pip install parameterized

WORKDIR /TP11

CMD ["python3","-m" ,"unittest"]
