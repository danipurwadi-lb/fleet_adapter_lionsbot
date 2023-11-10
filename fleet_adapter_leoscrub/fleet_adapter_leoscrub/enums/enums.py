from enum import Enum
from enum import IntEnum

class RobotStatus(Enum):
    CLEANING = "Cleaning"
    CLEANING_PAUSED = "Cleaning Paused"
    RESTING = "Resting"
    MOVING = "Moving"
    MOVING_PAUSED = "Moving Paused"
    DOCKED = "Docked"

class RobotMissionStatus(Enum):
    APP_STARTED = "APP_STARTED"
    CLEANING_FINISHED = 'ROBOT_CLEANING_FINISHED'
    MOVING_TO_WORK_STOPPED = 'ROBOT_MOVING_TO_WORK_STOPPED'
    APP_CLEANING_STOPPED = 'APP_CLEANING_STOPPED'
    CLEANING_STOPPED = 'ROBOT_CLEANING_STOPPED'
    ROBOT_EXITED = 'ROBOT_EXITED_FINISHED'
    APP_WAITING_FOR_LIFT_STOPPED = 'APP_WAITING_FOR_LIFT_STOPPED'
    APP_ENTERING_LIFT_STOPPED = 'APP_ENTERING_LIFT_STOPPED'
    APP_IN_LIFT_STOPPED = 'APP_IN_LIFT_STOPPED'
    APP_EXITING_LIFT_STOPPED = 'APP_EXITING_LIFT_STOPPED'
    APP_EXITED_LIFT_FINISHED_STOPPED = 'APP_EXITED_LIFT_FINISHED_STOPPED'
    E_STOP_PRESSED = 'USER_E_STOP_PRESSED'
    IN_CRITICAL = 'ROBOT_IN_CRITICAL'
    ROBOT_MOVING_TO_DOCK_STOPPED = 'ROBOT_MOVING_TO_DOCK_STOPPED'
    MOVING_FINISHED = 'ROBOT_MOVING_FINISHED'
    APP_STOPPED = 'APP_STOPPED'
    MOVING_STOPPED = 'ROBOT_MOVING_STOPPED'
    MOBVING_FINISHED = 'ROBOT_MOVING_FINISHED'
    APP_MOVING_TO_DOCK_STOPPED = 'APP_MOVING_TO_DOCK_STOPPED'
    APP_DOCKING_STOPPED = 'APP_DOCKING_STOPPED'
    APP_MOVING_TO_WORK_STOPPED = 'APP_MOVING_TO_WORK_STOPPED'
    CMD_REJECTED = 'CMD_REJECTED'
    ROBOT_DOCKING_STOPPED = 'ROBOT_DOCKING_STOPPED'
    ROBOT_MOVING = 'ROBOT_MOVING'


class Topic(Enum):
    RMF_LITTER = "rmf_litter"
    LB_TASKS_REQUEST = "lb_task_api_requests"
    DOCK_SUMMARY = "dock_summary"

class ResponseCode(IntEnum):
    # Success
    # leo bot does not have a success code when it moves/clean

    # Error
    UNABLE_TO_PLAN_PATH = 3101
    DESTINATION_TOO_NEAR = 3102

class NavigateStatus(Enum):
    MOVING = "MOVING"
    TOO_CLOSE = "TOO_CLOSE"
    FAILED = "FAILED"
    NONE = "NONE"

class NavigationCompleteStatus(Enum):
    NONE = "NONE"
    MOVING_COMPLETED = "MOVING_COMPLETED"
    MOVING_INPROGRESS = "MOVING_INPROGRESS"