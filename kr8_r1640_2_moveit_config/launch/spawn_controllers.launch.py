from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_spawn_controllers_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("kr8_r1640-2", package_name="kr8_r1640_2_moveit_config").to_moveit_configs()
    return generate_spawn_controllers_launch(moveit_config)
