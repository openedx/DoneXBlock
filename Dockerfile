FROM openedx/xblock-sdk
RUN mkdir -p /usr/local/src/DoneXBlock
VOLUME ["/usr/local/src/DoneXBlock"]
RUN apt-get update && apt-get install -y gettext
RUN echo "pip install -r /usr/local/src/DoneXBlock/requirements.txt" >> /usr/local/src/xblock-sdk/install_and_run_xblock.sh
RUN echo "pip install -e /usr/local/src/DoneXBlock" >> /usr/local/src/xblock-sdk/install_and_run_xblock.sh
# DoneXBlock currently doesn't support translation
# RUN echo "cd /usr/local/src/DoneXBlock && make compile_translations && cd /usr/local/src/xblock-sdk" >> /usr/local/src/xblock-sdk/install_and_run_xblock.sh
RUN echo "python manage.py migrate" >> /usr/local/src/xblock-sdk/install_and_run_xblock.sh
RUN echo "exec python /usr/local/src/xblock-sdk/manage.py \"\$@\"" >> /usr/local/src/xblock-sdk/install_and_run_xblock.sh
RUN chmod +x /usr/local/src/xblock-sdk/install_and_run_xblock.sh
ENTRYPOINT ["/bin/bash", "/usr/local/src/xblock-sdk/install_and_run_xblock.sh"]
CMD ["runserver", "0.0.0.0:8000"]
