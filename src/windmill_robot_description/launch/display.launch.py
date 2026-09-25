from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    pkg_share = FindPackageShare('windmill_robot_description')
    default_model = PathJoinSubstitution([pkg_share, 'urdf', 'ugv.urdf.xacro'])
    model = LaunchConfiguration('model')

    return LaunchDescription([
        DeclareLaunchArgument('model', default_value=default_model),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': ParameterValue(Command(['xacro ', model]), value_type=str)}],
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen',
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', PathJoinSubstitution([pkg_share, 'rviz', 'ugv.rviz'])],
        ),
    ])
