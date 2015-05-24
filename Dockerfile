From aadebuger/dockerpycelery
ENV aa 1
workdir /code
CMD ["celery -A ssserver.ContainerTask task"]
