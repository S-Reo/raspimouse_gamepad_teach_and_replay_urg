#! /usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

#/scan トピックからデータをsubscribe
#とりあえず2値取得して差分でモータ直進
sensor_values = LaserScan()
rospy.init_node('running_with_lidar')

def sensor_callback(messages):
    sensor_values = messages
    print (len(sensor_values.ranges), sensor_values.ranges[513], sensor_values.ranges[341], sensor_values.ranges[170])

rospy.Subscriber('/scan', LaserScan, sensor_callback)


rospy.spin()
