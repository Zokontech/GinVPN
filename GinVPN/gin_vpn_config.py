import sys, os
from pyautogui import typewrite
import secrets


def get_valid_int_selection(prompts, min, max, default=''):
    while True:
        if default!='':
            typewrite(str(default))
        s=input(prompts[0])
        try:
            i=int(s)
            if(i in range(min, max)):
                return i
            else:
                print(prompts[1])
        except ValueError:
            print(prompts[2])

def yes_no():
    a=input('y/n?')
    while True:
        if(a[0].lower()=='y'):
            return True
        elif(a[0].lower()=='n'):
            return False
        else:
            print("Please Enter Y or N")

def menu_choice(name, options_list):
    print(name)
    for i in range(0, len(options_list)):
        print(str(i+1)+'. '+options_list[i])
    print()
    prompts=['Enter Valid Selection: ', 'Choice Out Of Range', 'Invalid Selection']
    return get_valid_int_selection(prompts, 1, len(options_list)+1)
    
def get_string(prompt, default):
    print(prompt)
    typewrite(default)
    server_adr = input()
    return server_adr

def gen_key():
    print("Generating Key...")
    key=secrets.token_bytes(32)
    return key

def save_key_svr_port(filename, key, server_adr,server_port):
    print("Saving Options")
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open(os.path.join(__location__, filename), 'w')
    f.write('key='+str(key)+'\n'+'server_adr='+'\''+server_adr+'\''+'\n'+'server_port='+str(server_port))
    f.close()

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
    except ModuleNotFoundError:
        print('Running First Time Setup')
        key=gen_key()
        server_adr=get_string("Enter VPN Server Address: ",'127.0.0.1')
        prompts=['Enter VPN Port Address: ', 'Invalid Port', 'Invalid Port']
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
            server_adr=get_string("Enter VPN Server Address: ",server_adr)
        if i==3:
            prompts=['Enter VPN Port Address: ', 'Invalid Port', 'Invalid Port']
            server_port = get_valid_int_selection(prompts, 1024, 65535)
        if i==4:
            if yes_no():
                save_key_svr_port('GinSettings.py', key, server_adr,server_port)
                break
        if i==5:
            if yes_no():
                break

if __name__=='__main__':
    main()
