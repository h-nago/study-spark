FROM debian:buster 
RUN apt-get update -y
RUN apt-get install python3 python3-pip -y
RUN pip3 install pyspark==3.0.1
SHELL ["bash", "-c"]
RUN apt-get install curl unzip zip -y
RUN curl -s "https://get.sdkman.io" | bash
# RUN source "$HOME/.sdkman/bin/sdkman-init.sh" && sdk install java 11.0.9-amzn
RUN source "$HOME/.sdkman/bin/sdkman-init.sh" && sdk install java 8.0.272-amzn
ENV PYSPARK_PYTHON=python3
RUN apt-get install wget procps -y
RUN wget https://ftp.riken.jp/net/apache/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz
RUN tar xvzf spark-3.0.1-bin-hadoop2.7.tgz
ENV SDKMAN_DIR="/root/.sdkman"
WORKDIR /spark-3.0.1-bin-hadoop2.7