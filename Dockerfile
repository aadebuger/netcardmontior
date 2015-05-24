From aadebuger/dockerpycelery
ENV aa 1
add src/main/python /code
workdir /code
CMD ["celery","-A","ssserver.ContainerTask","worker","--loglevel=info"]
