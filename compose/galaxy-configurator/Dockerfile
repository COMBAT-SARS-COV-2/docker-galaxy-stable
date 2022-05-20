FROM alpine:3.15

RUN apk add --no-cache bash python3 rsync pip\
    && pip install j2cli[yaml] jinja2-ansible-filters

COPY ./templates /templates
COPY ./customize.py /customize.py
COPY ./run.sh /usr/bin/run.sh

RUN pip install -r ./requirements.txt
COPY ./workbench.py /workbench.py

ENTRYPOINT "/usr/bin/run.sh"

#FROM alpine:3.15
#
#RUN apk add --no-cache bash python3 rsync py-pip \
#    && pip install j2cli[yaml] jinja2-ansible-filters PyYAML
#
#
#RUN apk add --update \
#  build-base \
#  freetype-dev \
#  gcc \
#  libffi-dev \
#  openssl-dev \
#  py-cffi \
#  python3-dev \
#  cargo \
#  rust \
#  tcl-dev \
#  tiff-dev \
#  tk-dev \
#  zlib-dev
#
#COPY ./templates /templates
#COPY ./customize.py /customize.py
#COPY ./run.sh /usr/bin/run.sh
#COPY ./workbench.py /workbench.py
##COPY ./requirements.txt /requirements.txt
#
#WORKDIR /
#
#RUN apk add --no-cache make build-base
#RUN wget https://ftp.gnu.org/gnu/gcc/gcc-6.4.0/gcc-6.4.0.tar.gz
#RUN tar -xzvf gcc-6.4.0.tar.gz
#WORKDIR gcc-6.4.0
#RUN ./contrib/download_prerequisites
#WORKDIR ..
#RUN mkdir objdir
#WORKDIR objdir
#RUN ./../gcc-6.4.0/configure --prefix=$HOME/GCC-6.4.0 --disable-multilib
#RUN make all-gcc
#RUN make all-target-libgcc
#RUN make install-gcc
#RUN make install-target-libgcc
#RUN apk add python3-dev libffi-dev
#
#RUN pip install cryptography click coloredlogs configparser\
#    contextlib2 requests requests-toolbelt python-decouple\
#    pygithub loguru tqdm pyopenssl
#
#ENTRYPOINT "/usr/bin/run.sh"
