to_tar = $1

rm -r "$1.tar.gz"
tar -cvzf "$1.tar.gz" $1 --exclude="__pycache__"