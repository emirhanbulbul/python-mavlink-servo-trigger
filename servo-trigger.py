from dronekit import connect
import time
import dronekit
import socket
import exceptions
from pymavlink import mavutil, mavwp
import pymavlink



master = mavutil.mavlink_connection('udp:127.0.0.1:14550')

master.wait_heartbeat()

master.mav.command_long_send(
    master.target_system, master.target_component,
    mavutil.mavlink.MAV_CMD_DO_SET_SERVO, 0,
    14, 20000, 0, 0, 0, 0, 0)

#If 20000 sends 3.3 v.
#If 0, it sends 0V.
