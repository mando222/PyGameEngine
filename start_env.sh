#!/usr/bin/env bash

while test $# -gt 0; do
        case "$1" in
                -h|--help)
                        echo "$package - attempt to capture frames"
                        echo " "
                        echo "$package [options] application [arguments]"
                        echo " "
                        echo "options:"
                        echo "-h, --help                show brief help"
                        echo "-a, --activate  starts the python inviroment"
                        echo "-i, --install  installs the python inviroment"
                        exit 0
                        ;;
                -a|--activate)
                    source venv/bin/activate
                    ;;
                -i|--install)  
                    pip install virtualenv
                    virtualenv -p /usr/local/bin/python3 venv
                    ;;
                *)
                        break
                        ;;
        esac
done