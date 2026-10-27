# Project Tracking

## Description

- Group 1, Team 5
- Team Name: Thé-Lait-Café lovers

### Members:

- Tom Dugail
- Teammate_1
- Teammate_2
- Teammate_3

### Strengths and Weaknesses:

*List what you believe to be your team’s strengths and weaknesses. This will not be graded but may help you when designing your schedule and assigning tasks.*

#### Strengths

- We come from different academic backgrounds (MP, MPI, PSI, BTS), so we have a wide range of skills.
- We communicate well with each other and within the group.
- Our priority is the robot’s performance and reliability.

#### Weaknesses

- We’re not artists, and we don’t want to spend time on the robot’s decoration.

## Task Allocation and Initial Schedule

Indicate the task lead and **estimated dates** for the following versions:

- **V0**: initial prototypes for testing and experimentation, without a well-defined structure
- **V1**: functional code, structured but independent of other tasks
- **V2**: functional code integrated into the whole system

The task lead must ensure that the deadlines are met. They are not necessarily the only person working on this task.

**Note**:
- There must be a single task lead per task
- Completion of each task by the specified date will be verified (by the tutor or the judging panel)
- If you **add an additional task**, be sure to **check with your tutor**


| Task                 | In charge      | V0 (planned)  | V0 (completed)  | V1 (planned)  | V1 (completed)  | V2 (planned)  | V2 (completed)  |
| -------               | ---------------- | ----        | ----          | ----        | ----          | ---         | ---           |
| Robot design      | Group           | 30/09       | 26/09         | 14/10       | 30/09         | 24/10       | 24/10         |
| Rasberry config.      | Teammate_3 | 26/09       | 26/09         | 30/09       | 30/09         | 14/10       | 25/10         |
| Control and movement | Teammate_2 | 14/10       | 12/11         | 24/10       | 24/10         | 19/11       | 25/10         |
| Ctrl logic and tracking | Tom Dugail       | 24/10       | 24/10         | 12/11       | 24/10         | 19/11       | 25/10         |
| Ctrl Web Interface    | Teammate_1     | 24/10       | 24/10         | 12/11       | 24/10         | 19/11       | 25/10         |
| Flag detection     | Teammate_3 | 24/10       | 12/11         | 12/11       | 24/10         | 19/11       | 25/10         |

## Version Descriptions

### V0

- Robot design: Determining component placements (camera, Raspberry Pi, wheels, etc.) and selecting the chassis shape.
- Raspberry Pi Configuration: Configuring the Raspberry Pi’s operating system.
- Motion Control: Initial motor tests, camera tests, battery tests.
- Control Logic and Tracking: Creating a server with no additional features but capable of communicating.
- Web Interface and Control: Simple buttons for controlling the robot, basic front end.
- Beacon Detection: Camera tests, image capture.

### V1

- Robot design: SVG file with the main plates; adding mounting holes.
- Raspberry Pi configuration: Connecting the Raspberry Pi to the school network.
- Motion control: Control using a large Robot class.
- Control and tracking logic: Integrating the automatic algorithm.
- Web interface and control: Buttons linked to a backend; HTTP communication between different processes.
- Beacon detection: Basic QR code scanning.

### V2

- Robot design: Complete SVG file.
- Raspberry Pi configuration: All files are transferred to the Raspberry Pi and can be used remotely.
- Motion control: Approximate motor odometry.
- Control logic and tracking: Communication with the tracking server.
- Web interface and control: Clean interface, displays useful information, full integration with motor control.
- Beacon detection: High-level functions for capture

## Session Dates

| Session            | Date      |
|-------------------|-----------|
| TH 1-2            | 09/17     |
| TH 3-4            | Fri 09/26 |
| TH 5-6            | Tue 09/30 |
| TH 7-8            | Tue 10/14 |
| TH 9-10           | Fri 10/24 |
| (School Break)        |           |
| TH 11-12          | Wed, Nov 12 |
| TH 13-14 and 15-16 | Tue, Nov 18 |
| TH 17-18 and 19-20 | Wed, Nov 19 |
| TH 21-22          | Thu, Nov 20 |
| (Midterm Exam) |           |
| TH 23-24          | Wed, Nov. 26 |
| TH 25-26          | Thu, Dec. 4 |
| TH 27             | Tue, Dec. 9 |
| TH 28-29          | Fri, Dec. 19 |
| (Break)        |           |
| TH 30             | Wed, Jan 7 |
| TH 31-32          | Fri, Jan 16 |
| TH 33-34          | Thu, Jan 29 |
| TH 35-36 and 37-38 | Fri, Jan 30 |


**Please note**:
For the robot design, you must:

- have your blueprint in **SVG** format in your Git repository, in the root directory under the name **`plan_decoupe_GR_EQ.svg`**, where `GR` is your group number and `EQ` is your team number;
- have your design **approved** by your **advisor** (during or outside of office hours);
- after approval, send an email to [**Mr. Bouhier**](mailto:mickael.bouhier@telecom-paris.fr) to request the cutting.

This plan must be uploaded **no later than 10/24/2025, keeping in mind that the lead time before cutting is approximately one week**.

*Note for tutors*: Verify that the file is indeed on Git.

## Final Schedule

**To be completed after the midterm evaluation**

For each task, list the next steps and **tests** planned for the collaborative project.
These tests do not necessarily have to be the same as those of the other teams in the group.
You may add multiple entries per task.

The individuals responsible for the tasks defined in the initial schedule are responsible for the corresponding tests. Any changes **must be discussed and approved by the instructor**.


| Task                 | Assigned To | Details                                           | Date (scheduled)   | Date (completed)      |
| ---------             | ---------   | ---------                                         | --------       | --------  |
| Control | Teammate_1 | Refactoring the robot control code | 12/04 | 12/04 |
| Camera | Teammate_3 & Tom | Resolve the flag detection issue | 12/04 | 12/04 |
| Camera | Teammate_3 & Tom | Refactor the camera's high-level functions | 12/04 | 12/09 |
| Control | Teammate_2 & Teammate_1 | Optimize robot movement and calibration times | 12/04 | 12/19 |
| Web Interface | Teammate_1 | Clean up the console and robot information | 12/09 | 12/04 |
| Web Interface | Teammate_1 | Add a minimap | 12/19 | 12/04 |
| Web Interface | Teammate_3 | Add the camera view | 12/19 | 12/09 |
| Control | Teammate_1 | Set up movement tests | 12/19 | 01/15 |
| Strategy | Teammate_1 | Integrate the group’s shared Maestro code | 01/16 | 01/15 |
| Communication | Tom | Set up tracking server tests | 01/16 | 01/16 |
| Camera | Teammate_3 | Set up camera tests | 01/16 | 01/16 |
| Product Sheet | Tom | Create the robot’s product sheet | 01/28 | 01/28 |
| Camera | Teammate_2 | Point the camera downward | 01/29 | 01/29 |


## Architecture

Describe in detail here the software architecture of your program **for both evaluation stages**.
You may use a diagram.

Note in particular:

- the various algorithmic phases (image capture, calibration, motor controls, HTTP requests)
- the sequencing of these phases (use of _threads_, independent _processes_, discrete tasks)
- if applicable, how your various modules exchange data (via files, sockets, shared objects) and how concurrency between threads/processes is managed.

### Intermediate Evaluation Architecture

![Intermediate Evaluation Diagram](images/Schema%20architecture%20ARTEFACT%201.png)

The user communicates with the robot through the web interface.
This interface sends WebSocket requests to the Flask server.
The Flask server makes synchronous or asynchronous calls to the robot’s Python code (using `async`).

The automatic algorithm has three main steps:
1. Move forward 1 meter to enter the circle;
2. Perform an exhaustive search for the flags and store their positions;
3. Communicate with the server to capture the correct flags, without having to search for them.

The robot’s movement is managed as follows. For each call to `goto(x, y)`:
1. Determine the robot’s current position using triangulation with the markers;
2. Determine the robot’s orientation using one of the markers;
3. Set the robot’s orientation to 0;
4. Orient the robot toward the desired position;
5. The robot moves toward the desired position.

Virtually all modules (web, control, camera, and battery) have high-level functions, used by other modules, and low-level functions, which communicate with the physical hardware.

### Final Evaluation Architecture

![Final Evaluation Diagram](images/Schema%20architecture%20ARTEFACT%203.png)

The robot has four main modules: web, control, camera, and battery.

The user communicates with the robot through the web interface.
This interface sends WebSocket requests to the Flask server.
The Flask server makes synchronous or asynchronous calls to the robot’s Python code (using `async`).

To integrate the common strategy, commands from the group’s shared server are routed through the `puppet.py` file in the control module.
This file ensures consistency between the basic tasks required by the common strategy and the team’s corresponding implementation.

## Tests

**To be completed after the midterm evaluation**

In this section, describe in detail all the tests you have set up to validate your code.
The format is flexible, but you must document:

- what the test does
- how to run the test (or a series of tests) from the root of your Git repository.

These tests should allow you to quickly verify that a software module in your program works as expected.
It is therefore **essential** that the test directly use the code as it appears in your program, not a copy of that code.

Every task identified in the initial schedule **must have** associated tests. For the Raspberry Pi, be sure to create reinstallation scripts.

**Note**: These tests must:

- be executable automatically (if possible), that is, without human intervention other than running the initial command line,
- be able to run on any Raspberry Pi board; do not include any absolute file paths in your code or tests,
- if specific dependencies need to be installed (via pip or apt), be sure to indicate this or add an initial configuration script.


### Movement Tests

The test performs:
- a calibration
- a movement toward beacon 2
- a left/right calibration test
    - a turn in place
    - a check of the angle to beacon 2
- a forward/backward calibration test
    - a backward movement
    - a verification of the distance to beacon 2
The test result is displayed on the console

Running the test:

```bash
python3 /tests/test_controle.py
```

### Camera Tests

For a beacon B located at a measured distance of X, we verify that the camera calculates a distance
to the beacon with an error less than N

Running the test:

```bash
python3 test_cam.py B X N
```

The script returns **0** on success or **1** on failure.

### Tracking Server Tests

The test performs the following:
- Sends the position and angle specified by the user to the tracking server
Returns “success” if the request was processed successfully, if an error originated from the server, or if
the request is valid but the test has not yet started. Otherwise, returns an error

Running the test:

```bash
python3 /tests/test_pos.py X Y alpha
```

The script returns True if successful or False if it fails.


### Web client-server tests (example)

Here, we test the ability to send a “move forward” request of 30 cm and retrieve the map’s consumption.

Running the test:

```bash
python3 test_web.py “move forward” 30
```

The script returns the value 0 if the test fails, or the map’s consumption otherwise.


## Performance

*To be completed after the midterm evaluation, no later than the final evaluation*

**For example:**

- Camera+Aruco processing time in frames per second
- Latency of Camera+Aruco processing + motor action
- Average network communication latency (client/server requests, locally, via Wi-Fi, to the evaluation server)
- Camera+Aruco processing latency + server response
- Maximum robot travel speed in a straight line, m/s
- Minimum robot travel speed in a straight line, m/s >0
- Average CPU load during manual control
- Average CPU load during automatic control
- Estimated power consumption during manual control
- Estimated power consumption during automatic control

**Robot Performance:**

- Video stream latency: 0.9 s
- Average power consumption while stationary: 6 W
- Average power consumption while moving: 9 W
- Average CPU load with video stream: 25%
- Average CPU load without video stream: 1%
- Speed while moving in a straight line: 0.17 m/s


## Summary

*The summary describes your analysis of what worked, what didn’t work, and what needs to be or should be corrected. It should be completed immediately after each evaluation.*

### Interim Evaluation Summary

- Manual movement works well
- Sending and detecting position (i.e., beacons) works well
- Movement is good
- Flags are detected by a low-level camera function but not transmitted to the high-level function
- Certain time optimizations (limiting the number of unnecessary position measurements) should be considered

### Final Evaluation Summary

- 1st run: The robots connect and enter the zone, but are unable to capture any flags because the strategy isn’t working
- 2nd run: “Plan B” strategy launched (each robot covers one-quarter of the circle) and a few flags are captured

#### Single Robot Summary

- Our team’s robot can calibrate itself accurately (position and orientation)
- The robot has good odometry (it moves in a straight line, can estimate its position, etc.)
- The robot receives and executes commands from the shared code without any issues
- The web interface provides relevant information

#### Cooperation Summary

- The shared code connects successfully to all the robots and can communicate with them
- The shared code can issue commands that are executed by the robots
- The shared strategy proposed by the group did not work: it was too complicated, and it would have taken more time to fix the bugs
- The “Plan B” strategy assigned two zones to each robot so that captures could be made individually, without the need for communication *between* the robots
- The “Plan B” strategy was not thoroughly tested before the final evaluation, and bugs occurred during the evaluation

## Task Details

For each task, list the external expertise you sought (other students in the group, 1A, 2A, teachers),
the bibliographic resources used, and any other comments on how it worked.

In particular, note the various technical approaches considered,
their advantages and disadvantages, and the reasons for your technical choices (simplicity, quality of documentation, tutorials, past experience, etc.).

--------------------

### Task: Robot Design

#### Expertise


#### Bibliography

- https://urfist.unistra.fr/uploads/media/Tutoriel_inkscape_Ch-Paris.pdf (tutorial on using _Inkscape_)

#### Notes & Operation

We wanted the center of gravity to be between the two drive wheels; hence the choice of battery placement.

--------------------

### Task: Raspberry Pi—Installation and Configuration of the Board and Environment

#### Expertise

#### Bibliography

- https://discourse.r2.enst.fr/t/quel-os-pour-la-rasberry-pi/400
- https://discourse.r2.enst.fr/t/configuration-de-lacces-wifi-campus-telecom-pour-les-raspberry/430

#### Notes & Operation

--------------------

### Task: Movement Control

#### Expertise

#### Bibliography

- https://discourse.r2.enst.fr/t/carte-de-controle-moteurs/425
- https://discourse.r2.enst.fr/t/specifications-des-moteurs/424

#### Notes & Operation

The robot is controlled by the `controle` module (i.e., the folder).
All *high-level* functions for movement are contained in a `Robot` class object.
This class is located in `controle/main.py`.
It calls upon numerous *low-level* functions contained in other modules.
The `Robot` class handles the following functions in particular:
- `stop`
- `start`
- `move_forward`
- `move_backward`
- `turn_left`
- `turn_right`
- `turn`
- `dance`
- `get_status`
- `calibrate`
- `goto`
- `orient`

Many constants and initial values are defined in `control/config.py` to allow for easy modification.
The `control` module also receives commands from the shared code via the `control/puppet.py` file.

--------------------

### Task: Tracking and Control Logic

#### Expertise

#### Bibliography

- https://pypi.org/project/requests/

#### Notes & Operation

Information about the robot must be communicated to the tracking server; to avoid disrupting its operation and movement, this information is handled in an asynchronous loop.
The functions use `requests.post` to send information and `requests.get` to receive it.

--------------------

### Task: Remote Control Web Interface

#### Expertise

#### Bibliography

- https://www.videosdk.live/developer-hub/websocket/flask-websocket
- https://flask.palletsprojects.com/en/stable/async-await/
- https://developer.mozilla.org/en-US/docs/Web/API/Element/keydown_event
- https://www.w3schools.com/html/html5_canvas.asp

#### Notes & Functionality

The web interface is designed to provide as much information as possible about the robot; it includes a list of robot variables, a minimap, a console, and the camera feed.
The interface also features many buttons for issuing commands to the robot, enabling or disabling tasks, and adjusting odometry calibration values. The web interface uses little to no CSS.

--------------------

### Task: Beacon Detection

#### Expertise

#### Bibliography
https://discourse.r2.enst.fr/c/traitement-dimage/12
https://docs.opencv.org/4.x/d5/d1f/calib3d_solvePnP.html
https://docs.opencv.org/4.x/d1/dfb/intro.html
https://docs.opencv.org/4.x/d5/dae/tutorial_aruco_detection.html

#### Notes & Operation
For marker detection, everything is done via the camera using OpenCV, a Python computer vision library that enables the acquisition, processing, and interpretation of images in order to extract geometric information that can be used by a machine. Here, we used OpenCV to detect Aruco markers and to use markers with known positions to calibrate the robot. First and foremost, you must calibrate the camera to obtain its matrix and distortion coefficients.

Some aspects proved challenging because not all versions of OpenCV are compatible with our Raspberry Pi, and we also had to find an effective method to calibrate our robot in order to minimize camera error. We encountered a problem obtaining a reliable angle between the robot and the marker (the theta angle if we represent the circle in polar coordinates), as well as another problem with capturing multiple markers in a single frame.


--------------------

### Group Task: Software Architecture

#### Expertise

#### Bibliography

https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449& url=https://www.commentcoder.com/python-fichier-init/&ved=2ahUKEwj57q7RwLGSAxVwVaQEHY-jFT8QFnoECBkQAQ&usg=AOvVaw1kmYLT83cuSd7hbhg-8wUW

#### Notes & Operation

The robot has four main modules: web, control, camera, and battery.

The user communicates with the robot through the web interface.
This interface sends WebSocket requests to the Flask server.
The Flask server makes synchronous or asynchronous calls to the robot’s Python code (using `async`).

To integrate the common strategy, commands from the group’s shared server are routed through the `puppet.py` file in the control module.
This file ensures consistency between the basic tasks required by the common strategy and the team’s corresponding implementation.

--------------------

### Task: Measuring the robot’s energy consumption

#### Expertise

#### Bibliography

- https://wiki.dfrobot.com/Gravity:%20I2C%20Digital%20Wattmeter%20SKU:%20SEN0291
- https://www.dfrobot.com/product-1827.html
- https://github.com/DFRobot/DFRobot_INA219/

#### Notes & Operation

Estimation of the robot’s battery level using the voltage recorded by the wattmeter board by measuring different voltage levels (full battery, empty battery, in between, etc.) and performing a linear regression between these points. The battery percentage is displayed on the web interface.
Real-time measurement of power consumption and display on the web interface.

--------------------

## Session Follow-Up

*To keep track of your sessions, note what was done during the session and what needs to be prepared before the next session.
There’s no set format—just be sure to include the session title (_TH X-Y_).*

### TH 1-2

#### During the session

- Attendees: Teammate_2, Tom Dugail, Teammate_3, Teammate_1
- Configuration and installation of RPI OS Lite
- Connection to our group’s router
- Personal connection to the RPI via SSH

#### To be prepared for the next session

- Connection to the Campus Télécom Wi-Fi network

### TH 3-4

#### During the session

- Present: Teammate_2, Tom Dugail, Teammate_3, Teammate_1
- Attempted to connect to the Wi-Fi network but encountered connection issues via the router (“rpi15” not recognized; had to use the IP address instead)
- Began the design process; made initial design decisions

#### To be planned for the next session

- Finalize the Wi-Fi connection
- Finish designing the parts

### TH 5-6

#### During the session

- Present: Teammate_2, Tom Dugail, Teammate_1
- Uploaded the CA certificate, configured nmtui, and connected to the Campus-Telecom Wi-Fi
- Made progress on the design of the wooden plates; added holes for screws
- GitLab: added the “design” folder and the “testing” folder

#### Plans for the next session

- Soldering and connecting cables
- Testing the motors
- Starting the web page

### TH 7-8

#### During the session

- Present: Teammate_2, Tom Dugail, Teammate_3, Teammate_1
- Soldering wires and connecting cables at the FabLab
- Start of the web interface: basic Python code with Flask
- Robot design transferred to an A3 sheet

#### To be planned for the next session

- Test the motors
- Functional web page

### TH 9-10

#### Before the session

- Send the SVG plate
- Progress on the web interface

#### During the session

- Present: Teammate_2, Tom Dugail, Teammate_3, Teammate_1
- Motor testing
- Camera testing
- Tracking server testing
- Interactive web interface; basic functions work
- Pulled from Git on the RPI
- Created task-specific branches

#### To be planned for the next session

- Use the camera from the RPI
- Communication between the web interface and the motors

### TH 11-12

#### Before the session

- Progress on control and tracking

#### During the session

- Present: Teammate_2, Tom Dugail, Teammate_1
- Robot assembly
- Web interface with WebSockets
- Remote control of motors via the web interface

#### To be planned for the next session

- Motor calibration
- Using the camera from the RPI

### TH 13-14 and 15-16

#### During the session

- Present: Teammate_2, Tom Dugail, Teammate_3, Teammate_1
- Battery measurement using the wattmeter
- Algorithm for autonomous control
- Scanning beacons with the camera
- Asynchronous control functions
- Precise motor control, calibration using motor ticks

#### To be planned for the next session

- Goto and orient functions
- Integrate battery measurement with the web interface
- Integrate beacon scanning with autonomous control

### TH 17-18 and 19-20

#### During the session

- Present: Teammate_2, Tom Dugail, Teammate_3, Teammate_1
- The “orient” (rotates the robot by a given angle) and “goto” (go to a position) functions
- Implementation of battery level monitoring in the web interface
- Implementation of camera functions in the robot’s autonomous mode
- Function that enables movement tracking
- Initial tests of the autonomous robot (several minor fixes)

#### To be planned for the next session

- Test communication functions with the tracking server
- Fix the flag detection function, which does not always detect the flags

### TH 21-22

#### During the session

- Present: Teammate_2, Tom Dugail, Teammate_3, Teammate_1
- Flag detection ignores null flags
- Midterm evaluation

#### To be planned for the next session

- Fix the flag detection function
- Test the function for sending flag captures to the server

### TH 23-24

#### During the session

- Present: Teammate_2, Tom Dugail, Teammate_3, Teammate_1
- Discussion with the rest of the group about strategy
- Refactoring the control module
- Modifying the camera functions to detect multiple markers
- Ideas for optimizing the robot’s speed (avoiding recalibration with every movement, etc.)

#### To Do for the Next Session

- Test the camera and the code in the refactoring-control branch
- Implement the optimizations

### TH 25-26

#### During the Session

- Present: Teammate_2, Tom Dugail, Teammate_3, Teammate_1
- Testing the control module after refactoring
- Troubleshooting camera issues
- Rewriting the camera’s high-level functions
- Performance optimizations for robot calibration

#### To-do list for the next session

- Start working on the new web interface
- Integrate the new high-level functions into the rest of the code

### TH 27

#### Before the session

- New web interface
- Remote camera feed

#### During the session

- Present: Tom Dugail, Teammate_3, Teammate_1
- Began testing the new camera functions

#### Plans for the next session

- Finish camera testing
- Optimizations

### TH 28-29

#### During the session

- Present: Tom Dugail, Teammate_3, Teammate_2, Teammate_1
- Optimize calibration functions in controle-v3
- Merge controle-v3, web-v3, and camera-v3 and begin testing
- Update the tp-25.pem certificate

#### Things to Prepare for the Next Session

- Finish tests

### TH 30

#### During the session

- Present: Teammate_2, Teammate_1
- Discussion with the rest of the group about the common strategy
- Set up sshfs to replace VSCode’s ssh module because it was using too many resources

#### To be planned for the next session

- Finish tests

### TH 31-32

#### Before the session

- Complete movement tests for the new functions
- Improve the console on the web interface
- Add a runnable test to test movements
- Remove old code

#### During the session

- Present: Teammate_2, Teammate_1, Tom Dugail, Teammate_3
- Implementation of the shared Maestro code
- Addition of camera feeds to the web interface
- Addition of tests: robot control and sending position data to the server

#### To be planned for the next session

- Test the tests
- Add a test that checks for distance errors at a waypoint
- Test the robot in auto mode with other robots

### TH 33-34

#### Before the session

- Integration of a new task from the shared code to capture Aruco
- Creation of the product sheet
- Robot number
- Anti-spam on the console
- Measurement of the robot’s power consumption and other performance metrics
- Extensive testing with the other robots in the group

#### During the session

- Present: Teammate_2, Teammate_1, Tom Dugail, Teammate_3
- Optimized camera scanning function
- Calibration and beacon capture tests using the group’s shared code

#### To prepare for the next session

- Prepare technically and mentally for the evaluation