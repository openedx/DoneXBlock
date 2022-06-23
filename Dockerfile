FROM openedx/xblock-sdk
RUN mkdir -p /usr/local/src/DoneXBlock
VOLUME ["/usr/local/src/DoneXBlock"]
RUN apt-get update && apt-get install -y gettext
RUN make install

ENTRYPOINT ["/bin/bash", "/usr/local/src/DoneXBlock/scripts/install_and_run_xblock.sh"]

CMD ["runserver", "0.0.0.0:8000"]
