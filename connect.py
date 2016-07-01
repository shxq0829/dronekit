from dronekit import connect

vehicle = connect('127.0.0.1:5760', wait_ready=True)
