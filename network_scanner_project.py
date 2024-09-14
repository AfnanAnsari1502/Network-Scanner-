#Please note that the code contained here is not originally mine. This repository serves as a practice space for me to experiment with different coding techniques, understand various programming concepts, and refine my skills.
#The purpose of this project is to learn and grow as a developer, and I am using this code as a tool for personal development. If you have any feedback or suggestions for improvement, feel free to share them. Thank you for your understanding and support!


import argparse
import nmap

def argument_parser():
    """Allow user to specify target host and ports."""
    parser = argparse.ArgumentParser(description="TCP port scanner. Accepts a hostname/IP address and a list of ports to scan. Attempts to identify the service running on a port.")
    parser.add_argument("-o", "--host", required=True, help="Host IP address")
    parser.add_argument("-p", "--ports", required=True, help="Comma-separated port list, such as '25,80,8080'")

    return vars(parser.parse_args())

def nmap_scan(host_id, port_num):
    """Use nmap utility to check host ports for status."""
    nm_scan = nmap.PortScanner()
    nm_scan.scan(host_id, port_num)
    state = nm_scan[host_id]['tcp'][int(port_num)]['state']  # Indicate the type of scan and port number
    result = f"[*] {host_id} tcp/{port_num} {state}"

    return result

if __name__ == '__main__':
    try:
        user_args = argument_parser()
        host = user_args["host"]
        ports = user_args["ports"].split(",")  # Make a list from port numbers
        for port in ports:
            print(nmap_scan(host, port))
    except AttributeError:
        print("Error: Please provide the host and port numbers.")
