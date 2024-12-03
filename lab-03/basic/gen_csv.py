import struct
import os
import pandas as pd

# def ReadFile(filepath):
#     binfile = open(filepath, 'rb') 
#     size = os.path.getsize(filepath) 
#     for i in range(size//16):
#         data1 = binfile.read(8) 
#         data2 = binfile.read(8) 
#         print(f"{data1.hex()} {data2.hex()}")
#     binfile.close()
def Analyze(filepath):
    data = []
    base = 0x180c2000 #change it
    binfile = open(filepath, 'rb') 
    size = os.path.getsize(filepath) 
    offset = 0
    next_pre = 0
    fdbk = False
    for i in range(size//16):
        data1 = binfile.read(8) 
        data2 = binfile.read(8) 
        offset += 16
        if next_pre < offset: 
            print(f"{hex(offset-16)} {data1.hex()} {data2.hex()} \tprev_size: {hex(int.from_bytes(data1, byteorder='little', signed=True))}\tsize = {hex(int.from_bytes(data2, byteorder='little', signed=True)-1)}")
            next_pre += int.from_bytes(data2, byteorder='little', signed=True)-1
            data.append((hex(offset-16+base), hex(offset-16), hex(int.from_bytes(data1, byteorder='little', signed=True)), hex(int.from_bytes(data2, byteorder='little', signed=True)), f"prev_size: {hex(int.from_bytes(data1, byteorder='little', signed=True))} size: {hex(int.from_bytes(data2, byteorder='little', signed=True)-1)}"))
            fdbk = True
        elif(fdbk and offset>0x290):
            print(f"{hex(offset-16)} {data1.hex()} {data2.hex()} \tfb: {hex(int.from_bytes(data1, byteorder='little', signed=True))}\tbk: {hex(int.from_bytes(data2, byteorder='little', signed=True))}")
            fdbk = False
            data.append((hex(offset-16+base), hex(offset-16), hex(int.from_bytes(data1, byteorder='little', signed=True)), hex(int.from_bytes(data2, byteorder='little', signed=True)), f"fb: {hex(int.from_bytes(data1, byteorder='little', signed=True))} bk: {hex(int.from_bytes(data2, byteorder='little', signed=True))}"))
        else:
            print(f"{hex(offset-16)} {data1.hex()} {data2.hex()}")
            data.append((hex(offset-16+base), hex(offset-16), hex(int.from_bytes(data1, byteorder='little', signed=True)), hex(int.from_bytes(data2, byteorder='little', signed=True)), " "))
    df_output = pd.DataFrame(data, columns=['addr', 'offset', 'data1', 'data2', 'info'])
    output_path = './heap_parse.csv'
    df_output.to_csv(output_path, index=False)
    binfile.close()

Analyze("dump_1893e000_0.bin")