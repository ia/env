
i=1; while [ $i -lt 256 ] ; do echo "iroute $i.0.0.0 255.0.0.0" | sudo tee -a client3 ; i=$((i+1)); done;
client3
