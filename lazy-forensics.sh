#!/bin/bash

usage () {
    echo "Usage: $0 [directory]"
}

if [ $# -eq 0 ]
  then
    usage
  else
    if [ ! -d "$1" ]
      then
        usage
      else
        echo "filename,userid,user,birthH,birthE,accessH,accessE,modH,modE,stchangeH,stchangeE" ; find $1 -type f -exec stat --printf="%n,%u,%U,%w,%W,%x,%X,%y,%Y,%z,%Z\n" '{}' \;
    fi
fi
