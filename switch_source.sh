#!/bin/sh

J2M_USB_SINK=1
J2M_BLU_SINK=2

if [[ -z $J2M_AUDIO_SINK ]]
then 
	echo "Setting default audio sink to USB"
	# default to usb sink if not set
	export J2M_AUDIO_SINK=$J2M_USB_SINK
fi

#switch from USB to Bluetooth
if [[ $J2M_AUDIO_SINK -eq $J2M_USB_SINK ]] 
then

	# gets the pulseaudio index for bluetooth device
	index=$(pacmd list-sinks | awk '{if ($1 == "index:") {i=$2; getline; if($0 ~ "blue") print i}}')
	echo "Attempting to switch from USB to Bluetooth sink"
	echo "index=$index"

	#check that the audio device index was found
	#and switch to Bluetooth if so
	if [ $index ]
	then
		$(pacmd set-default-sink $index)
		$(sudo systemctl restart mopidy)
		echo "Current audio sink is Bluetooth"
	    export J2M_AUDIO_SINK=$J2M_BLU_SINK
	else
		echo "Unable to switch audio sink"
	fi

else
	#switch from Bluetooth to USB

	# gets the pulseaudio index for USB device
	index=$(pacmd list-sinks | awk '{if ($1 == "index:") {i=$2; getline; if($0 ~ "usb") print i}}')
	echo "Attempting to switch from Bluetooth to USB sink"
	echo "index=$index"

	#check that the audio device index was found
	#and switch to USB if so
	if [ $index ]
	then
		$(pacmd set-default-sink $index)
		$(sudo systemctl restart mopidy)
		echo "Current audio sink is USB"
	    export J2M_AUDIO_SINK=$J2M_USB_SINK
	else
		echo "Unable to switch audio sink"
	fi
fi
