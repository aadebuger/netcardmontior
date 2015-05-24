From aadebuger/dockerpycelery
ENV C_FORCE_ROOT 1
add src/main/python /code
workdir /code
CMD ["celery","-A","ssserver.ContainerTask","worker","--loglevel=info"]
