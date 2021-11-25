#!/bin/bash

# Start the first process
redis-server &

# Start the second process
cd /server && python3.9 server.py &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?
