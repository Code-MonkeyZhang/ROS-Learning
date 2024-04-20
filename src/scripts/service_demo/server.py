#!/usr/bin/env python3
from ros_basics_tutorials.srv import AddTwoInts
from ros_basics_tutorials.srv import AddTwoIntsRequest
from ros_basics_tutorials.srv import AddTwoIntsResponse

import rospy

def handle_add_two_ints(req):
    sum=req.a+req.b
    print("Returning [%s+%s=%s]"%(req.a,req.b,sum))
    return AddTwoIntsResponse(sum)

def add_two_ints_sever():
    rospy.init_node("add_two_ints_sever")
    # (A,B,C) A: name B: type C: callback func
    s=rospy.Service('add_two_ints',AddTwoInts,handle_add_two_ints) 
    print("Ready to recive two ints")
    rospy.spin()
if __name__ == "__main__":
    add_two_ints_sever() 