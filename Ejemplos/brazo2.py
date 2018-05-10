#!/usr/bin/env 

import rospy
import baxter_interface

rospy.init_node("brazo", annonymous = True)

brazo_izq = baxter_interface.Limb('left')