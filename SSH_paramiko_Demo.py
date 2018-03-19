#!python
# http://docs.paramiko.org/en/2.4/
# http://sebastiandahlgren.se/2012/10/11/using-paramiko-to-send-ssh-commands/

# to & execute commands on a remote host Unix device

# import requests
import paramiko
import time
import sys
import os

import sys
import SSH_login_demo


def send_text_2_file(ip, user_n, pass_w, in_text):
    SSH_remote = paramiko.SSHClient()
    SSH_remote
    SSH_remote.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # connect to device using SSH
        SSH_remote.connect(
            ip, username=user_n, password=pass_w, look_for_keys=False,
            allow_agent=False)
        # open a shell
        remote_conn = SSH_remote.invoke_shell()
        # get 10000 chars from remote
        output = remote_conn.recv(10000)
        print(output)
    except:
        time.sleep(1)
        pass
        # Send a  commnad
        remote_conn.send('rm test.txt\n')
        # wait
        time.sleep(1)
        # get 60000 chars from remote
        output = remote_conn.recv(60000)
        print(type(output))
        # Send a  commnad
        remote_conn.send("echo " + in_text + " >test.txt\n")
        # wait
        time.sleep(1)
        # get 60000 chars from remote
        output = remote_conn.recv(60000)
        print(type(output))
    SSH_remote.close()


def set_pi_date_time(ip, user_n, pass_w):
    SSH_remote = paramiko.SSHClient()
    SSH_remote
    SSH_remote.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # connect to device using SSH
        SSH_remote.connect(
            ip, username=user_n, password=pass_w, look_for_keys=False,
            allow_agent=False)
        # open a shell
        remote_conn = SSH_remote.invoke_shell()
        # get 10000 chars from remote
        output = remote_conn.recv(10000)
        print(output)
        # Send a  commnad
        remote_conn.send("date\n")
        # wait
        time.sleep(1)
        # get 60000 chars from remote
        output = remote_conn.recv(60000)
        # print(type(output))
        # out = output.decode("utf-8")
        # dt_str = out.split("date")[2]
        dt_str = output.decode("utf-8").split("date")[2][0:30]
        print(dt_str)
        d_date = dt_str[10:12].replace(' ', '0') + " " + dt_str[6:9].upper()
        + " " + dt_str[26:30] + " " + dt_str[13:21]
        print(dt_str)
        print(d_date)

        # uncomment break to set local time ona Raspberry Pi or unix device
        # break

        # unix
        # os.system('sudo date -set="2 OCT 2006 18:00:00"')
        # os.system('date -s ' + d_date)
        # set system date time
        os.system('sudo date --set="' + dt_str + '"')
    except:
        time.sleep(1)
        pass

    SSH_remote.close()

if __name__ == '__main__':
    # Update ip, username and password for your device
    send_text_2_file(
        SSH_login_demo.my_ip, SSH_login_demo.my_user_id,
        SSH_login_demo.my_password,
        "Hello World!")
    set_pi_date_time(
        SSH_login_demo.my_ip, SSH_login_demo.my_user_id,
        SSH_login_demo.my_password)
