#FROM alpine:3.15
#
#RUN apk add --no-cache bash python3 rsync pip\
#    && pip install j2cli[yaml] jinja2-ansible-filters
#
#COPY ./templates /templates
#COPY ./customize.py /customize.py
#COPY ./run.sh /usr/bin/run.sh
#
#RUN pip install -r ./requirements.txt
#COPY ./workbench.py /workbench.py
#
#ENTRYPOINT "/usr/bin/run.sh"

FROM alpine:3.15

RUN apk add --no-cache --update \
  build-base \
  bash \
  python3 \
  rsync \
  py-pip \
  freetype-dev \
  gcc \
  libffi-dev \
  openssl-dev \
  py-cffi \
  python3-dev \
  cargo \
  rust \
  tcl-dev \
  tiff-dev \
  tk-dev \
  zlib-dev \
  python3-dev \
  libffi-dev \
  libxml2-dev \
  libxslt-dev

RUN pip install j2cli[yaml] jinja2-ansible-filters PyYAML\
    cryptography click coloredlogs configparser\
    contextlib2 requests requests-toolbelt python-decouple\
    pygithub loguru tqdm pyopenssl ephemeris

COPY ./templates /templates
COPY ./customize.py /customize.py
COPY ./run.sh /usr/bin/run.sh
COPY ./workbench.py /workbench.py

WORKDIR /
RUN apk add --no-cache make build-base
RUN wget https://ftp.gnu.org/gnu/gcc/gcc-6.4.0/gcc-6.4.0.tar.gz \
    && tar -xzvf gcc-6.4.0.tar.gz

WORKDIR gcc-6.4.0
RUN ./contrib/download_prerequisites

WORKDIR ..
RUN mkdir objdir

WORKDIR objdir
RUN ./../gcc-6.4.0/configure --prefix=$HOME/GCC-6.4.0 --disable-multilib

RUN make all-gcc \
  && make all-target-libgcc \
  && make install-gcc \
  && make install-target-libgcc

ENTRYPOINT "/usr/bin/run.sh"
