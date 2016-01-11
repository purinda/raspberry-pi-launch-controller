#!/bin/sh
# launch-controller.sh	Phoenix Launch Controller service daemon
#
# Version:
#   1.0  04-Jan-2015  purinda@gmail.com
#
# Purpose:
#   This init script is responsible for detecting the launch controller hardware interface and
#   starting up or shutting down the user interface according to the state of the launch controller main switch.
#
#   This script depend on 'gpio' utility within the WiringPi package.
#   Refer to following documents if commands use within this script is not self explanatory.
#    - http://www.crompton.com/hamradio/BeagleBoneBlackAllstar/GPIO_how-to.pdf
#    - https://projects.drogon.net/raspberry-pi/wiringpi/the-gpio-utility/
#

### BEGIN INIT INFO
# Provides:          phoenix-launch-controller
# Required-Start:    $local_fs $network
# Required-Stop:     $local_fs $network
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
DAEMON=/usr/local/bin/gpio
NAME=phoenix-launch-controller
DESC=phoenix-launch-controller

#
# Function that starts the daemon/service
#
do_start()
{
    $DAEMON wfi 26 both
    $DAEMON read 26

	#   0 if daemon has been started
	#   1 if daemon was already running
	#   2 if daemon could not be started
	start-stop-daemon --start --quiet --pidfile $PID --exec $DAEMON --test > /dev/null \
		|| return 1
	start-stop-daemon --start --quiet --pidfile $PID --exec $DAEMON -- \
		$DAEMON_OPTS 2>/dev/null \
		|| return 2
}

#
# Function that stops the daemon/service
#
do_stop()
{
	# Return
	#   0 if daemon has been stopped
	#   1 if daemon was already stopped
	#   2 if daemon could not be stopped
	#   other if a failure occurred
	start-stop-daemon --stop --quiet --retry=$STOP_SCHEDULE --pidfile $PID --name $NAME
	RETVAL="$?"

	sleep 1
	return "$RETVAL"
}