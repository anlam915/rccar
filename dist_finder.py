import rospy
import math
from sensor_msgs.msg import LaserScan
# make pid intput message

desired_trajectory = 1
velocity = 30

pub = rospy.Publisher('error', pid_input, queue_size = 10)

# Function: getRange
# Parameters: the lidar LaserScan msg, and desired angle to find distance
# Output: the distance at angle theta

def getRange(data,theta):
# Get distance at theta
	

# function: callback
# performs getRange at angle 0 and theta to calculate error
def callback(data)
	theta = 25;
	a = getRange(data, theta);
	b = getRange(data, 0);
	swing = math.radians(theta);

	#implement distance finding equations

	# end

	# store calculated values into a message and publish
	msg = pid_input();			
	msg.pid_error = error;
	msg.pid_vel = vel;
	pub.publish(msg);

if __name__ == '__main__':
	print("Distance finder node")
	rospy.init_node('dist_finder', anonymous = True)
	rospy.Subscriber("scan", LaserScan, callback)		# this node subscribes to the lidar_scan topic
	rospy.spin()