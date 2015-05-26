From aadebuger/dockerpycelery
ENV C_FORCE_ROOT 1
#run apt-get -y install git
#run git clone https://github.com/aadebuger/netcardmontior /temp
#run cp /temp/src/main/python /code
add ./main/python /code
workdir /code
CMD ["celery","-A","ssserver.ContainerTask","worker","--loglevel=info"]
