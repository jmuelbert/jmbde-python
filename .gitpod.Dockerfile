FROM gitpod/workspace-full-vnc

USER gitpod

RUN sudo apt-get update \
    && rm -rf /var/lib/apt/lists/*
