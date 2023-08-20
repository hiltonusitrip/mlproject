CONTAINER="/mltest"
if [ "$(docker ps -a | grep -c $CONTAINER)" -gt 0 ]; then
    docker rm -f $CONTAINER
fi