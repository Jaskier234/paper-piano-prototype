docker run -it --rm --name paper-piano \
    --net=host --ipc=host \
    --cpus="1.0" \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v "$PWD":/usr/src/myapp \
    -w /usr/src/myapp paper_piano python3 $1
