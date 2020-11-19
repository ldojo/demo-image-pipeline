FROM registry.redhat.io/rhel8/python-38

ADD . /opt/app-root/src/
ENV VENV=/opt/app-root/src/venv

USER root
RUN cp entrypoint.sh /usr/local/bin/entrypoint
USER 1001
RUN make clean venv

# ENTRYPOINT [ "/opt/app-root/src/venv/bin/python", "push_results.py" ]
ENTRYPOINT [ "entrypoint" ]