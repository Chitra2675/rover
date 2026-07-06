# Autonomous LiDAR Rover

Final year B.Tech project — autonomous ground rover with LiDAR-based SLAM and Nav2 navigation.

## Stack
- ROS 2 Humble + Gazebo 11
- RPLiDAR A1M8 (360 deg SLAM)
- Raspberry Pi 5 (ROS host) + Jetson Orin Nano (AI brain)
- Cytron MDD10A motor drivers + 12V encoded motors
- slam_toolbox + Nav2

## Workspace structure
- `src/rover_description` — URDF robot model
- `src/rover_bringup` — launch files and configs
- `src/rover_control` — motor controller node
- `maps/` — saved SLAM maps
- `docs/` — notes and references

## Status
- [x] ROS 2 + Gazebo simulation environment verified
- [x] TurtleBot3 SLAM and TF pipeline verified
- [ ] Custom rover URDF
- [ ] SLAM on custom model
- [ ] Nav2 autonomous navigation
- [ ] Hardware integration
