from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlebot3_gazebo',
            executable='turtlebot3_fake',
            name='turtlebot3_fake',
        ),
        Node(
            package='turtlebot3_teleop',
            executable='turtlebot3_teleop_key',
            name='turtlebot3_teleop_key',
            output='screen',
        ),
    ])
