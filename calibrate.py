  [Restored contents truncated]
obstacle found: pos=(976,716), area=28, aspect=1.20
explorer: False
detected face: False
obstacle found: pos=(937,702), area=17, aspect=1.33
explorer: False
detected face: False
^Cpi@raspberrypi:~/JDESL/25-26-PWP-remote $ nano Motordriver.py 
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ nano pi_client.py 
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ ls
apiserver.py   calibrate.py  log_store.py  main.py               Motordriver.py     obstacle.py  pi_client.py            __pycache__  setting.txt  trial.py
automation.py  cvclass.py    log.txt       martian_detection.py  motor_steering.py  PCA9685.py   processing_parallel.py  README.md    templates    wanted.jpg
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ nano motor_steering.py 
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ nano motor_steering.py 
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ nano Motordriver.py 
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ pip install inspect
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    For more information visit http://rptl.io/venv

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ sudo apt install inspect
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Package inspect is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source

E: Package 'inspect' has no installation candidate
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ python3 main.py 
Pi motor client alive – polling the Mac every 100 ms…
start calibration?n
[ WARN:0@3.632] global ./modules/videoio/src/cap_gstreamer.cpp (1405) open OpenCV | GStreamer warning: Cannot query video position: status=0, value=-1, duration=-1
 * Serving Flask app 'apiserver'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.240.123:5000
Press CTRL+C to quit
192.168.240.18 - - [13/May/2026 09:04:11] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:04:12] "GET /gui HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:04:13] "GET /stream HTTP/1.1" 200 -
obstacle found: pos=(970,718), area=6, aspect=2.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:04:14] "GET /stream_processed HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:04:14] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(982,706), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(686,715), area=24, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(934,704), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(684,714), area=25, aspect=3.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:04:16] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(976,716), area=26, aspect=1.75
explorer: False
detected face: False
obstacle found: pos=(684,716), area=16, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(952,685), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(935,702), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(972,718), area=6, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(684,715), area=32, aspect=1.60
explorer: False
detected face: False
obstacle found: pos=(974,710), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:04:20] "POST /play HTTP/1.1" 200 -
obstacle found: pos=(972,719), area=4, aspect=1.33
explorer: False
last_c= 
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(980,719), area=4, aspect=1.33
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:04:21] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1198,718), area=6, aspect=2.00
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(984,694), area=18, aspect=1.33
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(786,698), area=6, aspect=1.00
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
192.168.240.18 - - [13/May/2026 09:04:23] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(638,704), area=24, aspect=1.63
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
obstacle found: pos=(225,700), area=6, aspect=1.00
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
obstacle found: pos=(1225,719), area=4, aspect=1.33
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
obstacle found: pos=(1252,686), area=6, aspect=1.00
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
192.168.240.18 - - [13/May/2026 09:04:25] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1246,366), area=9, aspect=1.33
explorer: False
last_c= r
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(399,716), area=22, aspect=1.50
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(535,719), area=4, aspect=1.33
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(749,702), area=18, aspect=1.50
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
192.168.240.18 - - [13/May/2026 09:04:27] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(569,719), area=4, aspect=1.33
explorer: False
last_c= l
turn left initialized-following horizontal
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:04:29] "GET /log HTTP/1.1" 200 -
loaded
0 12
diff 4
loaded
1 77
^Cpi@raspberrypi:~/JDESL/25-26-PWP-remote $ python3 main.py 
Pi motor client alive – polling the Mac every 100 ms…
start calibration?y
start calibration?y 
executing forward
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
turn right initialized
loaded
0 45
diff 4
loaded
1 45
loaded
0 77
diff 4
loaded
1 12
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
turn left initialized
loaded
0 45
diff 4
loaded
1 45
loaded
0 12
diff 4
loaded
1 77
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
settings are [4, [3.3, -36.0, 1.2], [3.5, 36.0, 1.3]], change differential,left, right?end
[ WARN:0@28.514] global ./modules/videoio/src/cap_gstreamer.cpp (1405) open OpenCV | GStreamer warning: Cannot query video position: status=0, value=-1, duration=-1
 * Serving Flask app 'apiserver'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.240.123:5000
Press CTRL+C to quit
192.168.240.18 - - [13/May/2026 09:05:12] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:05:12] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:05:16] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:05:16] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:05:20] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:05:20] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:05:22] "POST /play HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:05:22] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:05:27] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:05:27] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:05:30] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:05:30] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:05:34] "GET /gui HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:05:34] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:05:35] "GET /stream HTTP/1.1" 200 -
obstacle found: pos=(690,703), area=9, aspect=1.33
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:05:37] "GET /stream_processed HTTP/1.1" 200 -
obstacle found: pos=(690,678), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(710,690), area=9, aspect=1.33
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:05:38] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(728,663), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(788,636), area=12, aspect=1.67
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(724,717), area=10, aspect=1.33
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(760,632), area=30, aspect=2.25
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:05:40] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(762,682), area=54, aspect=2.60
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(766,637), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(810,719), area=4, aspect=1.33
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(794,701), area=13, aspect=1.40
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:05:42] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(840,698), area=9, aspect=1.33
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(573,719), area=4, aspect=1.33
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(881,702), area=9, aspect=1.33
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(269,630), area=15, aspect=2.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:05:44] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(920,707), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(887,692), area=20, aspect=1.75
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(938,715), area=22, aspect=2.67
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:05:46] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(964,642), area=6, aspect=1.00
explorer: False
last_c= 
turn left initialized-following horizontal
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:05:48] "GET /log HTTP/1.1" 200 -
loaded
0 12
diff 4
loaded
1 77
192.168.240.18 - - [13/May/2026 09:05:50] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:05:52] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:05:54] "GET /log HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
192.168.240.18 - - [13/May/2026 09:05:56] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(14,688), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(143,688), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(98,686), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:05:58] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(115,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(286,538), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(303,514), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(220,560), area=18, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:06:00] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(132,699), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(124,714), area=39, aspect=2.36
explorer: False
detected face: False
obstacle found: pos=(308,512), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:06:02] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(123,709), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(30,687), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(113,678), area=14, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(124,710), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:06:04] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(121,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(160,673), area=14, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(274,494), area=24, aspect=2.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:06:06] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(535,637), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(112,677), area=9, aspect=1.33
explorer: False
detected face: False
^Cpi@raspberrypi:~/JDESL/25-26-PWP-remote $ nano Motordriver.py 
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ python3 main.py 
Pi motor client alive – polling the Mac every 100 ms…
start calibration?n
[ WARN:0@6.527] global ./modules/videoio/src/cap_gstreamer.cpp (1405) open OpenCV | GStreamer warning: Cannot query video position: status=0, value=-1, duration=-1
 * Serving Flask app 'apiserver'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.240.123:5000
Press CTRL+C to quit
192.168.240.18 - - [13/May/2026 09:09:33] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:09:34] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:09:35] "GET /gui HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:09:36] "GET /stream HTTP/1.1" 200 -
obstacle found: pos=(1164,709), area=34, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:09:37] "GET /stream_processed HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:09:37] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(178,650), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(212,604), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(232,592), area=15, aspect=1.25
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:09:39] "POST /play HTTP/1.1" 200 -
obstacle found: pos=(121,711), area=13, aspect=1.00
explorer: False
last_c= 
turn left initialized-following horizontal
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:09:41] "GET /log HTTP/1.1" 200 -
loaded
0 12
diff 4
loaded
1 77
192.168.240.18 - - [13/May/2026 09:09:43] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:09:45] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:09:47] "GET /log HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
192.168.240.18 - - [13/May/2026 09:09:49] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(161,677), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(886,706), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(274,716), area=18, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(884,718), area=8, aspect=2.50
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:09:51] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(226,716), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(1100,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(220,718), area=8, aspect=2.50
explorer: False
detected face: False
obstacle found: pos=(193,705), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:09:53] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(220,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(257,698), area=24, aspect=2.47
explorer: False
detected face: False
obstacle found: pos=(222,717), area=10, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(880,716), area=22, aspect=1.50
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:09:55] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(222,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(216,718), area=6, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(218,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(275,716), area=18, aspect=1.25
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:09:57] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(268,704), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(883,710), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(888,698), area=14, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(270,704), area=13, aspect=1.40
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:09:59] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(265,701), area=20, aspect=2.43
explorer: False
detected face: False
obstacle found: pos=(885,712), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(888,703), area=17, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(239,708), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:10:01] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(269,703), area=21, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(156,692), area=50, aspect=2.17
explorer: False
detected face: False
obstacle found: pos=(190,708), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(878,716), area=23, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:10:03] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(258,700), area=18, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(885,705), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(271,703), area=12, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(891,700), area=32, aspect=1.71
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:10:05] "GET /log HTTP/1.1" 200 -
^Cpi@raspberrypi:~/JDESL/25-26-PWP-remote $ nano Motordriver.py 
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ python3 main.py 
Pi motor client alive – polling the Mac every 100 ms…
start calibration?n
[ WARN:0@11.454] global ./modules/videoio/src/cap_gstreamer.cpp (1405) open OpenCV | GStreamer warning: Cannot query video position: status=0, value=-1, duration=-1
 * Serving Flask app 'apiserver'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.240.123:5000
Press CTRL+C to quit
192.168.240.18 - - [13/May/2026 09:10:53] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:10:57] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:10:57] "GET /gui HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:10:58] "GET /stream HTTP/1.1" 200 -
obstacle found: pos=(24,667), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:11:00] "GET /stream_processed HTTP/1.1" 200 -
obstacle found: pos=(195,660), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(38,638), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:11:01] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(156,662), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(39,668), area=21, aspect=2.67
explorer: False
detected face: False
obstacle found: pos=(28,666), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(30,668), area=12, aspect=1.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:11:03] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(30,668), area=32, aspect=1.80
explorer: False
detected face: False
obstacle found: pos=(124,662), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(71,667), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:11:05] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(256,626), area=18, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(156,661), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(196,659), area=18, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(200,660), area=12, aspect=1.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:11:07] "POST /play HTTP/1.1" 200 -
obstacle found: pos=(72,666), area=9, aspect=1.33
explorer: False
last_c= 
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:11:08] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(332,676), area=22, aspect=1.75
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(48,124), area=40, aspect=1.17
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1058,367), area=9, aspect=1.33
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1144,571), area=11, aspect=1.00
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:11:10] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1114,561), area=6, aspect=1.00
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(153,484), area=104, aspect=1.30
explorer: False
last_c= r
turn left initialized-following horizontal
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:11:12] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:11:14] "GET /log HTTP/1.1" 200 -
loaded
0 12
diff 4
loaded
1 77
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:11:16] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:11:18] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:11:20] "GET /log HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
obstacle found: pos=(1152,644), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(1093,537), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:11:22] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1141,568), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1162,707), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1162,717), area=10, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(711,584), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:11:24] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1100,545), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(704,623), area=25, aspect=1.75
explorer: False
detected face: False
obstacle found: pos=(701,650), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1134,516), area=16, aspect=1.25
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:11:26] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1103,700), area=13, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1103,700), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1164,708), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:11:28] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1097,546), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(1154,648), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1136,549), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(718,614), area=13, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:11:30] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1212,512), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(721,538), area=21, aspect=2.67
explorer: False
detected face: False
obstacle found: pos=(1100,543), area=16, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(1128,486), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:11:32] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1100,546), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1097,543), area=40, aspect=1.61
explorer: False
detected face: False
obstacle found: pos=(690,716), area=18, aspect=2.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:11:34] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1156,700), area=9, aspect=1.33
explorer: False
detected face: False
^Cpi@raspberrypi:~/JDESL/25-26-PWP-remote $ python3 main.py 
Pi motor client alive – polling the Mac every 100 ms…
start calibration?y
start calibration?y
executing forward
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
turn right initialized
loaded
0 45
diff 4
loaded
1 45
loaded
0 77
diff 4
loaded
1 12
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
turn left initialized
loaded
0 45
diff 4
loaded
1 45
loaded
0 12
diff 4
loaded
1 77
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
settings are [4, [3.3, -36.0, 1.2], [3.5, 36.0, 1.3]], change differential,left, right?l
test right initial forward delay:3.5
test right turn speed-35
test right turn length1.3
executing forward
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
turn right initialized
loaded
0 45
diff 4
loaded
1 45
loaded
0 77
diff 4
loaded
1 12
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
turn left initialized
loaded
0 45
diff 4
loaded
1 45
loaded
0 13
diff 4
loaded
1 76
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
settings are [4, [3.5, -35.0, 1.3], [3.5, 36.0, 1.3]], change differential,left, right?again
executing forward
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
turn right initialized
loaded
0 45
diff 4
loaded
1 45
loaded
0 77
diff 4
loaded
1 12
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
turn left initialized
loaded
0 45
diff 4
loaded
1 45
loaded
0 13
diff 4
loaded
1 76
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
settings are [4, [3.5, -35.0, 1.3], [3.5, 36.0, 1.3]], change differential,left, right?end
[ WARN:0@96.298] global ./modules/videoio/src/cap_gstreamer.cpp (1405) open OpenCV | GStreamer warning: Cannot query video position: status=0, value=-1, duration=-1
 * Serving Flask app 'apiserver'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.240.123:5000
Press CTRL+C to quit
192.168.240.18 - - [13/May/2026 09:13:23] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:13:23] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:13:25] "GET /gui HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:13:25] "GET /stream HTTP/1.1" 200 -
obstacle found: pos=(1169,663), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:13:26] "GET /stream_processed HTTP/1.1" 200 -
obstacle found: pos=(198,692), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(131,634), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(197,718), area=6, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(216,706), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(135,632), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(18,719), area=4, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:13:29] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(4,634), area=20, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(133,632), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(950,711), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:13:31] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:13:31] "POST /play HTTP/1.1" 200 -
obstacle found: pos=(216,706), area=6, aspect=1.00
explorer: False
last_c= 
turn left initialized-following horizontal
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:13:33] "GET /log HTTP/1.1" 200 -
loaded
0 12
diff 4
loaded
1 77
192.168.240.18 - - [13/May/2026 09:13:35] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:13:37] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:13:39] "GET /log HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
192.168.240.18 - - [13/May/2026 09:13:41] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1236,69), area=40, aspect=1.17
explorer: False
detected face: False
obstacle found: pos=(582,557), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1048,376), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(568,658), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:13:43] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1142,378), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(573,623), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(700,360), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:13:45] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(584,552), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(624,357), area=34, aspect=2.75
explorer: False
detected face: False
obstacle found: pos=(566,685), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1072,376), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:13:47] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(570,660), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1074,374), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(1171,380), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(982,372), area=15, aspect=2.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:13:49] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1062,376), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(566,685), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(566,682), area=24, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(593,473), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:13:51] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(604,404), area=24, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(49,403), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(569,659), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1200,367), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:13:53] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(98,599), area=14, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(1017,374), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1180,380), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:13:55] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(24,460), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(48,403), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(27,650), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(970,372), area=18, aspect=2.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:13:57] "GET /flog HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:13:57] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(649,359), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(566,689), area=12, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:13:58] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1081,375), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1017,374), area=6, aspect=1.00
explorer: False
detected face: False
^Cpi@raspberrypi:~/JDESL/25-26-PWP-remote $ nano Motordriver.py 
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ python3 main.py 
Pi motor client alive – polling the Mac every 100 ms…
start calibration?n
[ WARN:0@4.420] global ./modules/videoio/src/cap_gstreamer.cpp (1405) open OpenCV | GStreamer warning: Cannot query video position: status=0, value=-1, duration=-1
 * Serving Flask app 'apiserver'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.240.123:5000
Press CTRL+C to quit
192.168.240.18 - - [13/May/2026 09:15:50] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:15:51] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:15:52] "GET /gui HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:15:53] "GET /stream HTTP/1.1" 200 -
obstacle found: pos=(580,695), area=20, aspect=1.20
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:15:53] "GET /stream_processed HTTP/1.1" 200 -
obstacle found: pos=(558,624), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(591,600), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(552,668), area=12, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(581,696), area=15, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(579,700), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:15:56] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(578,693), area=11, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(586,600), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(554,683), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(616,404), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:15:58] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(562,583), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(591,357), area=12, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(582,676), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:16:00] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(555,652), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(586,598), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(500,591), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(569,523), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:16:02] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:16:02] "POST /play HTTP/1.1" 200 -
obstacle found: pos=(561,718), area=10, aspect=3.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(562,569), area=9, aspect=1.33
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(266,76), area=40, aspect=1.17
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:16:04] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(23,688), area=6, aspect=1.00
explorer: False
last_c= 
turn left initialized-following horizontal
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:16:06] "GET /log HTTP/1.1" 200 -
loaded
0 13
diff 4
loaded
1 76
192.168.240.18 - - [13/May/2026 09:16:08] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:16:10] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:16:12] "GET /log HTTP/1.1" 200 -
stop called
192.168.240.18 - - [13/May/2026 09:16:14] "GET /log HTTP/1.1" 200 -
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
obstacle found: pos=(1183,714), area=30, aspect=2.50
explorer: False
detected face: False
obstacle found: pos=(1242,366), area=20, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(1158,708), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:16:16] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1158,714), area=31, aspect=2.50
explorer: False
detected face: False
obstacle found: pos=(957,328), area=21, aspect=2.67
explorer: False
detected face: False
obstacle found: pos=(564,686), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1160,716), area=12, aspect=1.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:16:18] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(557,543), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(744,608), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1159,706), area=14, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(33,719), area=4, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:16:20] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1158,715), area=30, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(1158,714), area=24, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(1199,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1186,692), area=24, aspect=3.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:16:22] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(499,291), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(669,620), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1198,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1160,708), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:16:24] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1160,704), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1181,352), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1160,710), area=62, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(556,543), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:16:26] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:16:26] "GET /flog HTTP/1.1" 200 -
obstacle found: pos=(561,686), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1158,714), area=28, aspect=2.50
explorer: False
detected face: False
^Cpi@raspberrypi:~/JDESL/25-26-PWP-remote $ nano automation.py 
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ python3 main.py 
Pi motor client alive – polling the Mac every 100 ms…
start calibration?m
[ WARN:0@2.589] global ./modules/videoio/src/cap_gstreamer.cpp (1405) open OpenCV | GStreamer warning: Cannot query video position: status=0, value=-1, duration=-1
 * Serving Flask app 'apiserver'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.240.123:5000
Press CTRL+C to quit
192.168.240.18 - - [13/May/2026 09:17:39] "GET /stream HTTP/1.1" 200 -
obstacle found: pos=(1158,716), area=18, aspect=2.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:17:40] "GET /stream_processed HTTP/1.1" 200 -
obstacle found: pos=(1226,690), area=14, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(642,704), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1159,719), area=4, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:17:42] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1241,666), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1180,694), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1218,696), area=6, aspect=1.00
explorer: False
detected face: False
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: backward
192.168.240.18 - - [13/May/2026 09:17:43] "POST /do/backward HTTP/1.1" 200 -
obstacle found: pos=(1121,702), area=13, aspect=1.40
explorer: False
detected face: False
obstacle found: pos=(1224,688), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1082,717), area=10, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1179,719), area=4, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:17:45] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1085,695), area=22, aspect=1.14
explorer: False
detected face: False
obstacle found: pos=(862,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1115,670), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(253,660), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:17:47] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1255,569), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1247,540), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(642,703), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(52,665), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:17:49] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(959,330), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(363,697), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(390,718), area=6, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(446,718), area=6, aspect=2.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:17:51] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(342,698), area=21, aspect=2.67
explorer: False
detected face: False
obstacle found: pos=(1205,703), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1150,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(332,718), area=8, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:17:53] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1228,718), area=18, aspect=2.67
explorer: False
detected face: False
obstacle found: pos=(1143,698), area=176, aspect=1.87
explorer: False
detected face: False
obstacle found: pos=(192,698), area=21, aspect=2.67
explorer: False
detected face: False
obstacle found: pos=(836,707), area=38, aspect=3.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:17:55] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(260,675), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(231,693), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(759,672), area=9, aspect=1.33
explorer: False
detected face: False
loaded
0 45
diff 4
192.168.240.18 - - [13/May/2026 09:17:57] "GET /log HTTP/1.1" 200 -
loaded
1 45
[Motordriver] Command sent: left
192.168.240.18 - - [13/May/2026 09:17:57] "POST /do/left HTTP/1.1" 200 -
obstacle found: pos=(234,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(16,662), area=18, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(1246,526), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(1030,696), area=12, aspect=1.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:17:59] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1276,522), area=18, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(62,703), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(112,588), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(365,580), area=6, aspect=1.00
explorer: False
detected face: False
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:18:01] "POST /do/forward HTTP/1.1" 200 -
obstacle found: pos=(1055,463), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1010,526), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:18:02] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1279,599), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1219,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(80,717), area=14, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(929,685), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:18:04] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(990,690), area=18, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(1042,677), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(1086,678), area=24, aspect=3.00
explorer: False
detected face: False
stop called
obstacle found: pos=(1126,705), area=15, aspect=2.00
explorer: False
detected face: False
stopped 0
stopped 1
[Motordriver] Command sent: stop
192.168.240.18 - - [13/May/2026 09:18:07] "POST /stop HTTP/1.1" 200 -
obstacle found: pos=(802,672), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:18:07] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1246,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1213,714), area=32, aspect=2.25
explorer: False
detected face: False
obstacle found: pos=(460,672), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1212,707), area=32, aspect=2.76
explorer: False
192.168.240.18 - - [13/May/2026 09:18:09] "POST /play HTTP/1.1" 200 -
last_c= 
turn left initialized-following horizontal
192.168.240.18 - - [13/May/2026 09:18:09] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:18:11] "GET /log HTTP/1.1" 200 -
loaded
0 13
diff 4
loaded
1 76
192.168.240.18 - - [13/May/2026 09:18:13] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:18:15] "GET /log HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
192.168.240.18 - - [13/May/2026 09:18:17] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(137,469), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1237,269), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(133,483), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:18:19] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(172,388), area=44, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(187,430), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(192,409), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1165,700), area=21, aspect=2.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:18:21] "POST /play HTTP/1.1" 200 -
obstacle found: pos=(151,467), area=6, aspect=1.00
explorer: False
last_c= 
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(50,60), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:18:22] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(144,531), area=9, aspect=1.33
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(79,668), area=11, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1264,564), area=13, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1123,460), area=21, aspect=2.67
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:18:24] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(992,535), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1204,664), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(981,684), area=9, aspect=1.33
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:18:26] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(572,719), area=4, aspect=1.33
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(718,696), area=17, aspect=1.33
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(825,677), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:18:28] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(984,489), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(960,686), area=12, aspect=1.67
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1084,718), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(584,718), area=6, aspect=2.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:18:30] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1032,694), area=18, aspect=1.50
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1170,686), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1246,640), area=21, aspect=2.21
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:18:32] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(26,718), area=8, aspect=2.50
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(211,37), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(125,582), area=9, aspect=1.33
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(116,703), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:18:34] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(643,674), area=59, aspect=1.12
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(806,492), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(257,76), area=9, aspect=1.33
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:18:36] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1043,492), area=34, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1099,549), area=34, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1216,464), area=34, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(904,596), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:18:38] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(898,717), area=10, aspect=1.33
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1009,623), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(16,136), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(1063,596), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
192.168.240.18 - - [13/May/2026 09:18:40] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1224,716), area=16, aspect=2.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(864,714), area=24, aspect=3.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(1158,700), area=64, aspect=1.83
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(1202,719), area=4, aspect=1.33
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
192.168.240.18 - - [13/May/2026 09:18:42] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(594,718), area=8, aspect=2.50
explorer: False
last_c= l
turn left initialized-following horizontal
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:18:44] "GET /log HTTP/1.1" 200 -
loaded
0 13
diff 4
loaded
1 76
192.168.240.18 - - [13/May/2026 09:18:46] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:18:48] "GET /log HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
192.168.240.18 - - [13/May/2026 09:18:50] "POST /stop HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
obstacle found: pos=(402,707), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:18:51] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(165,694), area=27, aspect=2.94
explorer: False
detected face: False
obstacle found: pos=(102,715), area=22, aspect=2.67
explorer: False
detected face: False
obstacle found: pos=(200,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(337,695), area=37, aspect=2.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:18:53] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(203,688), area=142, aspect=1.96
explorer: False
detected face: False
obstacle found: pos=(699,557), area=20, aspect=2.12
explorer: False
detected face: False
obstacle found: pos=(253,683), area=95, aspect=3.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:18:55] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(227,652), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1228,716), area=16, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(238,714), area=42, aspect=2.75
explorer: False
detected face: False
explorer: False
detected face: False
loaded
0 45
diff 4
192.168.240.18 - - [13/May/2026 09:18:57] "GET /log HTTP/1.1" 200 -
loaded
1 45
[Motordriver] Command sent: right
192.168.240.18 - - [13/May/2026 09:18:57] "POST /do/right HTTP/1.1" 200 -
obstacle found: pos=(83,551), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(46,569), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(53,552), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(605,703), area=88, aspect=1.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:18:59] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(528,699), area=68, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(156,692), area=40, aspect=1.17
explorer: False
detected face: False
obstacle found: pos=(1261,377), area=46, aspect=1.33
explorer: False
detected face: False
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
192.168.240.18 - - [13/May/2026 09:19:01] "POST /stop HTTP/1.1" 200 -
obstacle found: pos=(696,294), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(116,306), area=64, aspect=1.83
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:02] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(384,310), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(88,315), area=128, aspect=2.10
explorer: False
detected face: False
obstacle found: pos=(384,312), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(384,312), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:04] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:19:04] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(384,312), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(384,313), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(384,313), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(384,312), area=9, aspect=1.33
explorer: False
detected face: False
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:19:06] "POST /do/forward HTTP/1.1" 200 -
obstacle found: pos=(384,313), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:07] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(378,364), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(41,438), area=34, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(342,553), area=28, aspect=2.20
explorer: False
detected face: False
obstacle found: pos=(369,709), area=58, aspect=1.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:09] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(309,704), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(384,584), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(387,606), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(398,694), area=24, aspect=3.00
explorer: False
detected face: False
loaded
192.168.240.18 - - [13/May/2026 09:19:11] "GET /log HTTP/1.1" 200 -
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: right
192.168.240.18 - - [13/May/2026 09:19:11] "POST /do/right HTTP/1.1" 200 -
obstacle found: pos=(392,627), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1276,532), area=18, aspect=2.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:12] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(213,638), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(14,649), area=32, aspect=2.50
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:13] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1074,388), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(14,30), area=16, aspect=1.25
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:14] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1258,705), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1129,674), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:15] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(916,660), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(754,688), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:16] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(722,672), area=18, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(350,714), area=30, aspect=2.50
explorer: False
detected face: False
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:19:17] "POST /do/forward HTTP/1.1" 200 -
obstacle found: pos=(913,692), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(138,717), area=12, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(90,688), area=11, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:19] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(106,668), area=20, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1234,228), area=12, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1119,107), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:21] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(99,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(114,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(139,581), area=20, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(76,717), area=14, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:23] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(116,702), area=28, aspect=2.22
explorer: False
detected face: False
obstacle found: pos=(76,665), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(124,626), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(122,709), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:25] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(158,594), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1262,712), area=50, aspect=2.60
explorer: False
detected face: False
obstacle found: pos=(160,665), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:27] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(322,593), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1041,718), area=10, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(1279,139), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(265,630), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:29] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(230,699), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(232,714), area=24, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(508,510), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(278,691), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:31] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1033,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(278,548), area=34, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(100,652), area=109, aspect=2.43
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:33] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(740,705), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(560,64), area=9, aspect=1.33
explorer: False
detected face: False
explorer: False
detected face: False
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:35] "GET /log HTTP/1.1" 200 -
explorer: False
detected face: False
explorer: False
detected face: False
explorer: False
detected face: False
obstacle found: pos=(542,387), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:37] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(522,680), area=24, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(1056,656), area=24, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(493,697), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(646,673), area=9, aspect=1.33
explorer: False
detected face: False
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: left
192.168.240.18 - - [13/May/2026 09:19:39] "POST /do/left HTTP/1.1" 200 -
obstacle found: pos=(1250,167), area=34, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(744,584), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:40] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(958,652), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(84,4), area=32, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(193,716), area=22, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(378,718), area=8, aspect=2.50
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:42] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(520,672), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(646,456), area=18, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(898,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1091,719), area=4, aspect=1.33
explorer: False
detected face: False
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:19:44] "POST /do/forward HTTP/1.1" 200 -
obstacle found: pos=(1030,647), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1016,691), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:45] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(613,376), area=16, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(57,669), area=34, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(537,696), area=15, aspect=2.00
explorer: False
detected face: False
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: right
192.168.240.18 - - [13/May/2026 09:19:47] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:19:47] "POST /do/right HTTP/1.1" 200 -
obstacle found: pos=(238,632), area=34, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(393,669), area=34, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(287,702), area=57, aspect=1.12
explorer: False
detected face: False
obstacle found: pos=(74,699), area=34, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:49] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1233,610), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1096,710), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(142,695), area=134, aspect=2.87
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:51] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(660,649), area=16, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(542,694), area=14, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(888,718), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(359,704), area=6, aspect=1.00
explorer: False
detected face: False
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
192.168.240.18 - - [13/May/2026 09:19:53] "POST /stop HTTP/1.1" 200 -
obstacle found: pos=(456,702), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(656,190), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:54] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(362,634), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(932,172), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(338,699), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(336,716), area=16, aspect=2.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:56] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: right
192.168.240.18 - - [13/May/2026 09:19:56] "POST /do/right HTTP/1.1" 200 -
obstacle found: pos=(334,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(341,678), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(217,573), area=12, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(4,648), area=33, aspect=1.40
explorer: False
detected face: False
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
192.168.240.18 - - [13/May/2026 09:19:58] "POST /stop HTTP/1.1" 200 -
obstacle found: pos=(876,106), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(658,64), area=34, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:19:59] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1113,428), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1200,704), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1248,718), area=8, aspect=2.50
explorer: False
detected face: False
obstacle found: pos=(1202,704), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:20:01] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1250,202), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1260,706), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1246,716), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(872,3), area=18, aspect=2.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:20:03] "POST /play HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:20:03] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1275,706), area=22, aspect=2.67
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(870,385), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(1279,699), area=4, aspect=1.33
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(852,626), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
192.168.240.18 - - [13/May/2026 09:20:05] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1253,688), area=21, aspect=2.80
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(1233,719), area=4, aspect=1.33
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(1,18), area=6, aspect=1.50
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(158,52), area=9, aspect=1.33
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:20:07] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1262,99), area=34, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1204,684), area=15, aspect=2.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(520,311), area=13, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(680,415), area=17, aspect=2.14
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:20:09] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(15,239), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(824,642), area=12, aspect=1.67
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(554,656), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:20:11] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(292,651), area=16, aspect=1.50
explorer: False
last_c= l
detected face: False
obstacle found: pos=(98,370), area=9, aspect=1.33
explorer: True
loaded
0 54
diff 4
loaded
1 36
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:20:13] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
192.168.240.18 - - [13/May/2026 09:20:15] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:20:17] "GET /log HTTP/1.1" 200 -
loaded
0 18
diff 4
loaded
1 72
192.168.240.18 - - [13/May/2026 09:20:19] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:20:21] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:20:23] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
obstacle found: pos=(1094,714), area=25, aspect=3.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:25] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1075,714), area=36, aspect=2.50
explorer: True
detected face: False
obstacle found: pos=(1128,594), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(356,688), area=12, aspect=1.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:27] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1099,641), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1101,610), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(511,695), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1030,648), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:29] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1078,716), area=26, aspect=1.20
explorer: True
detected face: False
obstacle found: pos=(1081,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1079,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1083,710), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:31] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1076,718), area=10, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(1078,718), area=10, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1088,691), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1072,715), area=22, aspect=2.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:33] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1078,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1078,710), area=16, aspect=1.75
explorer: True
detected face: False
obstacle found: pos=(1043,677), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1078,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:35] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1074,716), area=22, aspect=1.40
explorer: True
detected face: False
obstacle found: pos=(1098,699), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1110,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:37] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1110,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1077,708), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1077,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1110,717), area=10, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:39] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1059,689), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1074,716), area=20, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1076,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1075,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:41] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1077,679), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1082,675), area=22, aspect=2.76
explorer: True
detected face: False
obstacle found: pos=(1110,716), area=18, aspect=2.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:43] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1110,716), area=18, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(1108,716), area=16, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1043,623), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1104,698), area=18, aspect=1.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:45] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1110,716), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(1075,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1080,717), area=10, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1108,718), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:47] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1108,716), area=18, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(1110,717), area=10, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1110,715), area=22, aspect=2.67
explorer: True
detected face: False
obstacle found: pos=(1082,718), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:49] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1058,691), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1072,715), area=32, aspect=1.60
explorer: True
detected face: False
obstacle found: pos=(1031,614), area=28, aspect=2.50
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:51] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1112,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1100,704), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1079,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1075,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:53] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1101,706), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1074,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1073,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1112,716), area=18, aspect=2.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:55] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1096,688), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1074,718), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1026,648), area=22, aspect=1.20
explorer: True
detected face: False
obstacle found: pos=(1109,716), area=16, aspect=1.25
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:57] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(126,689), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(116,696), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(1077,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1058,689), area=9, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:20:59] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1075,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1102,704), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1074,711), area=16, aspect=1.25
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:01] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1110,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(352,686), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1074,716), area=18, aspect=1.50
explorer: True
detected face: False
obstacle found: pos=(1111,716), area=18, aspect=1.50
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:03] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1111,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1071,712), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1070,715), area=22, aspect=2.67
explorer: True
detected face: False
obstacle found: pos=(122,693), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:05] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1074,718), area=8, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1098,691), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1109,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:07] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1070,707), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1071,715), area=26, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1043,678), area=22, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1046,678), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:09] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1075,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1074,718), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1026,653), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:11] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1076,718), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1072,715), area=26, aspect=1.60
explorer: True
detected face: False
obstacle found: pos=(1030,648), area=24, aspect=3.00
explorer: True
detected face: False
obstacle found: pos=(1110,714), area=42, aspect=2.20
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:13] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1064,702), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1111,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1072,716), area=27, aspect=1.40
explorer: True
detected face: False
obstacle found: pos=(1066,705), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:15] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1076,714), area=58, aspect=1.10
explorer: True
detected face: False
obstacle found: pos=(1043,676), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1109,716), area=21, aspect=1.75
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:17] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1109,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1061,683), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1110,717), area=10, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1051,632), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:19] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1086,686), area=12, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1048,679), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1061,694), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1078,675), area=9, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:21] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1028,649), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1044,678), area=22, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(50,679), area=13, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:23] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1079,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1064,705), area=25, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1072,702), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1089,684), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:25] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1110,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1075,716), area=15, aspect=1.25
explorer: True
detected face: False
obstacle found: pos=(1110,715), area=22, aspect=2.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:27] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1080,716), area=16, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1112,718), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1072,716), area=22, aspect=1.40
explorer: True
detected face: False
obstacle found: pos=(1112,716), area=12, aspect=1.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:29] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1108,718), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(994,615), area=16, aspect=1.60
explorer: True
detected face: False
obstacle found: pos=(1078,716), area=20, aspect=1.50
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:31] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1077,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1081,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1058,684), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1112,714), area=30, aspect=1.80
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:33] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1100,700), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1082,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1084,692), area=13, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:35] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1108,718), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1109,716), area=18, aspect=1.50
explorer: True
detected face: False
obstacle found: pos=(1012,633), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1042,630), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:37] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1039,664), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1080,718), area=8, aspect=2.50
explorer: True
detected face: False
obstacle found: pos=(1140,670), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:39] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1064,650), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1108,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1058,695), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1108,716), area=12, aspect=1.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:41] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1074,716), area=20, aspect=1.20
explorer: True
detected face: False
obstacle found: pos=(1093,686), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1077,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:43] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1110,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1091,718), area=10, aspect=3.00
explorer: True
detected face: False
obstacle found: pos=(1094,698), area=12, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1108,718), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:45] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1109,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1109,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1034,650), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1074,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:47] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1085,697), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1010,637), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1072,703), area=11, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:49] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1075,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1072,715), area=22, aspect=2.67
explorer: True
detected face: False
obstacle found: pos=(1066,692), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1072,715), area=26, aspect=1.60
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:51] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1072,716), area=16, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1108,706), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1077,710), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:53] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(992,598), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1072,718), area=8, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1138,683), area=78, aspect=1.71
explorer: True
detected face: False
obstacle found: pos=(1017,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:55] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(94,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(168,717), area=10, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(406,662), area=9, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:57] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(110,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1048,631), area=24, aspect=1.75
explorer: True
detected face: False
obstacle found: pos=(228,705), area=13, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(156,716), area=18, aspect=1.25
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:21:59] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(209,679), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(110,718), area=10, aspect=3.00
explorer: True
detected face: False
obstacle found: pos=(285,701), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:22:01] "POST /play HTTP/1.1" 200 -
obstacle found: pos=(314,667), area=6, aspect=1.00
explorer: True
loaded
0 36
diff 4
loaded
1 54
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:22:02] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
192.168.240.18 - - [13/May/2026 09:22:04] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:22:06] "GET /log HTTP/1.1" 200 -
loaded
0 18
diff 4
loaded
1 72
192.168.240.18 - - [13/May/2026 09:22:08] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:22:10] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:22:12] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
192.168.240.18 - - [13/May/2026 09:22:14] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(932,716), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(851,714), area=35, aspect=2.15
explorer: True
detected face: False
obstacle found: pos=(1000,699), area=94, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(140,686), area=12, aspect=1.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:22:16] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(835,663), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(840,678), area=16, aspect=1.25
explorer: True
detected face: False
obstacle found: pos=(886,716), area=16, aspect=2.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:22:18] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(850,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(852,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(876,693), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(842,696), area=8, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:22:20] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(853,718), area=10, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(850,717), area=10, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(826,654), area=18, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(856,645), area=16, aspect=1.50
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:22:22] "POST /play HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:22:22] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(882,702), area=12, aspect=1.67
explorer: True
loaded
0 36
diff 4
loaded
1 54
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:22:24] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:22:26] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:22:28] "GET /log HTTP/1.1" 200 -
loaded
0 18
diff 4
loaded
1 72
192.168.240.18 - - [13/May/2026 09:22:30] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:22:32] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
192.168.240.18 - - [13/May/2026 09:22:34] "GET /log HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
obstacle found: pos=(163,588), area=11, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:22:36] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(114,716), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(338,288), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(141,696), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(75,605), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:22:38] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(336,292), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(112,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(115,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:22:40] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(106,699), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(106,698), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(61,550), area=9, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:22:42] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(13,390), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(96,674), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(93,657), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(112,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:22:44] "POST /play HTTP/1.1" 200 -
obstacle found: pos=(112,705), area=9, aspect=1.33
explorer: True
loaded
0 36
diff 4
loaded
1 54
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:22:45] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
192.168.240.18 - - [13/May/2026 09:22:47] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:22:49] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:22:51] "GET /log HTTP/1.1" 200 -
loaded
0 18
diff 4
loaded
1 72
192.168.240.18 - - [13/May/2026 09:22:53] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:22:55] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
192.168.240.18 - - [13/May/2026 09:22:57] "GET /log HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
obstacle found: pos=(922,523), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1262,716), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(1052,704), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:22:59] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1086,687), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1045,699), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1276,702), area=16, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1048,698), area=20, aspect=1.50
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:01] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1051,701), area=17, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1074,672), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(1050,701), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1067,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:03] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1054,705), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1027,681), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1081,681), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1045,700), area=15, aspect=2.18
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:05] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1018,674), area=11, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1073,672), area=11, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1048,700), area=13, aspect=1.40
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:07] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1046,699), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1070,718), area=8, aspect=2.50
explorer: True
detected face: False
obstacle found: pos=(1253,715), area=28, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1051,703), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:09] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1054,705), area=13, aspect=1.40
explorer: True
detected face: False
obstacle found: pos=(1044,697), area=24, aspect=1.80
explorer: True
detected face: False
obstacle found: pos=(1068,718), area=16, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(1069,718), area=6, aspect=2.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:11] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1008,666), area=19, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(1048,698), area=18, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(1055,708), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1081,683), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:13] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1030,685), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1040,693), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1252,716), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(1046,698), area=11, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:15] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1068,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1039,693), area=12, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1045,698), area=13, aspect=1.40
explorer: True
detected face: False
obstacle found: pos=(1045,696), area=24, aspect=1.43
explorer: True
192.168.240.18 - - [13/May/2026 09:23:17] "GET /log HTTP/1.1" 200 -
detected face: False
obstacle found: pos=(1069,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1068,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1071,672), area=9, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:19] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1047,698), area=17, aspect=1.80
explorer: True
detected face: False
obstacle found: pos=(874,701), area=37, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(617,698), area=66, aspect=1.43
explorer: True
detected face: False
obstacle found: pos=(1022,718), area=8, aspect=2.50
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:21] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1157,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1134,696), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1137,699), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:23] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1214,612), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1130,706), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1266,474), area=40, aspect=1.17
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:25] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1209,616), area=110, aspect=1.90
explorer: True
detected face: False
obstacle found: pos=(1135,692), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1129,703), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1224,642), area=15, aspect=2.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:27] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1202,626), area=128, aspect=2.50
explorer: True
detected face: False
obstacle found: pos=(1269,396), area=40, aspect=1.17
explorer: True
detected face: False
obstacle found: pos=(1205,625), area=132, aspect=2.48
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:29] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1225,710), area=10, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1076,685), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(754,675), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:31] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(806,675), area=62, aspect=2.06
explorer: True
detected face: False
obstacle found: pos=(648,632), area=34, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(644,676), area=34, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(340,712), area=62, aspect=2.65
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:33] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(344,716), area=24, aspect=1.75
explorer: True
detected face: False
obstacle found: pos=(96,716), area=18, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(343,712), area=46, aspect=2.17
explorer: True
detected face: False
obstacle found: pos=(343,712), area=33, aspect=2.17
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:35] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(344,713), area=55, aspect=2.40
explorer: True
detected face: False
obstacle found: pos=(1248,716), area=16, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(344,714), area=42, aspect=1.80
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:37] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(342,713), area=35, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1252,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(342,715), area=38, aspect=1.60
explorer: True
detected face: False
obstacle found: pos=(344,715), area=38, aspect=1.60
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:39] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(344,715), area=30, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(344,714), area=42, aspect=1.80
explorer: True
detected face: False
obstacle found: pos=(344,714), area=38, aspect=2.50
explorer: True
detected face: False
obstacle found: pos=(342,712), area=60, aspect=2.60
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:41] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1246,694), area=18, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(344,714), area=48, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(344,712), area=54, aspect=2.60
explorer: True
detected face: False
obstacle found: pos=(1266,716), area=12, aspect=1.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:43] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(456,704), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(605,307), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1238,283), area=9, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:45] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1227,286), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(87,522), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(999,278), area=15, aspect=2.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:47] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(569,698), area=34, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(886,274), area=24, aspect=3.00
explorer: True
detected face: False
obstacle found: pos=(747,295), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1264,513), area=34, aspect=2.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:49] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(173,491), area=36, aspect=3.00
explorer: True
detected face: False
obstacle found: pos=(135,479), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(168,483), area=9, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:51] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1261,337), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(349,564), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(608,368), area=18, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(1254,445), area=44, aspect=1.45
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:53] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(460,716), area=20, aspect=1.50
explorer: True
detected face: False
obstacle found: pos=(84,675), area=88, aspect=2.50
explorer: True
detected face: False
obstacle found: pos=(1266,579), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1270,568), area=12, aspect=1.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:55] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(909,545), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1234,695), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(158,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(253,673), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:57] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(164,684), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(752,630), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(849,565), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:23:59] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1109,620), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1129,611), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1194,568), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1236,599), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:24:01] "GET /log HTTP/1.1" 200 -
explorer: True
detected face: False
obstacle found: pos=(1152,617), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1159,645), area=11, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1144,589), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:24:03] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1156,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1164,653), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1122,540), area=9, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:24:05] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1168,671), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1171,679), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1168,671), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1166,670), area=9, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:24:07] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1142,595), area=11, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1164,662), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1180,703), area=21, aspect=2.67
explorer: True
detected face: False
obstacle found: pos=(1145,600), area=18, aspect=1.50
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:24:09] "POST /play HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:24:09] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(682,655), area=6, aspect=1.00
explorer: True
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:24:11] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:24:13] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:24:15] "GET /log HTTP/1.1" 200 -
loaded
0 18
diff 4
loaded
1 72
192.168.240.18 - - [13/May/2026 09:24:17] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:24:19] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
192.168.240.18 - - [13/May/2026 09:24:21] "GET /log HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
obstacle found: pos=(1024,678), area=56, aspect=1.29
explorer: True
detected face: False
obstacle found: pos=(1015,681), area=34, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:24:23] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(722,716), area=18, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(957,706), area=89, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(720,715), area=38, aspect=1.60
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:24:25] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1016,683), area=34, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(994,690), area=64, aspect=1.83
explorer: True
detected face: False
obstacle found: pos=(718,714), area=34, aspect=1.80
explorer: True
detected face: False
obstacle found: pos=(718,715), area=30, aspect=2.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:24:27] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(718,715), area=30, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(952,708), area=54, aspect=1.29
explorer: True
detected face: False
obstacle found: pos=(718,715), area=38, aspect=1.60
explorer: True
detected face: False
obstacle found: pos=(830,620), area=12, aspect=1.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:24:29] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(955,706), area=59, aspect=1.43
explorer: True
detected face: False
obstacle found: pos=(965,703), area=34, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(992,690), area=34, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(992,690), area=34, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:24:31] "POST /play HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:24:31] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(994,690), area=80, aspect=1.86
explorer: True
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:24:33] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:24:35] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:24:37] "GET /log HTTP/1.1" 200 -
loaded
0 18
diff 4
loaded
1 72
stop called
192.168.240.18 - - [13/May/2026 09:24:39] "GET /log HTTP/1.1" 200 -
stopped 0
stopped 1
[Motordriver] Command sent: stop
192.168.240.18 - - [13/May/2026 09:24:39] "POST /stop HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:24:41] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
192.168.240.18 - - [13/May/2026 09:24:43] "POST /stop HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
192.168.240.18 - - [13/May/2026 09:24:44] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(221,699), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(197,712), area=58, aspect=2.57
explorer: True
detected face: False
obstacle found: pos=(196,714), area=42, aspect=2.20
explorer: True
detected face: False
obstacle found: pos=(177,690), area=64, aspect=1.83
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:24:46] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(146,718), area=12, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(194,714), area=25, aspect=1.50
explorer: True
detected face: False
obstacle found: pos=(222,700), area=38, aspect=1.80
explorer: True
detected face: False
obstacle found: pos=(220,692), area=9, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:24:48] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(709,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(193,711), area=66, aspect=2.73
explorer: True
detected face: False
obstacle found: pos=(218,695), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(195,713), area=42, aspect=2.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:24:50] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(228,716), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(196,710), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(703,716), area=18, aspect=1.25
explorer: True
detected face: False
obstacle found: pos=(142,697), area=18, aspect=1.25
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:24:52] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(197,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(196,714), area=43, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(221,695), area=30, aspect=1.85
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:24:54] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(198,717), area=14, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(196,716), area=25, aspect=1.20
explorer: True
detected face: False
obstacle found: pos=(196,716), area=16, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(196,716), area=22, aspect=1.20
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:24:56] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(223,715), area=28, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(202,708), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(191,715), area=24, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(146,718), area=18, aspect=3.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:24:58] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(150,716), area=30, aspect=1.40
explorer: True
detected face: False
obstacle found: pos=(194,714), area=24, aspect=3.00
explorer: True
detected face: False
obstacle found: pos=(190,702), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(140,709), area=11, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:00] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(146,718), area=10, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(144,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(179,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(152,700), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:02] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1122,238), area=32, aspect=1.60
explorer: True
detected face: False
obstacle found: pos=(968,657), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(399,690), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(325,685), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:04] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(358,703), area=74, aspect=2.92
explorer: True
detected face: False
obstacle found: pos=(368,717), area=24, aspect=2.25
explorer: True
detected face: False
obstacle found: pos=(363,717), area=16, aspect=1.50
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:06] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(786,704), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(364,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(342,696), area=19, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(370,716), area=12, aspect=1.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:08] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(366,718), area=8, aspect=2.50
explorer: True
detected face: False
obstacle found: pos=(366,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(739,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(352,705), area=20, aspect=1.75
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:10] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(372,718), area=16, aspect=2.67
explorer: True
detected face: False
obstacle found: pos=(358,708), area=151, aspect=2.13
explorer: True
detected face: False
obstacle found: pos=(103,700), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:12] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(46,716), area=16, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(40,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(161,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(367,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:14] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(361,708), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(369,717), area=14, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(372,718), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(748,696), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:16] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(372,717), area=18, aspect=1.75
explorer: True
detected face: False
obstacle found: pos=(373,674), area=22, aspect=1.20
explorer: True
detected face: False
obstacle found: pos=(784,718), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:18] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(367,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(361,706), area=15, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(367,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(366,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:20] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(343,698), area=17, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(368,716), area=36, aspect=2.60
explorer: True
detected face: False
obstacle found: pos=(740,705), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(737,717), area=10, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:22] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(365,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(364,718), area=8, aspect=2.50
explorer: True
detected face: False
obstacle found: pos=(814,671), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(784,706), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:24] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(351,702), area=18, aspect=1.50
explorer: True
detected face: False
obstacle found: pos=(340,694), area=28, aspect=2.47
explorer: True
detected face: False
obstacle found: pos=(783,714), area=33, aspect=2.75
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:26] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(364,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(743,704), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(372,718), area=18, aspect=2.67
explorer: True
detected face: False
obstacle found: pos=(368,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:28] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(347,699), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(358,704), area=14, aspect=1.25
explorer: True
detected face: False
obstacle found: pos=(368,702), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(782,707), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:30] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(360,707), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(780,707), area=17, aspect=1.25
explorer: True
detected face: False
obstacle found: pos=(366,716), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(369,717), area=16, aspect=1.50
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:32] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(367,718), area=8, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(364,718), area=8, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(779,667), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:34] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(736,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(369,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(345,700), area=29, aspect=2.67
explorer: True
detected face: False
obstacle found: pos=(366,717), area=10, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:36] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(788,707), area=11, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(740,704), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(784,709), area=9, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:38] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(394,693), area=11, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(408,702), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(783,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(366,718), area=6, aspect=2.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:40] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(785,708), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(736,715), area=22, aspect=2.67
explorer: True
detected face: False
obstacle found: pos=(366,716), area=22, aspect=1.40
explorer: True
detected face: False
obstacle found: pos=(365,718), area=10, aspect=3.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:42] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(784,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(349,701), area=38, aspect=2.69
explorer: True
detected face: False
obstacle found: pos=(778,718), area=8, aspect=2.50
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:44] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(363,716), area=16, aspect=1.25
explorer: True
detected face: False
obstacle found: pos=(789,705), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(785,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(354,706), area=12, aspect=1.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:25:46] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(741,704), area=11, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(339,687), area=6, aspect=1.00
explorer: True
detected face: False
^Cpi@raspberrypi:~/JDESL/25-26-PWP-remote $ nano automation.py 
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ python3 main.py 
Pi motor client alive – polling the Mac every 100 ms…
start calibration?n
[ WARN:0@6.870] global ./modules/videoio/src/cap_gstreamer.cpp (1405) open OpenCV | GStreamer warning: Cannot query video position: status=0, value=-1, duration=-1
 * Serving Flask app 'apiserver'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.240.123:5000
Press CTRL+C to quit
192.168.240.18 - - [13/May/2026 09:26:25] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:26:26] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:26:28] "GET /gui HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:26:28] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:26:29] "GET /stream HTTP/1.1" 200 -
obstacle found: pos=(1001,701), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:26:31] "GET /stream_processed HTTP/1.1" 200 -
obstacle found: pos=(1007,674), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1003,701), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:26:32] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1020,652), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(990,606), area=52, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(988,606), area=18, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(0,610), area=2, aspect=3.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:26:34] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(989,600), area=20, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(1001,716), area=20, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(1010,680), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:26:36] "POST /play HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:26:36] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1024,622), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(990,640), area=12, aspect=1.67
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1071,701), area=36, aspect=2.56
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1117,699), area=6, aspect=1.00
explorer: False
last_c= 
turn left initialized-following horizontal
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:26:38] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:26:40] "GET /log HTTP/1.1" 200 -
loaded
0 13
diff 4
loaded
1 76
192.168.240.18 - - [13/May/2026 09:26:42] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
192.168.240.18 - - [13/May/2026 09:26:44] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1126,696), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1192,672), area=32, aspect=2.75
explorer: False
detected face: False
obstacle found: pos=(1204,626), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1186,715), area=22, aspect=2.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:26:46] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1178,718), area=8, aspect=2.50
explorer: False
detected face: False
obstacle found: pos=(1148,716), area=26, aspect=1.40
explorer: False
detected face: False
obstacle found: pos=(1190,692), area=88, aspect=2.57
explorer: False
detected face: False
obstacle found: pos=(1188,702), area=18, aspect=2.20
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:26:48] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1183,710), area=91, aspect=2.25
explorer: False
detected face: False
obstacle found: pos=(1186,696), area=94, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(1204,634), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(1182,716), area=26, aspect=1.20
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:26:50] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1184,715), area=38, aspect=1.60
explorer: False
detected face: False
obstacle found: pos=(1196,654), area=18, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(1189,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1160,678), area=15, aspect=1.25
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:26:52] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(986,651), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(91,704), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1226,606), area=22, aspect=1.40
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:26:54] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1190,558), area=17, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1252,718), area=6, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(1244,685), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1244,686), area=12, aspect=1.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:26:56] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(974,654), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(160,691), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1245,688), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(574,711), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:26:58] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1246,683), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1252,716), area=16, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(1219,715), area=25, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(528,708), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:00] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1222,717), area=10, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(211,630), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1218,714), area=24, aspect=3.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:02] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(215,701), area=83, aspect=1.87
explorer: False
detected face: False
obstacle found: pos=(754,704), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1026,695), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(834,707), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:04] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(864,697), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1015,670), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(831,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(828,664), area=18, aspect=2.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:06] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1090,638), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(1012,669), area=12, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(864,696), area=20, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:08] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1057,634), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1015,670), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1007,661), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(860,687), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:10] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:27:10] "POST /play HTTP/1.1" 200 -
obstacle found: pos=(1013,667), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1017,668), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(887,703), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(882,577), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:27:12] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(868,694), area=18, aspect=2.33
explorer: False
last_c= 
turn left initialized-following horizontal
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:27:14] "GET /log HTTP/1.1" 200 -
loaded
0 13
diff 4
loaded
1 76
192.168.240.18 - - [13/May/2026 09:27:16] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:27:18] "GET /log HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
obstacle found: pos=(13,688), area=79, aspect=1.73
explorer: False
detected face: False
obstacle found: pos=(18,696), area=201, aspect=1.12
explorer: False
detected face: False
obstacle found: pos=(666,679), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:20] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(692,702), area=31, aspect=1.60
explorer: False
detected face: False
obstacle found: pos=(659,697), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(662,688), area=24, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(688,717), area=10, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:22] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(684,717), area=10, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(705,652), area=12, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(661,689), area=11, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(662,686), area=12, aspect=1.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:24] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(20,698), area=180, aspect=1.07
explorer: False
detected face: False
obstacle found: pos=(668,677), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(660,697), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(704,656), area=15, aspect=2.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:26] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(111,630), area=151, aspect=2.95
explorer: False
detected face: False
obstacle found: pos=(686,718), area=8, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(691,706), area=26, aspect=2.50
explorer: False
detected face: False
obstacle found: pos=(687,718), area=6, aspect=2.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:28] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1034,118), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1149,526), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(901,704), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:30] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1129,679), area=11, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(944,715), area=22, aspect=2.67
explorer: False
detected face: False
obstacle found: pos=(941,604), area=20, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(118,716), area=20, aspect=1.50
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:32] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(939,657), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(954,470), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(960,523), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(973,667), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:34] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(962,557), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(939,652), area=34, aspect=2.75
explorer: False
detected face: False
obstacle found: pos=(942,717), area=10, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:36] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(942,682), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(944,710), area=18, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(943,677), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(968,574), area=18, aspect=2.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:38] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(984,704), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(894,712), area=54, aspect=2.74
explorer: False
detected face: False
obstacle found: pos=(892,719), area=4, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:40] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(891,695), area=58, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(928,702), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(904,707), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(908,714), area=40, aspect=2.20
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:42] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(871,713), area=40, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(914,694), area=25, aspect=1.40
explorer: False
detected face: False
obstacle found: pos=(824,658), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:44] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(865,690), area=40, aspect=2.75
explorer: False
detected face: False
obstacle found: pos=(837,690), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(858,712), area=60, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(870,686), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:46] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(908,716), area=26, aspect=1.75
explorer: False
detected face: False
obstacle found: pos=(874,690), area=11, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(874,714), area=24, aspect=3.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:48] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(829,626), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(877,702), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(834,654), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(842,710), area=11, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:50] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(839,683), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(839,685), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(860,630), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:52] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(832,646), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(864,656), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(860,616), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(830,632), area=12, aspect=1.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:54] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(18,454), area=40, aspect=1.17
explorer: False
detected face: False
obstacle found: pos=(872,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(876,688), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:56] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(838,699), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(872,718), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(838,699), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:27:58] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(873,685), area=22, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(876,716), area=20, aspect=1.40
explorer: False
detected face: False
obstacle found: pos=(954,642), area=43, aspect=2.60
explorer: False
detected face: False
obstacle found: pos=(914,653), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:28:00] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(915,700), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(905,624), area=16, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(916,694), area=31, aspect=1.60
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:28:02] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(992,646), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(914,716), area=18, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(917,680), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(916,688), area=42, aspect=2.60
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:28:04] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(913,705), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(973,651), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1141,690), area=58, aspect=1.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:28:06] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(942,641), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(915,692), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(906,629), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(914,692), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:28:08] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(916,702), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(914,718), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(912,670), area=14, aspect=1.25
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:28:10] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(936,640), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1260,393), area=40, aspect=1.17
explorer: False
detected face: False
obstacle found: pos=(943,638), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(917,719), area=4, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:28:12] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(945,660), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(930,701), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(912,671), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:28:14] "POST /play HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:28:14] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(944,659), area=9, aspect=1.33
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(910,662), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(926,711), area=6, aspect=1.00
explorer: False
last_c= 
turn left initialized-following horizontal
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:28:16] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:28:18] "GET /log HTTP/1.1" 200 -
loaded
0 13
diff 4
loaded
1 76
192.168.240.18 - - [13/May/2026 09:28:20] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
obstacle found: pos=(254,378), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:28:22] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(35,591), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(29,551), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(34,585), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(0,578), area=2, aspect=3.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:28:24] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1,578), area=8, aspect=2.50
explorer: False
detected face: False
obstacle found: pos=(36,585), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(35,585), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(48,577), area=36, aspect=2.50
explorer: False
detected face: False
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: backward
192.168.240.18 - - [13/May/2026 09:28:26] "POST /do/backward HTTP/1.1" 200 -
obstacle found: pos=(31,591), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(177,440), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:28:27] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(130,714), area=43, aspect=1.80
explorer: False
detected face: False
obstacle found: pos=(90,701), area=34, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(283,705), area=34, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:28:29] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(4,688), area=20, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(222,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(348,700), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(598,718), area=10, aspect=3.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:28:31] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(557,634), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(998,704), area=18, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(1196,703), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1093,718), area=10, aspect=3.00
explorer: False
detected face: False
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
192.168.240.18 - - [13/May/2026 09:28:33] "POST /stop HTTP/1.1" 200 -
obstacle found: pos=(1054,713), area=48, aspect=2.40
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:28:34] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1043,695), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(995,715), area=28, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(994,716), area=20, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(998,705), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:28:36] "POST /play HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:28:36] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(996,716), area=16, aspect=1.25
explorer: False
last_c= 
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(995,714), area=32, aspect=2.25
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1246,702), area=21, aspect=2.67
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:28:38] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1203,714), area=42, aspect=2.42
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(371,689), area=28, aspect=1.70
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(108,703), area=6, aspect=1.00
explorer: False
last_c= l
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(105,698), area=49, aspect=1.14
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
192.168.240.18 - - [13/May/2026 09:28:40] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(2,536), area=14, aspect=1.67
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
obstacle found: pos=(112,630), area=9, aspect=1.33
explorer: False
last_c= r
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(366,716), area=18, aspect=2.33
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
192.168.240.18 - - [13/May/2026 09:28:42] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(642,718), area=8, aspect=2.50
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(706,718), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(738,676), area=15, aspect=2.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(974,718), area=8, aspect=2.50
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
192.168.240.18 - - [13/May/2026 09:28:44] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1208,718), area=10, aspect=3.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(0,718), area=2, aspect=2.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(987,719), area=4, aspect=1.33
explorer: False
last_c= l
detected face: False
obstacle found: pos=(331,696), area=6, aspect=1.00
explorer: True
loaded
0 54
diff 4
loaded
1 36
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:28:46] "GET /log HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
192.168.240.18 - - [13/May/2026 09:28:48] "POST /stop HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
192.168.240.18 - - [13/May/2026 09:28:49] "POST /stop HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
stop called
192.168.240.18 - - [13/May/2026 09:28:50] "GET /log HTTP/1.1" 200 -
stopped 0
stopped 1
[Motordriver] Command sent: stop
192.168.240.18 - - [13/May/2026 09:28:50] "POST /stop HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:28:51] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:28:52] "GET /log HTTP/1.1" 200 -
loaded
0 18
diff 4
loaded
1 72
192.168.240.18 - - [13/May/2026 09:28:53] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:28:54] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:28:55] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:28:56] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
192.168.240.18 - - [13/May/2026 09:28:59] "POST /stop HTTP/1.1" 200 -
obstacle found: pos=(404,501), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(235,685), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:00] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(205,664), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(448,677), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(189,689), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(736,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:02] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(528,704), area=14, aspect=1.25
explorer: True
detected face: False
obstacle found: pos=(1088,671), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1089,671), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(452,677), area=9, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:04] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(459,711), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(203,665), area=20, aspect=3.00
explorer: True
detected face: False
obstacle found: pos=(448,671), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(452,686), area=11, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:06] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(504,678), area=28, aspect=1.40
explorer: True
detected face: False
obstacle found: pos=(737,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(206,663), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(493,531), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:08] "GET /log HTTP/1.1" 200 -
explorer: True
detected face: False
obstacle found: pos=(1258,692), area=55, aspect=1.29
explorer: True
detected face: False
obstacle found: pos=(993,684), area=16, aspect=1.25
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:10] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(996,716), area=25, aspect=1.20
explorer: True
detected face: False
obstacle found: pos=(998,717), area=10, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(996,712), area=60, aspect=3.00
explorer: True
detected face: False
obstacle found: pos=(1029,702), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:12] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1021,672), area=26, aspect=2.25
explorer: True
detected face: False
obstacle found: pos=(996,714), area=32, aspect=2.75
explorer: True
detected face: False
obstacle found: pos=(1022,680), area=13, aspect=1.40
explorer: True
detected face: False
obstacle found: pos=(1023,673), area=40, aspect=2.45
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:14] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(992,691), area=12, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(996,714), area=27, aspect=2.25
explorer: True
detected face: False
obstacle found: pos=(1020,666), area=9, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:16] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1022,672), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(998,716), area=18, aspect=1.25
explorer: True
detected face: False
obstacle found: pos=(996,707), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1012,700), area=18, aspect=2.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:18] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(997,713), area=37, aspect=3.00
explorer: True
detected face: False
obstacle found: pos=(1035,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(998,716), area=30, aspect=1.40
explorer: True
detected face: False
obstacle found: pos=(998,716), area=23, aspect=1.75
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:20] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1020,670), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(996,716), area=16, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1028,685), area=15, aspect=1.82
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:22] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1034,716), area=18, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(996,713), area=37, aspect=2.91
explorer: True
detected face: False
obstacle found: pos=(996,716), area=24, aspect=1.20
explorer: True
detected face: False
obstacle found: pos=(1011,698), area=21, aspect=2.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:24] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(996,709), area=15, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1032,714), area=24, aspect=3.00
explorer: True
detected face: False
obstacle found: pos=(998,712), area=38, aspect=2.79
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:26] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1030,702), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1028,696), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(1022,674), area=16, aspect=1.25
explorer: True
detected face: False
obstacle found: pos=(997,713), area=44, aspect=2.80
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:28] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(996,712), area=53, aspect=2.60
explorer: True
detected face: False
obstacle found: pos=(1030,699), area=30, aspect=1.60
explorer: True
detected face: False
obstacle found: pos=(997,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:30] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(995,704), area=22, aspect=1.75
explorer: True
detected face: False
obstacle found: pos=(1030,698), area=22, aspect=1.75
explorer: True
detected face: False
obstacle found: pos=(998,716), area=16, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1034,715), area=22, aspect=2.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:32] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1034,716), area=16, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1034,714), area=24, aspect=3.00
explorer: True
detected face: False
obstacle found: pos=(1026,680), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:34] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1000,718), area=8, aspect=2.50
explorer: True
detected face: False
obstacle found: pos=(1034,715), area=22, aspect=2.67
explorer: True
detected face: False
obstacle found: pos=(996,712), area=47, aspect=2.80
explorer: True
detected face: False
obstacle found: pos=(998,712), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:29:36] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(998,717), area=10, aspect=1.33
explorer: True
detected face: False
^Cpi@raspberrypi:~/JDESL/25-26-PWP-remote $ nano automation.py \
> ^C
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ nano automation.py 
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ python3 main.py 
Pi motor client alive – polling the Mac every 100 ms…
start calibration?y
start calibration?y
executing forward
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
turn right initialized
loaded
0 45
diff 4
loaded
1 45
loaded
0 77
diff 4
loaded
1 12
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
turn left initialized
loaded
0 45
diff 4
loaded
1 45
loaded
0 13
diff 4
loaded
1 76
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
settings are [4, [3.5, -35.0, 1.3], [3.5, 36.0, 1.3]], change differential,left, right?r
test right initial forward delay:3.0
test right turn speed36
test right turn length1.3
executing forward
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
turn right initialized
loaded
0 45
diff 4
loaded
1 45
loaded
0 77
diff 4
loaded
1 12
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
turn left initialized
loaded
0 45
diff 4
loaded
1 45
loaded
0 13
diff 4
loaded
1 76
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
settings are [4, [3.5, -35.0, 1.3], [3.0, 36.0, 1.3]], change differential,left, right?l
test right initial forward delay:3.0
test right turn speed-35
test right turn length1.2
executing forward
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
turn right initialized
loaded
0 45
diff 4
loaded
1 45
loaded
0 77
diff 4
loaded
1 12
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
turn left initialized
loaded
0 45
diff 4
loaded
1 45
loaded
0 13
diff 4
loaded
1 76
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
settings are [4, [3.0, -35.0, 1.2], [3.0, 36.0, 1.3]], change differential,left, right?r
test right initial forward delay:3.0
test right turn speed36
test right turn length1.4
executing forward
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
turn right initialized
loaded
0 45
diff 4
loaded
1 45
loaded
0 77
diff 4
loaded
1 12
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
turn left initialized
loaded
0 45
diff 4
loaded
1 45
loaded
0 13
diff 4
loaded
1 76
loaded
0 45
diff 4
loaded
1 45
stopped 0
stopped 1
settings are [4, [3.0, -35.0, 1.2], [3.0, 36.0, 1.4]], change differential,left, right?end
[ WARN:0@168.001] global ./modules/videoio/src/cap_gstreamer.cpp (1405) open OpenCV | GStreamer warning: Cannot query video position: status=0, value=-1, duration=-1
 * Serving Flask app 'apiserver'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.240.123:5000
Press CTRL+C to quit
192.168.240.18 - - [13/May/2026 09:33:02] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:33:02] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:33:06] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:33:06] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:33:10] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:33:10] "GET /gui HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:33:11] "GET /stream HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:33:12] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(316,698), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:33:13] "GET /stream_processed HTTP/1.1" 200 -
obstacle found: pos=(100,684), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(114,648), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(90,703), area=11, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(132,706), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(139,669), area=11, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(166,606), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:33:16] "POST /play HTTP/1.1" 200 -
obstacle found: pos=(109,662), area=9, aspect=1.33
explorer: False
last_c= 
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(112,656), area=14, aspect=1.25
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:33:17] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(141,691), area=6, aspect=1.00
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(196,686), area=6, aspect=1.00
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(174,706), area=9, aspect=1.33
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:33:19] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1096,660), area=9, aspect=1.33
explorer: False
last_c= r
turn left initialized-following horizontal
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:33:21] "GET /log HTTP/1.1" 200 -
loaded
0 13
diff 4
loaded
1 76
192.168.240.18 - - [13/May/2026 09:33:23] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:33:25] "GET /log HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
obstacle found: pos=(540,708), area=13, aspect=1.40
explorer: False
detected face: False
obstacle found: pos=(446,704), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(354,682), area=20, aspect=1.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:33:27] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(510,717), area=10, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(428,700), area=34, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(506,718), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(510,718), area=8, aspect=2.50
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:33:29] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(554,696), area=24, aspect=1.12
explorer: False
detected face: False
obstacle found: pos=(506,717), area=18, aspect=1.75
explorer: False
detected face: False
obstacle found: pos=(554,696), area=22, aspect=1.75
explorer: False
detected face: False
obstacle found: pos=(444,702), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:33:31] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(509,718), area=8, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(508,717), area=19, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(512,717), area=24, aspect=2.75
explorer: False
detected face: False
obstacle found: pos=(592,704), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:33:33] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(510,717), area=12, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(511,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(510,718), area=12, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(508,718), area=10, aspect=3.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:33:35] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(504,717), area=16, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(510,718), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(508,718), area=8, aspect=2.50
explorer: False
detected face: False
obstacle found: pos=(504,719), area=4, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:33:37] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(586,704), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(584,704), area=26, aspect=2.82
explorer: False
detected face: False
obstacle found: pos=(508,717), area=16, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(557,698), area=18, aspect=1.50
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:33:39] "GET /flog HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:33:39] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(508,718), area=6, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(560,674), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(505,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(508,718), area=14, aspect=2.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:33:41] "GET /flog HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:33:41] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:33:41] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(510,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(593,705), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:33:52] "GET /stream HTTP/1.1" 200 -
obstacle found: pos=(590,704), area=15, aspect=1.25
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:33:54] "GET /stream_processed HTTP/1.1" 200 -
obstacle found: pos=(510,717), area=10, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(586,704), area=24, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(390,690), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(586,704), area=54, aspect=2.45
explorer: False
detected face: False
obstacle found: pos=(508,718), area=8, aspect=2.50
explorer: False
detected face: False
obstacle found: pos=(508,717), area=15, aspect=1.25
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:33:57] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(508,718), area=6, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(588,704), area=28, aspect=2.29
explorer: False
detected face: False
obstacle found: pos=(437,700), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(500,718), area=12, aspect=1.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:33:59] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(382,698), area=32, aspect=1.60
explorer: False
detected face: False
obstacle found: pos=(460,681), area=28, aspect=2.52
explorer: False
detected face: False
obstacle found: pos=(460,694), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:34:01] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(463,687), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(488,716), area=16, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(1172,630), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(458,703), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:34:03] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1098,627), area=21, aspect=2.21
explorer: False
detected face: False
obstacle found: pos=(1028,622), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(482,670), area=18, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(1204,632), area=15, aspect=2.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:34:05] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(470,641), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(497,643), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(460,705), area=21, aspect=2.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:34:07] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1176,630), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(799,603), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(395,528), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(410,719), area=4, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:34:09] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(380,716), area=18, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(411,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(379,705), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:34:11] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(408,710), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(470,397), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(508,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1276,486), area=18, aspect=2.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:34:13] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1006,479), area=36, aspect=2.50
explorer: False
detected face: False
obstacle found: pos=(1218,486), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(1180,484), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(870,473), area=32, aspect=2.75
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:34:15] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1257,488), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1187,484), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(470,717), area=10, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:34:17] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(444,716), area=18, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(736,465), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(435,456), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(892,638), area=18, aspect=2.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:34:19] "POST /play HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:34:19] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1027,480), area=6, aspect=1.00
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
obstacle found: pos=(1169,483), area=6, aspect=1.00
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
obstacle found: pos=(1043,634), area=6, aspect=1.00
explorer: False
last_c= r
turn left initialized-following horizontal
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:34:21] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:34:23] "GET /log HTTP/1.1" 200 -
loaded
0 13
diff 4
loaded
1 76
192.168.240.18 - - [13/May/2026 09:34:25] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
192.168.240.18 - - [13/May/2026 09:34:27] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(194,716), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(175,704), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(175,717), area=10, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(226,718), area=6, aspect=2.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:34:29] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(173,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(176,718), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(240,708), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(232,710), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:34:31] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(192,697), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(173,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(229,715), area=66, aspect=2.25
explorer: False
detected face: False
obstacle found: pos=(236,714), area=42, aspect=1.43
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:34:33] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(174,716), area=26, aspect=1.75
explorer: False
detected face: False
obstacle found: pos=(174,718), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(223,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(225,718), area=6, aspect=2.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:34:35] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(224,716), area=16, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(173,716), area=13, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(266,690), area=19, aspect=2.42
explorer: False
detected face: False
obstacle found: pos=(218,716), area=32, aspect=1.50
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:34:37] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(175,719), area=4, aspect=1.33
explorer: False
detected face: False
^Cpi@raspberrypi:~/JDESL/25-26-PWP-remote $ nano obstacle.py 
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ nano automation.py 
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ python3 main.py 
Pi motor client alive – polling the Mac every 100 ms…
start calibration?n
[ WARN:0@8.305] global ./modules/videoio/src/cap_gstreamer.cpp (1405) open OpenCV | GStreamer warning: Cannot query video position: status=0, value=-1, duration=-1
 * Serving Flask app 'apiserver'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.240.123:5000
Press CTRL+C to quit
192.168.240.18 - - [13/May/2026 09:36:25] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:36:25] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:36:29] "GET /gui HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:36:29] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:36:30] "GET /stream HTTP/1.1" 200 -
obstacle found: pos=(577,363), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:36:32] "GET /stream_processed HTTP/1.1" 200 -
obstacle found: pos=(1214,370), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1122,388), area=18, aspect=2.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:36:33] "POST /play HTTP/1.1" 200 -
obstacle found: pos=(836,368), area=12, aspect=1.67
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(345,639), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:36:34] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(410,439), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(992,583), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(588,702), area=9, aspect=1.33
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(16,694), area=12, aspect=1.67
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:36:36] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(498,625), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(607,203), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:36:38] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1154,468), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(672,698), area=12, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(894,711), area=9, aspect=1.33
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1263,282), area=34, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:36:40] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(808,712), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1227,497), area=34, aspect=1.00
explorer: False
last_c= 
turn left initialized-following horizontal
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:36:42] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:36:44] "GET /log HTTP/1.1" 200 -
loaded
0 13
diff 4
loaded
1 76
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:36:46] "GET /log HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
obstacle found: pos=(197,710), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(172,700), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(197,718), area=6, aspect=2.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:36:48] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(206,707), area=13, aspect=1.40
explorer: False
detected face: False
obstacle found: pos=(213,701), area=15, aspect=1.82
explorer: False
detected face: False
obstacle found: pos=(169,692), area=15, aspect=2.18
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:36:50] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(214,699), area=16, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(159,716), area=26, aspect=1.75
explorer: False
detected face: False
obstacle found: pos=(198,708), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(206,709), area=17, aspect=1.25
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:36:52] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1240,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(194,718), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(180,694), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(222,690), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:36:54] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(199,717), area=15, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(196,718), area=15, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(192,717), area=17, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(196,719), area=4, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:36:56] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(199,714), area=29, aspect=2.25
explorer: False
detected face: False
obstacle found: pos=(201,714), area=40, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(195,718), area=11, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(190,717), area=10, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:36:58] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(210,706), area=11, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(198,717), area=10, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(216,685), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1072,624), area=18, aspect=2.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:00] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1018,668), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1048,715), area=28, aspect=1.60
explorer: False
detected face: False
explorer: False
detected face: False
obstacle found: pos=(509,708), area=78, aspect=2.62
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:02] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(842,694), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(34,706), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(724,669), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(34,712), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:04] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(37,692), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(726,702), area=40, aspect=1.17
explorer: False
detected face: False
obstacle found: pos=(35,707), area=20, aspect=1.50
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:06] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(30,708), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(41,694), area=32, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(19,717), area=12, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(714,698), area=106, aspect=2.57
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:08] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(470,704), area=64, aspect=1.57
explorer: False
detected face: False
obstacle found: pos=(991,705), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1118,702), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:10] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(873,626), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1154,706), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(188,678), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1259,267), area=70, aspect=2.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:12] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(854,496), area=13, aspect=1.40
explorer: False
detected face: False
obstacle found: pos=(863,591), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(866,624), area=14, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(1234,267), area=46, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:14] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1245,267), area=82, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(1205,266), area=94, aspect=2.67
explorer: False
detected face: False
obstacle found: pos=(893,590), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:16] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(984,504), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(872,386), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(869,652), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(853,494), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:18] "POST /play HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:37:18] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(868,628), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1263,268), area=58, aspect=1.67
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(842,369), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1034,435), area=40, aspect=1.17
explorer: False
last_c= 
turn left initialized-following horizontal
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:37:20] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:37:22] "GET /log HTTP/1.1" 200 -
loaded
0 13
diff 4
loaded
1 76
192.168.240.18 - - [13/May/2026 09:37:24] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
obstacle found: pos=(1181,661), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:26] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1204,352), area=14, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(1121,348), area=18, aspect=2.09
explorer: False
detected face: False
obstacle found: pos=(1243,388), area=21, aspect=2.67
explorer: False
detected face: False
obstacle found: pos=(1254,712), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:28] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1086,356), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(1148,354), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1230,366), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(1279,390), area=4, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:30] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1048,414), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1277,679), area=14, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1279,689), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1228,676), area=12, aspect=1.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:32] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1091,642), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1254,677), area=13, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1256,354), area=150, aspect=1.42
explorer: False
detected face: False
obstacle found: pos=(1040,629), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:34] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1275,698), area=22, aspect=2.67
explorer: False
detected face: False
obstacle found: pos=(179,346), area=26, aspect=2.19
explorer: False
detected face: False
obstacle found: pos=(174,342), area=14, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(1188,356), area=24, aspect=1.75
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:36] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1194,354), area=21, aspect=2.67
explorer: False
detected face: False
obstacle found: pos=(1270,664), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1229,373), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1092,356), area=16, aspect=1.25
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:38] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1242,357), area=21, aspect=1.50
explorer: False
detected face: False
obstacle found: pos=(1227,647), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1186,664), area=21, aspect=2.67
explorer: False
detected face: False
obstacle found: pos=(1112,348), area=22, aspect=1.75
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:40] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1234,357), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1128,632), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1144,366), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(1267,679), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:42] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1264,372), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(1135,673), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1204,362), area=18, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(1172,666), area=28, aspect=2.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:44] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1205,646), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(1221,700), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1234,624), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1160,366), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:46] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1269,705), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1277,360), area=10, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1279,551), area=4, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:48] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(214,379), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1204,362), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1136,690), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1081,418), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:50] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1217,703), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1199,366), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1247,344), area=28, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(1239,354), area=23, aspect=2.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:52] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1196,340), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1264,652), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1228,368), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(171,352), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:54] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1191,665), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1264,379), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1265,348), area=41, aspect=2.75
explorer: False
detected face: False
obstacle found: pos=(1229,357), area=6, aspect=1.00
explorer: False
detected face: False
stop called
192.168.240.18 - - [13/May/2026 09:37:56] "GET /log HTTP/1.1" 200 -
stopped 0
stopped 1
[Motordriver] Command sent: stop
192.168.240.18 - - [13/May/2026 09:37:56] "POST /stop HTTP/1.1" 200 -
obstacle found: pos=(1164,368), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(1232,369), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1184,674), area=6, aspect=1.00
explorer: False
detected face: False
^@obstacle found: pos=(1173,634), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:37:58] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1276,361), area=24, aspect=1.75
explorer: False
detected face: False
obstacle found: pos=(1262,373), area=22, aspect=2.13
explorer: False
detected face: False
^Cpi@raspberrypi:~/JDESL/25-26-PWP-remote $ 
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ nano automation.py 
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ python3 main.py 
Pi motor client alive – polling the Mac every 100 ms…
start calibration?n
[ WARN:0@3.066] global ./modules/videoio/src/cap_gstreamer.cpp (1405) open OpenCV | GStreamer warning: Cannot query video position: status=0, value=-1, duration=-1
 * Serving Flask app 'apiserver'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.240.123:5000
Press CTRL+C to quit
192.168.240.18 - - [13/May/2026 09:38:49] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:38:49] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:38:52] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:38:52] "GET /gui HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:38:53] "GET /stream HTTP/1.1" 200 -
obstacle found: pos=(1257,373), area=26, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:38:55] "GET /stream_processed HTTP/1.1" 200 -
obstacle found: pos=(1248,381), area=15, aspect=2.00
explorer: False
detected face: False
obstacle found: pos=(1101,350), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:38:56] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1211,678), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1080,356), area=18, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(1030,436), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1245,346), area=6, aspect=1.00
explorer: False
detected face: False
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: left
192.168.240.18 - - [13/May/2026 09:38:58] "POST /do/left HTTP/1.1" 200 -
obstacle found: pos=(1251,674), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1210,362), area=24, aspect=1.40
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:38:59] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1243,406), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1141,443), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(767,348), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(4,702), area=20, aspect=2.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:39:01] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(689,634), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(856,674), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(1035,716), area=24, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(762,646), area=95, aspect=1.56
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:39:03] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(986,28), area=24, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(1096,658), area=40, aspect=1.17
explorer: False
detected face: False
obstacle found: pos=(1234,536), area=52, aspect=1.50
explorer: False
detected face: False
stop called
explorer: False
detected face: False
stopped 0
stopped 1
[Motordriver] Command sent: stop
192.168.240.18 - - [13/May/2026 09:39:06] "POST /stop HTTP/1.1" 200 -
obstacle found: pos=(171,665), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:39:06] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(285,663), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(0,622), area=2, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(296,663), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(41,637), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:39:08] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(36,602), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(46,632), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(314,719), area=4, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(354,716), area=12, aspect=1.67
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:39:10] "POST /play HTTP/1.1" 200 -
obstacle found: pos=(66,614), area=9, aspect=1.33
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(34,633), area=17, aspect=1.25
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:39:11] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(0,698), area=2, aspect=3.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(360,719), area=4, aspect=1.33
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(580,671), area=6, aspect=1.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:39:13] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(708,716), area=23, aspect=1.17
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(931,673), area=42, aspect=2.63
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1028,718), area=6, aspect=2.00
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(49,206), area=9, aspect=1.33
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:39:15] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1020,680), area=12, aspect=1.67
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(91,314), area=9, aspect=1.33
explorer: False
last_c= 
here
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(623,661), area=6, aspect=1.00
explorer: False
last_c= 
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(563,687), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:39:17] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(134,555), area=15, aspect=2.18
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(169,719), area=4, aspect=1.33
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1184,241), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(814,538), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:39:19] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(676,670), area=34, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(802,700), area=34, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1209,581), area=34, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1094,444), area=9, aspect=1.33
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
192.168.240.18 - - [13/May/2026 09:39:21] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1154,556), area=12, aspect=1.67
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(27,144), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(774,654), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(500,715), area=22, aspect=2.67
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
192.168.240.18 - - [13/May/2026 09:39:23] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(88,698), area=9, aspect=1.33
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(156,532), area=38, aspect=2.40
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(102,708), area=18, aspect=2.33
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
192.168.240.18 - - [13/May/2026 09:39:25] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1181,639), area=34, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(1275,300), area=26, aspect=1.60
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(1279,527), area=4, aspect=1.33
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(823,573), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
192.168.240.18 - - [13/May/2026 09:39:27] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(319,719), area=4, aspect=1.33
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(954,607), area=20, aspect=1.75
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(829,698), area=18, aspect=1.50
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(661,708), area=9, aspect=1.33
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
192.168.240.18 - - [13/May/2026 09:39:29] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(464,653), area=11, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(301,622), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(176,712), area=50, aspect=2.60
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(1060,294), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
192.168.240.18 - - [13/May/2026 09:39:31] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1240,490), area=15, aspect=2.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(1061,494), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(1177,701), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(848,711), area=18, aspect=2.09
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
192.168.240.18 - - [13/May/2026 09:39:33] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(434,716), area=16, aspect=2.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(96,127), area=116, aspect=1.88
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(1278,232), area=8, aspect=2.50
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(686,149), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
192.168.240.18 - - [13/May/2026 09:39:35] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(83,380), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(1176,623), area=15, aspect=2.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(1101,599), area=18, aspect=2.08
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(1017,657), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
192.168.240.18 - - [13/May/2026 09:39:37] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(21,694), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(482,705), area=6, aspect=1.00
explorer: False
last_c= l
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(980,718), area=10, aspect=3.00
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(476,570), area=6, aspect=1.00
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:39:39] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(442,690), area=9, aspect=1.33
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1276,718), area=8, aspect=2.50
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
obstacle found: pos=(1111,672), area=21, aspect=2.80
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
obstacle found: pos=(596,712), area=66, aspect=2.46
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
192.168.240.18 - - [13/May/2026 09:39:41] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(866,703), area=6, aspect=1.00
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
obstacle found: pos=(1045,640), area=6, aspect=1.00
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
obstacle found: pos=(1031,719), area=4, aspect=1.33
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
192.168.240.18 - - [13/May/2026 09:39:43] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(983,719), area=4, aspect=1.33
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(213,718), area=6, aspect=2.00
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(730,710), area=18, aspect=2.33
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1216,715), area=30, aspect=2.00
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:39:45] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1143,719), area=4, aspect=1.33
explorer: False
last_c= r
howdy
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1256,540), area=12, aspect=1.67
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
obstacle found: pos=(524,312), area=6, aspect=1.00
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
192.168.240.18 - - [13/May/2026 09:39:47] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(242,719), area=4, aspect=1.33
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
obstacle found: pos=(949,441), area=6, aspect=1.00
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
obstacle found: pos=(1246,680), area=12, aspect=1.67
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
obstacle found: pos=(164,629), area=6, aspect=1.00
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
192.168.240.18 - - [13/May/2026 09:39:49] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(471,624), area=11, aspect=1.00
explorer: False
last_c= r
here
loaded
0 31
diff 4
loaded
1 58
detected face: False
obstacle found: pos=(840,633), area=9, aspect=1.33
explorer: False
last_c= r
turn left initialized-following horizontal
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:39:51] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:39:53] "GET /log HTTP/1.1" 200 -
loaded
0 13
diff 4
loaded
1 76
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: backward
192.168.240.18 - - [13/May/2026 09:39:55] "GET /log HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
obstacle found: pos=(190,76), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(192,50), area=14, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(67,186), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:39:57] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(191,54), area=14, aspect=1.25
explorer: False
detected face: False
obstacle found: pos=(2,148), area=12, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(1089,182), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:39:59] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(108,78), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(11,120), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(174,556), area=24, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(291,88), area=9, aspect=1.33
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:40:01] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(440,85), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(129,74), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(246,52), area=15, aspect=2.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:40:03] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(179,73), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(94,80), area=12, aspect=1.67
explorer: False
detected face: False
obstacle found: pos=(193,50), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(57,140), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:40:05] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(192,58), area=44, aspect=2.55
explorer: False
detected face: False
obstacle found: pos=(191,68), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(344,394), area=6, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(425,339), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:40:07] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(2,116), area=8, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(0,112), area=2, aspect=3.00
explorer: False
detected face: False
obstacle found: pos=(122,123), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:40:09] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(464,110), area=18, aspect=2.33
explorer: False
detected face: False
obstacle found: pos=(820,251), area=34, aspect=1.00
explorer: False
detected face: False
obstacle found: pos=(166,198), area=9, aspect=1.33
explorer: False
detected face: False
obstacle found: pos=(218,12), area=6, aspect=1.00
explorer: False
detected face: False
192.168.240.18 - - [13/May/2026 09:40:11] "POST /play HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:40:11] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(44,672), area=6, aspect=1.00
explorer: False
last_c= r
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(80,182), area=9, aspect=1.33
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(338,22), area=12, aspect=1.67
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(199,149), area=6, aspect=1.00
explorer: False
192.168.240.18 - - [13/May/2026 09:40:13] "GET /log HTTP/1.1" 200 -
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(126,462), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(21,400), area=6, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1154,686), area=44, aspect=1.00
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
192.168.240.18 - - [13/May/2026 09:40:15] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1252,653), area=149, aspect=1.82
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(215,658), area=6, aspect=1.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(158,684), area=12, aspect=1.67
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
obstacle found: pos=(279,718), area=6, aspect=2.00
explorer: False
last_c= l
here
loaded
0 58
diff 4
loaded
1 31
detected face: False
192.168.240.18 - - [13/May/2026 09:40:17] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(313,592), area=30, aspect=1.11
explorer: False
last_c= l
heyo
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
detected face: False
obstacle found: pos=(1094,618), area=50, aspect=1.14
explorer: False
last_c= l
detected face: False
obstacle found: pos=(1276,553), area=23, aspect=1.75
explorer: True
loaded
0 54
diff 4
loaded
1 36
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:40:19] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
192.168.240.18 - - [13/May/2026 09:40:21] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:40:23] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:40:25] "GET /log HTTP/1.1" 200 -
loaded
0 18
diff 4
loaded
1 72
192.168.240.18 - - [13/May/2026 09:40:27] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:40:29] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
192.168.240.18 - - [13/May/2026 09:40:31] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(111,502), area=106, aspect=3.00
explorer: True
detected face: False
obstacle found: pos=(290,539), area=239, aspect=1.20
explorer: True
detected face: False
obstacle found: pos=(274,553), area=64, aspect=1.83
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:40:33] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(22,570), area=64, aspect=1.43
explorer: True
detected face: False
obstacle found: pos=(252,552), area=78, aspect=1.71
explorer: True
detected face: False
obstacle found: pos=(254,552), area=136, aspect=3.00
explorer: True
detected face: False
obstacle found: pos=(383,540), area=122, aspect=2.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:40:35] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(66,566), area=46, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(16,570), area=88, aspect=1.50
explorer: True
detected face: False
obstacle found: pos=(46,567), area=124, aspect=2.00
explorer: True
detected face: False
stop called
192.168.240.18 - - [13/May/2026 09:40:37] "GET /log HTTP/1.1" 200 -
stopped 0
stopped 1
[Motordriver] Command sent: stop
192.168.240.18 - - [13/May/2026 09:40:37] "POST /stop HTTP/1.1" 200 -
obstacle found: pos=(425,537), area=34, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(31,568), area=161, aspect=2.22
explorer: True
detected face: False
obstacle found: pos=(378,541), area=92, aspect=1.62
explorer: True
detected face: False
obstacle found: pos=(382,540), area=126, aspect=2.12
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:40:39] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(294,544), area=294, aspect=1.22
explorer: True
detected face: False
obstacle found: pos=(28,568), area=192, aspect=2.86
explorer: True
detected face: False
obstacle found: pos=(426,538), area=64, aspect=1.43
explorer: True
detected face: False
obstacle found: pos=(290,544), area=238, aspect=1.06
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:40:41] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(246,553), area=40, aspect=1.17
explorer: True
detected face: False
obstacle found: pos=(384,542), area=164, aspect=2.67
explorer: True
detected face: False
obstacle found: pos=(30,568), area=155, aspect=2.62
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:40:43] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(4,450), area=20, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(204,557), area=134, aspect=2.50
explorer: True
detected face: False
obstacle found: pos=(380,541), area=164, aspect=2.48
explorer: True
detected face: False
obstacle found: pos=(35,568), area=126, aspect=1.78
explorer: True
detected face: False
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:40:45] "POST /do/forward HTTP/1.1" 200 -
obstacle found: pos=(401,540), area=34, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:40:46] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(386,640), area=77, aspect=1.38
explorer: True
detected face: False
obstacle found: pos=(271,702), area=34, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1254,568), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(32,52), area=6, aspect=1.00
explorer: True
detected face: False
loaded
192.168.240.18 - - [13/May/2026 09:40:48] "GET /log HTTP/1.1" 200 -
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: right
192.168.240.18 - - [13/May/2026 09:40:48] "POST /do/right HTTP/1.1" 200 -
obstacle found: pos=(1212,475), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1031,171), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1120,671), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(859,551), area=12, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:40:50] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(392,104), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(13,628), area=15, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1152,706), area=50, aspect=1.14
explorer: True
detected face: False
obstacle found: pos=(54,496), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:40:52] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(96,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(671,689), area=34, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(360,661), area=21, aspect=2.67
explorer: True
detected face: False
obstacle found: pos=(247,574), area=15, aspect=2.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:40:54] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(38,698), area=35, aspect=3.00
explorer: True
detected face: False
obstacle found: pos=(20,204), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(764,40), area=12, aspect=1.67
explorer: True
detected face: False
loaded
0 45
diff 4
192.168.240.18 - - [13/May/2026 09:40:56] "GET /log HTTP/1.1" 200 -
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:40:56] "POST /do/forward HTTP/1.1" 200 -
obstacle found: pos=(1141,656), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1047,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1038,372), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1168,696), area=6, aspect=1.00
explorer: True
detected face: False
loaded
0 45
diff 4
192.168.240.18 - - [13/May/2026 09:40:58] "GET /log HTTP/1.1" 200 -
loaded
1 45
[Motordriver] Command sent: left
192.168.240.18 - - [13/May/2026 09:40:58] "POST /do/left HTTP/1.1" 200 -
obstacle found: pos=(708,673), area=16, aspect=1.25
explorer: True
detected face: False
obstacle found: pos=(1265,221), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(297,696), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1276,228), area=12, aspect=1.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:41:00] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(975,328), area=21, aspect=2.67
explorer: True
detected face: False
obstacle found: pos=(1194,374), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(974,614), area=13, aspect=1.40
explorer: True
detected face: False
loaded
0 45
diff 4
loaded
1 45
192.168.240.18 - - [13/May/2026 09:41:02] "GET /log HTTP/1.1" 200 -
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:41:02] "POST /do/forward HTTP/1.1" 200 -
obstacle found: pos=(190,681), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(839,297), area=89, aspect=2.97
explorer: True
detected face: False
loaded
192.168.240.18 - - [13/May/2026 09:41:03] "GET /log HTTP/1.1" 200 -
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:41:03] "POST /do/forward HTTP/1.1" 200 -
obstacle found: pos=(855,359), area=11, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(661,686), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:41:04] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(877,584), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1156,716), area=12, aspect=1.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:41:05] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1087,660), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1276,698), area=18, aspect=2.33
explorer: True
detected face: False
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:41:06] "POST /do/forward HTTP/1.1" 200 -
obstacle found: pos=(1279,709), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(127,540), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:41:07] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:41:07] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(14,626), area=24, aspect=3.00
explorer: True
detected face: False
obstacle found: pos=(359,658), area=9, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:41:08] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(20,674), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(107,625), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1,638), area=6, aspect=1.50
explorer: True
detected face: False
obstacle found: pos=(179,301), area=17, aspect=2.14
explorer: True
detected face: False
obstacle found: pos=(283,671), area=12, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(85,643), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(554,716), area=18, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(702,715), area=22, aspect=2.67
explorer: True
detected face: False
loaded
0 45
diff 4
loaded
1 45
192.168.240.18 - - [13/May/2026 09:41:12] "GET /log HTTP/1.1" 200 -
[Motordriver] Command sent: right
192.168.240.18 - - [13/May/2026 09:41:12] "POST /do/right HTTP/1.1" 200 -
obstacle found: pos=(839,652), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(805,680), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:41:13] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(672,692), area=12, aspect=1.67
explorer: True
detected face: False
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:41:14] "POST /do/forward HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:41:14] "POST /do/forward HTTP/1.1" 200 -
obstacle found: pos=(628,698), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:41:14] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(543,644), area=16, aspect=1.25
explorer: True
detected face: False
obstacle found: pos=(576,716), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(260,712), area=13, aspect=1.40
explorer: True
detected face: False
obstacle found: pos=(450,694), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(312,719), area=4, aspect=1.33
explorer: True
detected face: False
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: right
192.168.240.18 - - [13/May/2026 09:41:17] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:41:17] "POST /do/right HTTP/1.1" 200 -
obstacle found: pos=(841,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(768,715), area=24, aspect=1.60
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:41:18] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(76,702), area=18, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(1044,425), area=88, aspect=2.50
explorer: True
detected face: False
obstacle found: pos=(47,414), area=58, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(68,705), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1216,437), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1006,395), area=6, aspect=1.00
explorer: True
detected face: False
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:41:22] "POST /do/forward HTTP/1.1" 200 -
obstacle found: pos=(1226,605), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(624,350), area=9, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:41:23] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:41:23] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(987,696), area=44, aspect=2.98
explorer: True
detected face: False
obstacle found: pos=(856,678), area=12, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(718,718), area=12, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(524,718), area=10, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(345,705), area=14, aspect=3.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:41:26] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(202,702), area=17, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(242,703), area=34, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(340,692), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(434,718), area=8, aspect=2.50
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:41:28] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(547,716), area=26, aspect=1.17
explorer: True
detected face: False
obstacle found: pos=(613,684), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(688,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(799,718), area=6, aspect=2.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:41:30] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(940,694), area=30, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1027,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1116,718), area=8, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1198,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:41:32] "POST /play HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:41:32] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(874,693), area=15, aspect=2.00
explorer: True
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:41:34] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:41:36] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:41:38] "GET /log HTTP/1.1" 200 -
loaded
0 18
diff 4
loaded
1 72
192.168.240.18 - - [13/May/2026 09:41:40] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:41:42] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
192.168.240.18 - - [13/May/2026 09:41:44] "GET /log HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
obstacle found: pos=(1000,714), area=24, aspect=3.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:41:46] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(543,634), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(966,715), area=22, aspect=2.67
explorer: True
detected face: False
obstacle found: pos=(765,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(759,718), area=6, aspect=2.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:41:48] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(759,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(994,716), area=18, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(761,718), area=10, aspect=3.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:41:50] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(777,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(994,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(966,715), area=22, aspect=2.67
explorer: True
detected face: False
obstacle found: pos=(963,717), area=10, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:41:52] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:41:52] "POST /play HTTP/1.1" 200 -
obstacle found: pos=(995,719), area=4, aspect=1.33
explorer: True
192.168.240.18 - - [13/May/2026 09:41:54] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:41:56] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:41:58] "POST /play HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:41:59] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
192.168.240.18 - - [13/May/2026 09:42:01] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:42:03] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:42:05] "GET /log HTTP/1.1" 200 -
loaded
0 18
diff 4
loaded
1 72
192.168.240.18 - - [13/May/2026 09:42:07] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:42:09] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
192.168.240.18 - - [13/May/2026 09:42:11] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(165,712), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(144,698), area=15, aspect=1.25
explorer: True
detected face: False
obstacle found: pos=(94,697), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:13] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(127,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(86,716), area=18, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(88,706), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(84,715), area=22, aspect=2.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:15] "POST /play HTTP/1.1" 200 -
obstacle found: pos=(118,658), area=28, aspect=2.18
explorer: True
turn right initialized
192.168.240.18 - - [13/May/2026 09:42:16] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:42:18] "GET /log HTTP/1.1" 200 -
loaded
0 81
diff 4
loaded
1 8
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:42:20] "GET /log HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
obstacle found: pos=(1196,568), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1073,587), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1139,535), area=12, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:22] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(998,511), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1010,458), area=24, aspect=3.00
explorer: True
detected face: False
obstacle found: pos=(1239,495), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1266,455), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:24] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1174,464), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1174,528), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1276,238), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(1277,458), area=10, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:26] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1260,347), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1172,260), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1257,316), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1248,484), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:28] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1113,531), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(673,200), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(858,320), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(763,316), area=9, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:30] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1085,522), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1020,239), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(572,256), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1058,457), area=23, aspect=1.75
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:32] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1198,327), area=22, aspect=2.67
explorer: True
detected face: False
obstacle found: pos=(934,409), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1270,450), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1009,453), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:34] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1266,465), area=19, aspect=1.92
explorer: True
detected face: False
obstacle found: pos=(1259,372), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(989,449), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1112,536), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:36] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1180,516), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1093,472), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1240,481), area=17, aspect=1.25
explorer: True
detected face: False
obstacle found: pos=(1047,497), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:38] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1274,146), area=26, aspect=2.25
explorer: True
detected face: False
obstacle found: pos=(1127,221), area=26, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1188,516), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(680,473), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:40] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1195,470), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(928,250), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1049,498), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1080,475), area=15, aspect=2.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:42] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1184,391), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1092,476), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1010,457), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1256,320), area=12, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:44] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1186,387), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(768,317), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1016,424), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:46] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1105,510), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1257,314), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1210,477), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1204,468), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:48] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1013,456), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1203,475), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1278,468), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1029,438), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:50] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1149,492), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1227,556), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1278,471), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1107,498), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:52] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1196,234), area=14, aspect=1.25
explorer: True
detected face: False
obstacle found: pos=(1251,262), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1136,480), area=18, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(1144,539), area=21, aspect=2.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:54] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1276,290), area=18, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(1244,259), area=16, aspect=1.25
explorer: True
detected face: False
obstacle found: pos=(1276,468), area=18, aspect=1.25
explorer: True
detected face: False
obstacle found: pos=(762,320), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:56] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(764,318), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(1155,326), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1192,366), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:42:58] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1267,397), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1260,492), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(1079,558), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(986,512), area=12, aspect=1.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:00] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(836,352), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1126,487), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(311,237), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1037,491), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:02] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1012,518), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1248,491), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1105,538), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1173,538), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:04] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1114,443), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1262,464), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1089,480), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1110,212), area=15, aspect=2.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:06] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1248,479), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1260,494), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1230,470), area=26, aspect=2.25
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:08] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1114,535), area=18, aspect=1.71
explorer: True
detected face: False
obstacle found: pos=(1240,312), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1279,366), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1277,544), area=10, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:10] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1178,536), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1169,27), area=12, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1162,680), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(1245,705), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:12] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(813,708), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1094,718), area=8, aspect=2.50
explorer: True
detected face: False
obstacle found: pos=(1088,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:14] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(981,717), area=14, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1050,718), area=8, aspect=2.50
explorer: True
detected face: False
obstacle found: pos=(1050,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1232,698), area=18, aspect=2.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:16] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(884,708), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(1058,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1057,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:18] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(997,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1057,718), area=10, aspect=3.00
explorer: True
detected face: False
obstacle found: pos=(1092,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(1220,697), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:20] "GET /gui HTTP/1.1" 200 -
obstacle found: pos=(975,717), area=12, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(1058,718), area=10, aspect=3.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:21] "GET /stream HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:43:22] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1057,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:23] "GET /stream_processed HTTP/1.1" 200 -
obstacle found: pos=(1056,719), area=4, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(686,698), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:24] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1092,718), area=8, aspect=2.50
explorer: True
detected face: False
obstacle found: pos=(1040,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(1093,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(746,702), area=18, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(1098,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(960,716), area=18, aspect=2.33
explorer: True
detected face: False
obstacle found: pos=(1058,718), area=6, aspect=2.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:28] "POST /play HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:43:28] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(1098,690), area=15, aspect=2.00
explorer: True
loaded
0 54
diff 4
loaded
1 36
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:43:30] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:43:32] "GET /log HTTP/1.1" 200 -
192.168.240.18 - - [13/May/2026 09:43:34] "GET /log HTTP/1.1" 200 -
loaded
0 18
diff 4
loaded
1 72
192.168.240.18 - - [13/May/2026 09:43:36] "GET /log HTTP/1.1" 200 -
loaded
0 45
diff 4
loaded
1 45
[Motordriver] Command sent: forward
192.168.240.18 - - [13/May/2026 09:43:38] "GET /log HTTP/1.1" 200 -
loaded
0 67
diff 4
loaded
1 22
192.168.240.18 - - [13/May/2026 09:43:40] "GET /log HTTP/1.1" 200 -
stop called
stopped 0
stopped 1
[Motordriver] Command sent: stop
detected face: False
obstacle found: pos=(552,346), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(496,719), area=4, aspect=1.33
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:42] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(470,601), area=15, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(412,254), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(478,634), area=12, aspect=1.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:44] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(296,234), area=12, aspect=1.67
explorer: True
detected face: False
obstacle found: pos=(569,676), area=14, aspect=1.25
explorer: True
detected face: False
obstacle found: pos=(503,715), area=30, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(485,655), area=6, aspect=1.00
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:46] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(467,582), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(492,687), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(501,718), area=6, aspect=2.00
explorer: True
detected face: False
obstacle found: pos=(472,610), area=12, aspect=1.67
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:48] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(568,676), area=11, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(496,581), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(571,677), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(570,676), area=24, aspect=1.20
explorer: True
detected face: False
192.168.240.18 - - [13/May/2026 09:43:50] "GET /log HTTP/1.1" 200 -
obstacle found: pos=(74,288), area=9, aspect=1.33
explorer: True
detected face: False
obstacle found: pos=(494,692), area=6, aspect=1.00
explorer: True
detected face: False
obstacle found: pos=(500,711), area=6, aspect=1.00
explorer: True
detected face: False
^Cpi@raspberrypi:~/JDESL/25-26-PWP-remote $ git add .
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ find .git/objects/ -type f -empty -delete
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ git add .
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ git commit -m "thing"
fatal: could not parse HEAD
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ git commit -m "thing"
fatal: could not parse HEAD
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ git log
fatal: bad object HEAD
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ git fsck -full
error: did you mean `--full` (with two dashes)?
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ git fsck --full
Checking object directories: 100% (256/256), done.
Checking objects: 100% (159/159), done.
error: refs/heads/master: invalid sha1 pointer 20de0da523b94548546924a1263782882528cd55
error: refs/remotes/origin/master: invalid sha1 pointer 20de0da523b94548546924a1263782882528cd55
error: HEAD: invalid sha1 pointer 20de0da523b94548546924a1263782882528cd55
dangling blob 51c8cda3e3a6a18316dc4a69e5752392328b9eca
dangling blob 77b64188a6a63de5519b8ecdea5534059f17c27c
dangling blob 94be066b402d20af6dd4eab1bc13ec86a77e1a58
dangling blob bf5237882ae684bc29f2c346d6164dffe6431700
dangling blob cc28109c4c574d0944f1fc76f622a5d63b3dcb6a
dangling blob 0511bf9b3e4f18316e1df4a71f22e5e0f6d17311
dangling blob 40efe049fc12cd3ee6413392078a72ed15eb5565
dangling blob 5d1fc429a4a8803fda55df06cc58f4c7c124d17f
dangling blob 93fb0d7948ae3c72798985bfc91318feda93f32f
dangling blob 9bc10f29e2d78fddbf9b90820b63fd4042d2fcb5
dangling blob c4415a1d392a0f163554ec66424b6eccacbce4e2
dangling blob c425aca9e8f9ef8474846d84455a480e873c1a55
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ git commit
fatal: could not parse HEAD
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ git reset
fatal: Could not parse object 'HEAD'.
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ ^C
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ ^C
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ exit
logout
Connection to 192.168.240.123 closed.
pl1013184@7118L06 ~ % 
  [Restored May 15, 2026 at 7:49:23 AM]
Last login: Fri May 15 07:49:23 on ttys000
Restored session: Thu May 14 08:48:38 EDT 2026
pl1013184@7118L06 ~ % ssh pi@192.168.240.123
pi@192.168.240.123's password: 
Permission denied, please try again.
pi@192.168.240.123's password: 
Linux raspberrypi 6.12.47+rpt-rpi-v7 #1 SMP Raspbian 1:6.12.47-1+rpt1~bookworm (2025-09-16) armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed May 13 09:46:55 2026 from 192.168.240.6

SSH is enabled and the default password for the 'pi' user has not been changed.
This is a security risk - please login as the 'pi' user and type 'passwd' to set a new password.

pi@raspberrypi:~ $ git log
fatal: not a git repository (or any of the parent directories): .git
pi@raspberrypi:~ $ cd  ..
pi@raspberrypi:/home $ ls
pi
pi@raspberrypi:/home $ cd pi
pi@raspberrypi:~ $ cd JDESL/
pi@raspberrypi:~/JDESL $ ls
25-26-PWP-remote  api_jeremy  apiserver.py  automation1  automation.py  bcm2835-1.70  bcm2835-1.70.tar.gz  GUI_Jeremy.py  Lilly_code  PWP2025-JDESL  suri_code  users.db
pi@raspberrypi:~/JDESL $ cd 25-26-PWP-remote/
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ ls
apiserver.py   calibrate.py  log_store.py  main.py               Motordriver.py     obstacle.py  pi_client.py            __pycache__  setting.txt  trial.py
automation.py  cvclass.py    log.txt       martian_detection.py  motor_steering.py  PCA9685.py   processing_parallel.py  README.md    templates    wanted.jpg
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ git log
fatal: bad object HEAD
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ git reset
fatal: Could not parse object 'HEAD'.
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ nano automation.py 
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ cat automation.py 



import pickle as pck
try:
    settings=pck.load(open('setting.txt','rb'))
except:
    settings=[None,[3.8,-40,1.5],[3,40,1]]

"""
Purpose:
Control the robot's automatic movement.

Pseudocode:
1. Check whether auto mode is running.
2. Check whether a stop line has already been detected.
3. Receive the newest camera frame from the server layer.
4. Process the frame using OpenCV.
5. Use the steering value to control motor speeds.
6. If the horizontal stop line is detected, wait a few seconds so the robot
   can pass over the line, then stop the robot.
7. Allow the GUI Play/Stop buttons to start and stop automation.
"""

import time
import processing_parallel
from processing_parallel import process_frame
from motor_steering import set_motor_speeds
from Motordriver import stop_all,_send_command,turn_right
from obstacle import avoid_obstacle
from log_store import log_sto

# Auto-mode state variables
auto_running = False
stop_line_seen = False
stop_time = None

# How long the robot should keep moving after it detects the horizontal tape
# before stopping. You can tune this later if needed.
STOP_DELAY_SECONDS = 2.0


def start_automation():
    """
    Turn on automatic line-following mode.
    """
    global auto_running, stop_line_seen, stop_time,stopped
    stopped=True
    auto_running = True
    stop_line_seen = False
    stop_time = None


def stop_automation(pause=False):
    """
    Turn off automatic line-following mode and stop the robot.
    """
    global auto_running, stop_line_seen, stop_time, stopped

    auto_running = pause
    stopped =False
    stop_line_seen = False
    stop_time = None
    explorer=False
    stop_all()


def is_running():
    """
    Return whether automatic mode is currently active.
    """
    return auto_running
last_c=""
def explorer(l,right,horizontal):
    #print("explorer:",explored)
    global last_c
    if not auto_running:
        print('ended due to stop')
        log_sto('ended due to stop')
        return False
    print("last_c=",last_c)
    if l and right:
        return True
    if horizontal:
        print('turn left initialized-following horizontal')
        log_sto('turn left initialized-following horizontal')
        _send_command('forward')
        time.sleep(settings[1][0])
#        print('turn right initialized')
        set_motor_speeds(settings[1][1])
        time.sleep(settings[1][2])
        _send_command('backward')
        time.sleep(1)
        stop_automation(True)
        #return False
    elif horizontal and right:
        print('turn right initialized')
        log_sto('turn right initialized')
        _send_command('forward')
        time.sleep(settings[2][0])
        #print("turn right initialized")
        set_motor_speeds(settings[2][1])
        time.sleep(settings[2][2])
        _send_command('forward')
        time.sleep(1)
        stop_automation(True)
        #return False
    elif horizontal and l:
        print('turn left initialized')
        log_sto('turn left initialized')
        _send_command('forward')
        time.sleep(settings[1][0])
#        print('turn right initialized')
        set_motor_speeds(settings[1][1])
        time.sleep(settings[1][2])
        _send_command('forward')
        time.sleep(5)
        stop_automation(True)
        #return False
    elif l:
        last_c="l"
        print('heyo')
        _send_command('forward')
    elif right:
        last_c='r'
        print('howdy')
        _send_command('forward')
    else:
        print('here')
        if last_c == 'l':
            set_motor_speeds(15)
        elif last_c == 'r':
            set_motor_speeds(-15)
        elif last_c=="":
            #print("here")
            _send_command("forward")
    return False
explored=False
def update_automation(frame):
    """
    Process one frame of video and update robot behavior.

    Parameters:
        frame: The newest camera frame.

    Returns:
        out: The processed overlay image.
    """
    global auto_running, stop_line_seen, stop_time, explored,stopped


    # Always process the frame so the processed stream can still display overlays
    out, steering_value, stop_line_detected, center_line,left,right,det,obst = process_frame(frame)
    print("explorer:",explored)
    log_sto("explorer mode:"+str(explored)+" ")
    if not auto_running or not stopped:
        return out,det
    if not explored:
        explored = explorer(left,right,stop_line_detected)
        return out,det
    # If the stop line is detected for the first time, start the stop timer
    if stop_line_detected and not stop_line_seen:
        stop_line_seen = True
        stop_time = time.time()

    # If the robot has already seen the stop line, keep going for a short delay,
    # then stop completely
    if stop_line_seen and left and not center_line:
        print('turn right initialized')
        #_send_command('forward')
        time.sleep(3.0)
        #print("turn right initialized")
        set_motor_speeds(40)
        time.sleep(1)
        _send_command('forward')
        time.sleep(1)
        stop_automation()
        return out,det
    if stop_line_seen and right and not center_line:
        print('turn left initialized')
        #_send_command('forward')
        time.sleep(3.8)
#        print('turn right initialized')
        set_motor_speeds(-40)
        time.sleep(1.0)
        _send_command('forward')
        time.sleep(5)
        stop_automation()
        return out,det
    elif stop_line_seen and not center_line:
        elapsed = time.time() - stop_time
        time.sleep(6.0)
        if elapsed >= STOP_DELAY_SECONDS:
            stop_automation()
            return out,det
    if center_line:
    # Normal line-following behavior
        print('hi')
        _send_command('forward')
    elif left:
        set_motor_speeds(10.0)
    elif right:
        set_motor_speeds(-10.0)
    else:
        stop_automation(True)
    if obst:
        log_sto('found obstacle... avoiding')
        avoid_obstacle()
        stop_automation(True)
    return out,det
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ cat log_store.py 
from datetime import datetime as dt
from datetime import timezone
utc_dt=dt.now(timezone.utc)
l_dt=utc_dt.astimezone()
partial_l=""
try:
    openlog=open("log.txt","x")
    openlog.close()
    #openlog = open("log.txt","a+")
except:
    openlog=open("log.txt","w")
    openlog.write("")
    openlog.close()
def log_sto(info):
    partial_log=""
    openlog = open("log.txt","a+")
    openlog.write(info+"["+l_dt.now().strftime("%H:%M:%S")+"]"+"<br>\n")
    openlog.seek(0)
    for i in openlog.readlines()[-32:]:
        partial_log+=i.replace("\n","")
    return partial_log
def gimmefull():
    read=open("log.txt","r")
    return read.read()
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ la
-bash: la: command not found
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ ls
apiserver.py   calibrate.py  log_store.py  main.py               Motordriver.py     obstacle.py  pi_client.py            __pycache__  setting.txt  trial.py
automation.py  cvclass.py    log.txt       martian_detection.py  motor_steering.py  PCA9685.py   processing_parallel.py  README.md    templates    wanted.jpg
pi@raspberrypi:~/JDESL/25-26-PWP-remote $ nano calibrate.py 

  GNU nano 7.2                                                                           calibrate.py                                                                                     
        except:
                def_data=[4,[3.8,-40,1.5],[3,40,1]]
                try:
                        settings=pk.load(open('setting.txt','rb'))
                except:
                        settings=def_data
        print('executing forward')
        cli.execute_command('forward')
        time.sleep(4)
        cli.execute_command('stop')
        time.sleep(2)
        print('turn right initialized')
        cli.execute_command('forward')
        time.sleep(settings[2][0])
        #print("turn right initialized")
        set_motor_speeds(settings[2][1])
        time.sleep(settings[2][2])
        cli.execute_command('forward')
        time.sleep(1)
        cli.execute_command('stop')
        time.sleep(2)
        print('turn left initialized')
        cli.execute_command('forward')
        time.sleep(settings[1][0])
        #print("turn right initialized")
        set_motor_speeds(settings[1][1])
        time.sleep(settings[1][2])
        cli.execute_command('forward')
        time.sleep(1)
        cli.execute_command('stop')
        i_n=input(f'settings are {settings}, change differential,left, right?')
        if 'end' not in i_n:
                if 'd'in i_n.lower() and not ('r'in i_n.lower() or 'l'in i_n.lower()):
                        with open('setting.txt','wb') as wr:
                                settings[0]=int(input('test differential:'))
                                pk.dump(settings,wr)
                elif 'r'in i_n.lower() and not ('l' in i_n.lower() or 'd' in i_n.lower()):
                        with open('setting.txt','wb') as wr:
                                settings[2][0]=float(input('test right initial forward delay:'))
                                settings[2][1]=float(input('test right turn speed'))
                                settings[2][2]=float(input('test right turn length'))
                                pk.dump(settings,wr)
                elif 'l'in i_n.lower() and not ('r' in i_n.lower() or 'd' in i_n.lower()):
                        with open('setting.txt','wb') as wr:
                                settings[1][0]=float(input('test right initial forward delay:'))
                                settings[1][1]=float(input('test right turn speed'))
                                settings[1][2]=float(input('test right turn length'))
                                pk.dump(settings,wr)

                calibrate()
calibrate()
