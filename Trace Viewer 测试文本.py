# from obspy import read
import obspy
import matplotlib.pyplot as plt
import pylab

#importing segy file fromm file

data = obspy.read(r"D:\\Program Files\\Python313\\Lib\site-packages\\obspy\\io\segy\tests\data\planes.segy_first_trace", format="SEGY")
print(data)
st = data[0:25]
meta = str(st[0])

#Grab the number of traces per shot by analysing the date and times of first group of traces.

timelist = []
for i in range(len(st)):
    td = str(st[i])
    timedate = td[25:44]
    timelist.append(timedate)
 
t = str(st[0])[25:44]
tracespershot = timelist.count(t)


#User select shot number from segy dataset

print ("Input shot number between 1 and " + str((len(data))/tracespershot) + "...")
shotselect =1
shotend = shotselect * tracespershot
shotstart = (shotselect) - 1 * tracespershot
st = data[shotstart:shotend]

#User select components from segy dataset
print ("\n" + "Select component....")
print ("1. VZ")
print ("2. HX")
print ("3. HY")
twig = (int(input()))-1

#User select zoom start  & end points
print( "\n" + "Choose zoom start point (0 for default)....")
zoomstart = int(input())
print ("\n" + "Choose zoom end point (0 for default)....")
zend = int(input())
if zend == 0:
 zoommend = len (data)
elif zend > 0:
    zoomend = zend

#Pulling out the meta data for selected shot


print ("\n"+ "----------------------------------------META DATA--------------------------------------------" + "\n")
print ("Shot Number: " + str(shotselect))
print ("Date: " + meta[25:35])
print ("Time: " + meta[36:44])
if twig == 0:
    print ("Component: VZ")
elif twig == 1:
    print ("Component: HX")
elif twig == 2:
    print ("Component: HY")
print ("Sample Rate: " + str(float(meta[85:89])) + " Hz")
print ( "Sample Interval:  83.3 ms")
print ( "Number of Samples: " + meta[96:100])
print( "Record Length: " + str(1000*(float(meta[85:89]))/12) + " ms")
print( "Number of traces in selected shot: " + str(len(st)))
print( "Number of traces entire dataset: " + str(len(data)))

print( "\n" + "---------------------------------------SHOT #" + str(shotselect) + " -------------------------------------------" + "\n")


#plot Time break and surface geo, then every 5th trace. the VZ/HX/HY channel from 5 tools.

count = 2
subplot = 2

for i in range(len(st)):
    if i % 5 == 0:
        count += 1    

plt.figure(1)

plt.subplot(111)
plt.plot(st[0])
    




for i in range(len(st)):

    if i % 5 == 0:   
        tr = st[i + twig][zoomstart:zoommend]
    
         
        plt.subplot(111)
        plt.plot(tr, color = '0.4')

plt.show()
