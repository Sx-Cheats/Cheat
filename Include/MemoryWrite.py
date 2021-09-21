import os.path
from  ctypes  import *

PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_OPERATION = 0x0008
PROCESS_VM_READ = 0x0010
PROCESS_VM_WRITE = 0x0020
MAX_PATH = 260

class ReadWriteMemoryError(Exception):
    pass
class Process(object):
    def __init__(self, name = '', pid = -1, handle = -1):
        self.name = name
        self.pid = pid
        self.handle = handle
        self.ReadProcessMemory = windll.kernel32.ReadProcessMemory
        self.WriteProcessMemory = windll.kernel32.WriteProcessMemory
    def __repr__(self) :
        return f'{self.__class__.__name__}: "{self.name}"'
    def FLOAT_TO_DEC(self,f: float) -> int:
         return c_int32.from_buffer(c_float(f)).value
    def DEC_TO_FLOAT(self,d:int) -> float:
         return c_float.from_buffer(c_uint32(d)).value
    def open(self):
        dw_desired_access = (PROCESS_QUERY_INFORMATION | PROCESS_VM_OPERATION | PROCESS_VM_READ | PROCESS_VM_WRITE)
        b_inherit_handle = False
        self.handle = windll.kernel32.OpenProcess(dw_desired_access, b_inherit_handle, self.pid)
        if not self.handle:
            raise ReadWriteMemoryError(f'Unable to open process <{self.name}>')

    def get_pointer(self, lp_base_address: hex, offsets = []) :
        temp_address = self.read(lp_base_address)
        pointer = 0x0
        if not offsets:
            return temp_address
        else:
            for offset in offsets:
                pointer = int(str(temp_address), 0) + int(str(offset), 0)
                temp_address = self.read(pointer)
            return pointer
    def read(self, lp_base_address):
        try:
            read_buffer = c_uint32(0)
            lp_buffer = byref(read_buffer)
            n_size = sizeof(read_buffer)
            lp_number_of_bytes_read = c_ulong(0)
            self.ReadProcessMemory(self.handle, lp_base_address, lp_buffer,n_size, lp_number_of_bytes_read)
            return read_buffer.value
        except (BufferError, ValueError, TypeError) as error:
            if self.handle:
                self.close()
            error = {'msg': str(error), 'Handle': self.handle, 'PID': self.pid,
                     'Name': self.name}
            ReadWriteMemoryError(error)
    def write(self, lp_base_address, value) :
        try:
            write_buffer = c_uint(value)
            lp_buffer = byref(write_buffer)
            n_size = sizeof(write_buffer)
            lp_number_of_bytes_written = c_ulong(0)
            self.WriteProcessMemory(self.handle, lp_base_address, lp_buffer,n_size, lp_number_of_bytes_written)
            return True
        except (BufferError, ValueError, TypeError) as error:
            if self.handle:
                self.close()
            error = {'msg': str(error), 'Handle': self.handle, 'PID': self.pid,
                     'Name': self.name}
            ReadWriteMemoryError(error)
            
class ReadWriteMemory:
    def __init__(self):
        self.handle = None
        self.process = Process()
    def get_process_by_name(self, NAME):
        self.process.pid    = eval(__import__("subprocess").getoutput(f"powershell -Command (Get-Process -ProcessName {NAME}).Id"))
        self.process.handle = windll.kernel32.OpenProcess(PROCESS_QUERY_INFORMATION, False, self.process.pid)
        self.process.name = NAME +".exe"    
        return self.process
