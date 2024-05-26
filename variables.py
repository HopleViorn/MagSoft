import numpy as np

mm_per_pix=1
rgb_mt=[]

base_img=np.zeros((1,1))

# rgb_lut=[i for i in range(256)]
mag_lut=np.array([i for i in range(256)])

def update_mag_lut():
    rgb_mt.sort(key=lambda x:x.avg)

    j=0
    l=len(rgb_mt)
    print('\n')
    for i in range(256):
        if j<l-1 and rgb_mt[j+1].avg <= i:
            j+=1
        x0,x1=rgb_mt[j].avg,rgb_mt[j+1].avg
        y0,y1=rgb_mt[j].md,rgb_mt[j+1].md

        point=(i-x0)*(y1-y0)/(x1-x0)+y0
        mag_lut[i]=point
    
