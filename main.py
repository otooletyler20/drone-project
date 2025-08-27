import socket
import time

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Tello IP and port
tello_address = ('192.168.10.1', 8889)

# Send a command to the drone
def send_command(command, delay=2):
    print(f"Sending: {command}")
    sock.sendto(command.encode('utf-8'), tello_address)
    time.sleep(delay)

# Main program
def main():
    try:
        # Enter SDK mode
        send_command("command", 4)

        # Take off
        send_command("takeoff", 4)

        # START
        send_command("up 2", 4) # TRAVERSING HOOPS
        send_command("forward 300", 4)
        send_command("up 45", 4)
        send_command("ccw 90", 4)
        send_command("forward 50", 4)
        send_command("ccw 90", 4)
        send_command("forward 30")
        send_command("flip f", 4) # FLIP
        send_command("cw 90", 4) # GOING TO TABLE
        send_command("forward 110", 4)
        send_command("cw 90", 4)
        send_command("down 40", 4)
        send_command("forward 265", 4)

        send_command("cw 90", 4) # AROUND THE TABLE
        send_command("forward 80", 4)
        send_command("cw 90", 4)
        send_command("forward 80", 4)
        send_command("cw 90", 4)
        send_command("forward 80", 4)
        send_command("cw 90", 4)

        send_command("forward 215", 4) # GO TO END
        send_command("cw 90", 4)
        send_command("forward 40", 4)

        # Land
        send_command("land", 4)

    except KeyboardInterrupt:
        print("Emergency landing...")
        send_command("land")

    finally:
        sock.close()

if __name__ == '__main__':
    main()
