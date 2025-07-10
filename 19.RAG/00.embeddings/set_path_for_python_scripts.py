import os
import sys
import winreg

# The directory to add
scripts_dir = r"C:\Users\Omar Essam2\AppData\Roaming\Python\Python313\Scripts"

# Get current user PATH
with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Environment', 0, winreg.KEY_READ) as key:
    try:
        user_path, _ = winreg.QueryValueEx(key, 'PATH')
    except FileNotFoundError:
        user_path = ''

if scripts_dir in user_path:
    print(f"'{scripts_dir}' is already in your user PATH.")
    sys.exit(0)

# Add to user PATH
new_path = user_path + (";" if user_path and not user_path.endswith(";") else "") + scripts_dir
with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Environment', 0, winreg.KEY_SET_VALUE) as key:
    winreg.SetValueEx(key, 'PATH', 0, winreg.REG_EXPAND_SZ, new_path)

print(f"Added '{scripts_dir}' to your user PATH.")
print("Please restart your terminal or log out and log in again for the changes to take effect.") 