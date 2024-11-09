#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_in_rectangle():
    
    rospy.init_node('move_turtle_in_rectangle', anonymous=True)

    
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    
    rate = rospy.Rate(1)  
    
    
    move_cmd = Twist()
    move_duration = 4.999999
    n = 2  

    while n != 0:
        
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 1.57  
        pub.publish(move_cmd)
        rospy.sleep(1.0)
        n = n-1  
        
        
        
        move_cmd.linear.x = 3.0  
        move_cmd.angular.z = 0.0  
        pub.publish(move_cmd)
        rospy.sleep(move_duration)  
        
        
        
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 1.57  
        pub.publish(move_cmd)
        rospy.sleep(1.0)  
        
        
        
        move_cmd.linear.x = 3.0  
        move_cmd.angular.z = 0.0  
        pub.publish(move_cmd)
        rospy.sleep(move_duration)  
        
        

if __name__ == '__main__':
    try:
        move_in_rectangle()
    except rospy.ROSInterruptException:
        pass

