import tkinter as tk
import bluetooth

class BluetoothFileTransferGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Bluetooth File Transfer")
        
        # Set the name of the file to send
        self.filename = "example.txt"
        
        # Get the available Bluetooth devices
        self.devices = bluetooth.discover_devices()
        
        # Create a listbox to display the devices
        self.device_listbox = tk.Listbox(self.master, height=len(self.devices))
        self.device_listbox.pack(fill=tk.BOTH, expand=True)
        for device in self.devices:
            self.device_listbox.insert(tk.END, device)
        
        # Create a button to send the file to the selected device
        self.send_button = tk.Button(self.master, text="Send File", command=self.send_file)
        self.send_button.pack()
    
    def send_file(self):
        # Get the selected device address
        selection = self.device_listbox.curselection()
        if not selection:
            return
        device_address = self.devices[selection[0]]
        
        # Create a Bluetooth socket
        socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        
        # Connect to the device
        socket.connect((device_address, 1))
        
        # Send the file
        with open(self.filename, "rb") as f:
            data = f.read()
            socket.send(data)
        
        # Close the socket
        socket.close()

root = tk.Tk()
app = BluetoothFileTransferGUI(root)
root.mainloop()
