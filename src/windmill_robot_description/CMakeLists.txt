cmake_minimum_required(VERSION 3.8)
project(windmill_robot_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY urdf launch rviz worlds params
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
