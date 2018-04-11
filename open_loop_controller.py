import can
import time
import sys
import numpy as np


def node_id_parse(user_node):
    return {
        'fld': 0x001,
        'frd': 0x002,
        'mld': 0x003,
        'mrd': 0x004,
        'rld': 0x005,
        'rrd': 0x006

        # 'f_l_steer': 0x20,
        # 'f_r_steer': 0x21,
        # 'm_l_steer': 0x22,
        # 'm_r_steer': 0x23,
        # 'r_l_steer': 0x24,
        # 'r_r_steer': 0x25,  

        # 'f_l_walk': 0x30,
        # 'f_r_walk': 0x31,
        # 'm_l_walk': 0x32,
        # 'm_r_walk': 0x33,
        # 'r_l_walk': 0x34,
        # 'r_r_walk': 0x35
    }.get(user_node,None)


def msg_id_parse(user_msg):
    return {
        'rpdo6': 0x180
        # 'node_sync': 0x1,
        # 'set_get': 0x580,
    }.get(user_msg,None)


def controlword_parse(user_cword):
    return {
        'en_op': 0x000f,
        'dis_op': 0x0007
    }.get(user_cword,None)


def vl_target_parse(user_vel):
    target_vel = int(user_vel*32767)
    # print "Target Velocity(int16): ", target_vel


    return target_vel


def init_bus():
    
    channel = sys.argv[3]

    try:
        print "Attempting connection to: ", channel
        bus = can.interface.Bus(bustype='socketcan',channel=channel)
        print "Connected to: ", channel

        return bus
    
    except:
        print "Connection attempt to ", channel, " failed"

        sys.exit("Socketcan Interface Connection Attemped Failed - Exiting")


def send_data(canbus,cmd_msg_id,cmd_msg_data):
    
    msg = can.Message(  arbitration_id = cmd_msg_id,
                        data = cmd_msg_data,
                        extended_id=False          )
                        
    try:
        canbus.send(msg)
        print ""
        print "CAN Message: ", msg
        print ""
    except can.CanError:
        print ""
        print "Message Not sent"
        print ""


def user_dsp_402_emulator(canbus):

    user_node = None
    user_msg = None
    user_cword = None
    user_vel = None

    msg_id = None

    print "Open Loop Controller Emulator - User Input"

    while True:
    
        user_node = raw_input("Send message to Node with name: ")
        node_id = node_id_parse(user_node)

        if node_id != None:
    
            

            while user_msg != '/b':
                print "Select Command (Enter /b to go back): ", user_node
            
                user_msg = raw_input(": ")
                msg_id = msg_id_parse(user_msg)

                if msg_id != None and user_msg != 'back':
                    
                    if user_msg == 'emergency_stop' and user_node == 'broadcast':
                        # emergency_stop command

                        print ""
                        print "Selection: node_id = ", hex(node_id), "msg_id = ", hex(msg_id), "message_header_t = ", hex(msg_header)
                        print "message_data_t = ", data
                        print ""
                        # send_data(canbus,msg_header,data)

                    if user_msg == 'node_sync' and user_node == 'broadcast':
                        
                        # node_sync broadcast command

                        print ""
                        print "Selection: node_id = ", hex(node_id), "msg_id = ", hex(msg_id), "message_header_t = ", hex(msg_header)
                        print "message_data_t = ", data
                        print ""
                        # send_data(canbus,msg_header,data)
                        

                    elif user_msg == 'set_get':
                        print "'set_get_command' selected to node: ", user_node
                        
                        while user_cmd_msg_index != 'back':
                            user_cmd_msg_index = raw_input("index to send: ")
                            msg_index = set_get_msg_index_parse(user_cmd_msg_index)

                            if msg_index != None:
                                user_cmd_msg_sub_index = raw_input("sub-index to send: ")
                                msg_sub_index = set_get_msg_sub_index_parse(user_cmd_msg_index,user_cmd_msg_sub_index)

                                if msg_sub_index != None:
                                    
                                    if 'set_' in user_cmd_msg_sub_index:
                                        print "set"
                                        set_get_flag = 1

                                    elif 'get_' in user_cmd_msg_sub_index:
                                        print "get"
                                        set_get_flag = 2

                                    msg_header = msg_id + node_id
                                    data[0] = set_get_flag
                                    data[1] = (msg_index >> 8) & 0xff
                                    data[2] = msg_index & 0xff
                                    data[3] = msg_sub_index


                                    # add specifics for index
                                    print ""
                                    print "Selection: node_id = ", hex(node_id), "msg_id = ", hex(msg_id), "message_header_t = ", hex(msg_header)
                                    print "message_data_t = ", data
                                    print ""
                                    send_data(canbus,msg_header,data)

                                else:
                                    print ""
                                    print "Selection invalid"
                                    print ""
                        
                            elif user_cmd_msg_index == 'back':
                                print ""
                                print 'going back to select new msg_id'
                                print ""
                                print ""


                            else:
                                print "msg_index invalid"
                    
                    elif msg_id == 'emergency_stop' and node_id != 'broadcast':
                        print "Combination invalid: Use 'broadcast' to send out 'emergency_stop' command"


                elif user_msg == 'back':
                    print ""
                    print "Going back to select new node_id"
                    print ""
                else:
                    print "msg_id invalid"
                    print ""

        else:
            print "node_id invalid"




def drive(canbus, node_id, target_velocity):

    msg_data = [0,0,0,0,0,0,0,0]

    print "Command node to DRIVE"

    msg_header = msg_id_parse('rpdo6') + node_id
    controlword = controlword_parse('en_op')
    target_velocity_vl = vl_target_parse(target_velocity);
    
    print "Node being commanded: ", hex(node_id) 
    print "RPDO_6 Message:\r\n\tcontrolword = ", hex(controlword), "\r\n\ttarget_velocity_vl (hex) = ", hex(target_velocity_vl)

    msg_data[0] = (controlword >> 8) & 0xff
    msg_data[1] = (controlword & 0xff)
    msg_data[2] = (target_velocity_vl >> 8) & 0xff
    msg_data[3] = (target_velocity_vl & 0xff)

    send_data(canbus, msg_header, msg_data)



def stop(canbus, node_id):

    msg_data = [0,0,0,0,0,0,0,0]

    target_velocity = 0

    print "Command Node to STOP"
    
    msg_header = msg_id_parse('rpdo6') + node_id
    controlword = controlword_parse('dis_op')
    target_velocity_vl = vl_target_parse(target_velocity);
    
    print "Node being commanded: ", hex(node_id) 
    print "RPDO_6 Message:\r\n\tcontrolword = ", hex(controlword), "\r\n\ttarget_velocity (float) = ", target_velocity, "\r\n\ttarget_velocity_vl (int16) = ", target_velocity_vl, "\r\n\ttarget_velocity_vl (hex) = ", hex(target_velocity_vl)

    msg_data[0] = (controlword >> 8) & 0xff
    msg_data[1] = (controlword & 0xff)
    msg_data[2] = (target_velocity_vl >> 8) & 0xff
    msg_data[3] = (target_velocity_vl & 0xff)

    send_data(canbus, msg_header, msg_data)




def run_node_drive_stop(canbus):
    
    node_id = 'frd'
    while 1:
        drive(canbus, node_id_parse('fld'), 0.75)
        drive(canbus, node_id_parse('frd'), 0.75)
        drive(canbus, node_id_parse('mld'), 0.75)
        time.sleep(5)
        stop(canbus, node_id_parse('fld'))
        stop(canbus, node_id_parse('frd'))
        stop(canbus, node_id_parse('mld'))
        time.sleep(5)





def system_start():
    if sys.argv[1] == 'user':
        print "Manual Mode Selected"  
        user_dsp_402_emulator(init_bus())


    elif sys.argv[1] == 'auto':
        print "Auto Mode - Executing Predefined Script"

        if sys.argv[2] == '1':
            run_node_drive_stop(init_bus())


    else:
        print "Incorrect inputs - select mode as manual' or 'auto' "
        print "\tFor Auto mode, please run: python open_loop_controller.py auto <x> slcan0"
        print "\tFor User mode, please run: python open_loop_controller.py user slcan0"
        sys.exit
        
    


if __name__ == "__main__":
    system_start()
    