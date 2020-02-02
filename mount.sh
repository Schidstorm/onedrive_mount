#!/bin/sh

path="/onedrive2"
mkdir -p $path
python3 src/onedrive_mount.py -o auto_unmount -o uid=`id -u` -o allow_other -d $path