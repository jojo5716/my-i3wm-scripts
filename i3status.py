from i3pystatus import Status

status = Status()

status.register("battery",
    format="{status} {percentage:.2f}% {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=10,
    status={
        "DIS": "↓",
        "CHR": "↑",
        "FULL": "FULL",
    },)

status.register("network",
    interface="wlp2s0",
    format_up="IP: {v4cidr}",)
    
status.register("network",
    interface="wlan0",
    format_up="{essid} {quality:03.0f}%",)

status.register("disk",
    path="/",
    format="{used}/{total}G [{avail}G]",)

status.register("pulseaudio",
    format="♪ {volume}",     
    on_upscroll = "decrease_volume",
    on_downscroll = "increase_volume",
)

status.run()
