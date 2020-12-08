import components.audio.audio_main as mysp
import pickle
import os

local_path = os.getcwd()
p = "audio_wav2"
#p="Walkers" *Audio file name
#c=r"C:\Users\.......YOUR_NAME........\Desktop\myprosody" *an example of path to directory "myprosody" 
c = os.path.join( str(local_path),"components","audio","myprosody")
print(p)
print(c)

# p : path to dataset folder
#m : path to file
#m, p

mysp.mysptotal(p,c)
mysp.myspgend(p,c)
mysp.myspsyl(p,c)
mysp.mysppaus(p,c)
mysp.myspsr(p,c)
mysp.myspatc(p,c)
mysp.myspst(p,c)
mysp.myspod(p,c)
mysp.myspbala(p,c)
mysp.myspf0mean(p,c)
mysp.myspf0sd(p,c)
mysp.myspf0med(p,c)
mysp.myspf0min(p,c)
mysp.myspf0max(p,c)
mysp.myspf0q25(p,c)
mysp.myspf0q75(p,c)
mysp.mysppron(p,c)
mysp.myprosody(p,c)
mysp.mysplev(p,c)
