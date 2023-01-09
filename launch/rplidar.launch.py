import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    serial_baudrate = LaunchConfiguration('serial_baudrate', default='115200')
    return LaunchDescription([

         DeclareLaunchArgument(
            'serial_baudrate',
            default_value=serial_baudrate,
            description='Specifying usb port baudrate to connected lidar'),

        Node(
            package='sllidar_ros2',
            executable='sllidar_node',
            output='screen',
            parameters=[{
                'serial_port': '/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.4:1.0-port0',
                'serial_baudrate': serial_baudrate, 
                'frame_id': 'laser_frame',
                'angle_compensate': True,
                # 'inverted': False,
                'scan_mode': 'Standard'
            }]
        )
    ])
