import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    pkg = FindPackageShare('windmill_robot_description')
    gz_pkg = FindPackageShare('ros_gz_sim')

    model_arg = DeclareLaunchArgument('model',
        default_value=PathJoinSubstitution([pkg,'urdf','ugv.urdf.xacro']))
    world_arg = DeclareLaunchArgument('world',
        default_value=PathJoinSubstitution([pkg,'worlds','windfarm_empty.sdf']))

    model = LaunchConfiguration('model')
    world = LaunchConfiguration('world')

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([gz_pkg,'launch','gz_sim.launch.py'])),
        launch_arguments={'gz_args':[world,' -r -v3']}.items())

    robot_description = ParameterValue(Command(['xacro ',model]),value_type=str)

    rsp = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description':robot_description,'use_sim_time':True}])

    spawn = TimerAction(period=4.0, actions=[
        Node(package='ros_gz_sim', executable='create',
             output='screen',
             arguments=['-topic','robot_description',
                        '-name','windmill_ugv',
                        '-x','0','-y','0','-z','0.15'])])

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        output='screen',
        parameters=[{'config_file':PathJoinSubstitution([pkg,'params','bridge.yaml']),
                     'use_sim_time':True}])

    image_bridge = Node(
        package='ros_gz_image',
        executable='image_bridge',
        output='screen',
        arguments=['/camera/image_raw'],
        parameters=[{'use_sim_time':True}])

    return LaunchDescription([
        model_arg, world_arg,
        gazebo, rsp, spawn, bridge, image_bridge])
