import can
import sys


def node_id_parse(user_node):
    return {
        'broadcast': 0x00,

        'f_l_drive': 0x10,
        'f_r_drive': 0x11,
        'm_l_drive': 0x12,
        'm_r_drive': 0x13,
        'r_l_drive': 0x14,
        'r_r_drive': 0x15,

        'f_l_steer': 0x20,
        'f_r_steer': 0x21,
        'm_l_steer': 0x22,
        'm_r_steer': 0x23,
        'r_l_steer': 0x24,
        'r_r_steer': 0x25,  

        'f_l_walk': 0x30,
        'f_r_walk': 0x31,
        'm_l_walk': 0x32,
        'm_r_walk': 0x33,
        'r_l_walk': 0x34,
        'r_r_walk': 0x35
    }.get(user_node,None)


def msg_id_parse(user_msg):
    return {
        'emergency_stop': 0x0,
        'node_sync': 0x1,
        'set_get': 0x580,
    }.get(user_msg,None)


def set_get_msg_index_parse(user_index):
    return {
        'system_state_management': 0x0001,
        'num2': 2
    }.get(user_index,None)


def set_get_msg_sub_index_parse(user_index,user_sub_index):
    if user_index == 'system_state_management':
        return {
            'set_state_error': 0x00,
            'set_state_emergency_stop': 0x01,
            'set_state_initialise': 0x02,
            'set_state_pre_operational': 0x03,
            'set_state_operational': 0x04,
            'set_state_config': 0x05,
            'set_state_debug': 0x06,

            'get_current_state':0x10
        }.get(user_sub_index,None)
    
    elif user_index == 'second':
        return {
            'id_1': 0
        
        }.get(user_sub_index,None)


def init_bus():
    
    channel = sys.argv[1]

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
        print msg
        print ""
    except can.CanError:
        print ""
        print "Message Not sent"
        print ""


def cmd_msg_emulator(canbus):
    
    msg_header = 0x20

    user_node = 'ignore'
    node_id = 0
    
    user_msg = 'ignore'
    msg_id = 0

    user_cmd_msg_index = 0
    user_cmd_msg_sub_index = 0


    data = [0,0,0,0,0,0,0,0]

    while True:
    
        user_node = raw_input("node to send msg to: ")
        node_id = node_id_parse(user_node)

        if node_id != None:
            
            msg_id = None
            while user_msg != 'back':
                print "Executing command to node: ", user_node
            
                user_msg = raw_input("Select msg_id: ")
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
        
        
        
    


if __name__ == "__main__":
    
    cmd_msg_emulator(init_bus())