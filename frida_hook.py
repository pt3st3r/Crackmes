import frida
import os
import sys,time
import argparse
script = ""
def on_message(message, data):
    global index, filename
    if message['type'] == 'send':
        print("recv payload" + message['payload'])
        new_data = input("insert new data=")
        script.post({"type": "send","data":new_data})
    else:
        print(message)


if __name__ == '__main__':
    try:
        package = "vn.com.seabank.mb1"
        print('[*] Spawning ' + package)
        frd = frida.get_usb_device()
        print(frd)
        pid = frd.spawn(package)
        session = frd.attach(pid)
        hook = open("cert_bypass.js", 'r')
        script = session.create_script(hook.read())
        script.on("message",on_message)
        script.load()

        frd.resume(pid)

        print('')
        sys.stdin.read()

    except KeyboardInterrupt:
        sys.exit(0)
