#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_in_rectangle():
    # Initialize the node
    rospy.init_node('move_turtle_in_rectangle', anonymous=True)

    # Create a publisher to send velocity commands to the turtle
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    # Set the rate of publishing messages
    rate = rospy.Rate(1)  # 1 Hz (1 second delay between each loop)
    
    # Create a Twist message to control the turtle's movement
    move_cmd = Twist()
    
    # Define rectangle dimensions
    length = 5.0  # Length of the rectangle
    width = 3.0   # Width of the rectangle
    move_duration = 5  # Time to move straight in one direction

    while not rospy.is_shutdown():
        # Move straight in the x direction (length of rectangle)
        move_cmd.linear.x = 1.0  # Forward speed
        move_cmd.angular.z = 0.0  # No rotation
        pub.publish(move_cmd)
        rospy.sleep(move_duration)  # Move for 'move_duration' seconds
        
        # Turn 90 degrees (right)
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = -1.57  # Rotate 90 degrees (in radians)
        pub.publish(move_cmd)
        rospy.sleep(1.0)  # Sleep for a second to complete the turn
        
        # Move straight in the y direction (width of rectangle)
        move_cmd.linear.x = 1.0  # Forward speed
        move_cmd.angular.z = 0.0  # No rotation
        pub.publish(move_cmd)
        rospy.sleep(move_duration)  # Move for 'move_duration' seconds
        
        # Turn 90 degrees (right)
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = -1.57  # Rotate 90 degrees (in radians)
        pub.publish(move_cmd)
        rospy.sleep(1.0)  # Sleep for a second to complete the turn
        
        # Rep

