FROM debian:unstable-20230814-slim

ARG USERNAME=starlette
ARG USER_UID=101
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --system --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    && savedAptMark="$savedAptMark sudo"

RUN set -eux; \
    apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    sudo \
    git \
    python3-virtualenv \
    libsodium-dev \
    python3-yaml \
    gnupg \
    ncat

USER $USERNAME

RUN set -eux; \
    /usr/bin/python3 -m virtualenv /home/$USERNAME/.python; \
    . /home/$USERNAME/.python/bin/activate; \
    python -m pip install --upgrade pip setuptools wheel; 

WORKDIR /app/

# RUN set -ex; \
#     echo "change_me to update starlette_auth" ; \
#     . /home/$USERNAME/.python/bin/activate; \
#     git clone https://github.com/accent-starlette/starlette-auth.git; \
#     cd starlette-auth; \
#     python -m pip install --upgrade -r requirements.txt; \
#     cd .. 
    
RUN set -ex; \
    echo "change_me to update starlette like_so..."; \
    git clone https://github.com/nixroxursox/starlette.git; \
    cd starlette; \
    git pull origin;

COPY  requirements.txt newreq.txt /app/starlette/ 
COPY  .bashrc /home/starlette/

USER $USERNAME

RUN set -ex; \
    cd /app/starlette \
    && . /home/$USERNAME/.python/bin/activate; \
    python -m pip install -r requirements.txt;

RUN set -eux; \
    sudo apt-get update

RUN set -ex; \
    cd /app/starlette \
    && . /home/$USERNAME/.python/bin/activate; \
    python -m pip install -r newreq.txt;


WORKDIR /app/website

CMD ["/home/starlette/.python/bin/gunicorn", "app:app", "--workers", "6", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "unix:/tmp/eCom.sock", "--backlog", "1024", "--threads", "24", "--access-logfile", "/proc/self/fd/1", "--error-logfile", "/proc/self/fd/2", "--log-level", "debug"]
#CMD ["/home/starlette/.python/bin/python", "app.py"]
