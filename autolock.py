import pyudev
import subprocess

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

lockScreen = "loginctl lock-session 3"
notify = "notify-send 'Titan key connected'"

for device in iter(monitor.poll, None):
	if device.action == 'add':
		if device.device_path == '/devices/pci0000:00/0000:00:01.3/0000:01:00.0/usb1/1-3/1-3:1.0':
			process = subprocess.Popen(notify.split(), stdout=subprocess.PIPE)
			output, error = process.communicate()

	if device.action == 'remove':
		if device.device_path == '/devices/pci0000:00/0000:00:01.3/0000:01:00.0/usb1/1-3/1-3:1.0':
			process = subprocess.Popen(lockScreen.split(), stdout=subprocess.PIPE)
			output, error = process.communicate()
		elif device.device_path == "/devices/pci0000:00/0000:00:01.3/0000:01:00.0/usb1/1-3":
			process = subprocess.Popen(lockScreen.split(), stdout=subprocess.PIPE)
			output, error = process.communicate()
