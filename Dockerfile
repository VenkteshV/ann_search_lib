FROM ubuntu:20.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository universe
RUN apt-get install -y \
    apache2 \
    libopenblas-base \
    libomp-dev \
    curl \
    git \
    build-essential \
    wget \
    python3.8 \
    python3-pip
COPY requirements.txt ./requirements.txt
COPY src ./src

# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
     /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

RUN conda install -c pytorch/label/nightly faiss-cpu

Run pip install -r requirements.txt