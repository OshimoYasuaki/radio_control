rosservice call /motor_on

sleep 1

rosservice call /timed_motion "left_hz: 300
right_hz: 300
duration_ms: 500" && rosservice call /timed_motion "left_hz: 500
right_hz: 200
duration_ms: 500"


rosservice call /timed_motion "left_hz: 300
right_hz: 300
duration_ms: 500"


rosservice call /timed_motion "left_hz: 200
right_hz: 200
duration_ms: 500"

rosservice call /timed_motion "left_hz: 100
right_hz: 100
duration_ms: 500"


sleep 1

rosservice call /motor_off
