import idaapi
import idautils

def ascii_to_hex(string):
  t1=list(string)
  t2=''
  for i in t1: 
    t3=re.sub('0x','',str(hex(ord(i))))
    t3=t3.zfill(2)
    t2+=t3

  t2=re.sub('0x','',t2)
  return t2

def save_disasm_functions_ida():
  funcDisassList = {}
  flag= 0

  for segAddress in Segments():
    segName = SegName(segAddress)
    if segName == ".text":
      funcs = Functions(SegStart(segAddress), SegEnd(segAddress))
      for address in funcs:
        t1= GetFunctionName(address)
        f1= idautils.FuncItems(address)
        t2=''
        for i in f1:
          t2+= GetDisasm(i).split(';')[0]
          t2+= '^^^'
        funcDisassList[t1]= t2
        
  return funcDisassList

def write_to_file(funcDisassList):        
  #Write results to output file
  output_dir="C:\data\output\\"
  output_filename=str(idc.GetInputFile())+'.txt'
  with open(output_dir+output_filename,'w') as f:
    for key, value in funcDisassList.iteritems():
      f.write(key)
      f.write('$$$')
      f.write(value)
      f.write("\n")

#Wait for analysis to complete
idaapi.autoWait()

#Save disassembly of binary to a file
funcDisassList= save_disasm_functions_ida()
write_to_file(funcDisassList)

idc.Exit(0)
