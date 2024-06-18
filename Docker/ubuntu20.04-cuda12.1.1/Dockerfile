FROM nvidia/cuda:12.1.1-cudnn8-devel-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive

###################################### basic-tool #####################################
RUN apt-get update && \
    apt-get install -q -y --no-install-recommends \
    tzdata \
    dirmngr \
    gnupg2 \
    git \
    vim \
    less \
    curl \
    wget \
    sudo \
    cmake \
    net-tools \
    lsb-release \
    build-essential \
    bash-completion \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

###################################### python3 #####################################
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip setuptools
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY entrypoint_setup.sh /
ENTRYPOINT ["/entrypoint_setup.sh"]