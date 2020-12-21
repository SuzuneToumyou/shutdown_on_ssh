#!/usr/bin/python3
# coding: utf-8

import paramiko
import sys
import time

def send_string_and_wait(shell, command, wait_time, should_print):
      
      shell.send(command)
      time.sleep(wait_time)
      receive_buffer = shell.recv(1024)
      if should_print:
        return  receive_buffer

def shutdown_on_ssh(host,owner,passwd,reboot_flag):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(str(host), username=str(owner),  password=str(passwd), port=22)
    shell = client.invoke_shell()
    if reboot_flag == 1:
        send_string_and_wait(shell, "sudo -k reboot\n", 1, True)
    else:
        send_string_and_wait(shell, "sudo -k halt -p\n", 1, True)
    send_string_and_wait(shell, str(passwd) + "\n", 1, True)
    client.close()
    
if __name__ == "__main__":
    shutdown_on_ssh('192.168.0.1', 'user', 'passwd', 1)
