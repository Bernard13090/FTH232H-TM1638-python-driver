
tm = TM1638()

tm.clear()

tm.start_transmission()
tm._command((0x8f))
tm.end_transmission()

tm.start_transmission()
tm._command(TM1638_CMD | 0x04)
tm.end_transmission()

key = tm.keys()
print(binary(key))

tm.show("B.Autran")

while True:
    
    key = tm.keys()
    sleep_µs(800)
    for i in range (1,16,2):
        #print(i,end=" shift ")
        shift = int((i-1)/2)
    
        #print(shift,end=" avec ")
        #print(binary((key >> shift)  & 1))
        x = True if (key >> shift & 1) else False # LED on if state is true, false otherwise
        tm.start_transmission()
        if x:
            tm._command(TM1638_ADDR | (i))
            tm._byte(0b00000001)
        else :
            tm._command(TM1638_ADDR | (i))
            tm._byte(0b00000000)
        tm.end_transmission() 

