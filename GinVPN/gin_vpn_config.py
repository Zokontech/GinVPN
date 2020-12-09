#Alexander Krasny
import sys, os
import secrets
"""
prompts-array of 3 messages: initial prompt, out of range error, and invalid selection error
min and max-inclusive bounds of int input
default-string value of default int
prompts the use to input a number between min and max. If no entry, will default to the default, unless there is no default provided. Returns the value
"""
def get_valid_int_selection(prompts, min, max, default=''):
    while True:
        if default!='':
            print(prompts[0]+',', 'Leave Blank For', default)
        else:
            print(prompts[0])
        s=input()
        if s=='' and default!='':
            return default
        try:
            i=int(s)
            if(i in range(min, max)):
                return i
            else:
                print(prompts[1])
        except ValueError:
            print(prompts[2])

#prompts the user with a yes/no choice. Returns a bool,  yes returns true.
def yes_no():
    print("Save Settings?")
    a=input('y/n?')
    while True:
        if(a[0].lower()=='y'):
            return True
        elif(a[0].lower()=='n'):
            return False
        else:
            print("Please Enter Y or N")

"""
Creates a menu with the name ‘name’ and options from options list. Will ask user to select an option, 
and uses get_valid_input_selection() to get a choice integer to return.
"""
def menu_choice(name, options_list):
    print(name)
    for i in range(0, len(options_list)):
        print(str(i+1)+'. '+options_list[i])
    print()
    prompts=['Enter Valid Selection: ', 'Choice Out Of Range', 'Invalid Selection']
    return get_valid_int_selection(prompts, 1, len(options_list)+1)

"""
prompt- message to user about what to input
default- value to use if no values is provided
prompts user to input a string, and returns the value
"""
def get_string(prompt, default):
    print(prompt, 'Leave Blank for', default)
    server_adr = input()
    if server_adr!='':
        return server_adr
    else:
        return default
#returns a 32 byte key created using the python secrets module
def gen_key():
    print("Generating Key...")
    key=secrets.token_bytes(32) #random 32 byte string
    return key
#saves current options to a python file that acts as a module to import variables from for all programs
def save_key_svr_port(filename, key, server_adr,server_port):
    print("Saving Options")
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) #sets path to module location
    f = open(os.path.join(__location__, filename), 'w')
    f.write('key='+str(key)+'\n'+'server_adr='+'\''+server_adr+'\''+'\n'+'server_port='+str(server_port))
    f.close()

"""
Checks if GinSettings.py exists. This file contains the definitions of variables the programs use. 
If it doesn’t exit, it runs first time setup, which creates a new key and prompts 
the user to enter server information.
"""
def main():
    try:
        import GinSettings
        try:
            key=GinSettings.key
        except AttributeError:
            key="Vrz19NDnmgmqvJw0fm4R3Zadi7OLLVoA"
        try:
            server_adr=GinSettings.server_adr
        except AttributeError:
            server_adr='127.0.0.1'
        try:
            server_port=GinSettings.server_port
        except AttributeError:
            server_port=5000
    except ModuleNotFoundError: #occurs if GinSettings does not exist
        print('Running First Time Setup')
        key=gen_key()
        server_adr=get_string("Enter VPN Server Address,",'127.0.0.1')
        prompts=['Enter VPN Port Address', 'Invalid Port', 'Invalid Port']
        server_port = get_valid_int_selection(prompts, 1024, 65535,'5000')
        save_key_svr_port('GinSettings.py', key, server_adr,server_port)
        return
    menu_name='Config Options'
    menu_options=['Generate New Key', 'Change VPN Server', 'Change VPN Port', 'Save Changes and Quit', 'Quit Config']
    while True:
        i=menu_choice('\n'+menu_name, menu_options)
        if i==1:
            key=gen_key()
        if i==2:
            server_adr=get_string("Enter VPN Server Address,",server_adr)
        if i==3:
            prompts=['Enter VPN Port Address', 'Invalid Port', 'Invalid Port']
            server_port = get_valid_int_selection(prompts, 1024, 65535, server_port)
        if i==4:
            if yes_no():
                save_key_svr_port('GinSettings.py', key, server_adr,server_port)
                break
        if i==5:
            if yes_no():
                break

if __name__=='__main__':
    main()
