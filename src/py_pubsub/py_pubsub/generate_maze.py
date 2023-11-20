import os

# Parameters
map_size = (2.5, 2.5)
grid_size = 0.5
robot_start_position = (map_size[0] / 2, map_size[1] / 2)
exit_position = (0, map_size[1] / 2)  # Exit point on the left side

# Create Gazebo world file content
world_content = f"""
<sdf version="1.6">
  <world name="default">
    <include>
      <uri>model://ground_plane</uri>
    </include>
    <include>
      <uri>model://sun</uri>
    </include>
"""

# Create grid structure
for i in range(-2, 3):
    for j in range(-2, 3):
        x = i * grid_size
        y = j * grid_size
        # Add walls (assuming wall model exists in Gazebo models)
        world_content += f"""
    <include>
      <uri>model://wall</uri>
      <pose>{x} {y} 0 0 0 0</pose>
    </include>
"""

# Add robot and exit point
world_content += f"""
    <include>
      <uri>model://your_robot_model</uri>
      <pose>{robot_start_position[0]} {robot_start_position[1]} 0 0 0 0</pose>
    </include>
    <include>
      <uri>model://exit_point</uri>
      <pose>{exit_position[0]} {exit_position[1]} 0 0 0 0</pose>
    </include>
  </world>
</sdf>
"""

# Save world file
world_filename = "maze.world"
with open(world_filename, "w") as f:
    f.write(world_content)

print(f"Generated Gazebo world file: {world_filename}")
