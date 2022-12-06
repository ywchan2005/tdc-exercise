FROM python

RUN pip3 install git+https://github.com/bp-kelley/descriptastorus
RUN pip3 install DeepPurpose
RUN pip3 install PyTDC
RUN pip3 install xgboost

WORKDIR /root
COPY metrics/*.py metrics/
COPY models/*.py models/
COPY utils/*.py utils/
COPY *.py .
COPY entrypoint.sh .
ENTRYPOINT ./entrypoint.sh
