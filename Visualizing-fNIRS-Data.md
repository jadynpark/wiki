This page contains info for visualizing fNIRS data.  

## Things to check:  
1. Check the `digpts.txt` file in your data directory. It'll look something like this:  

<p align="center">
<img src="https://github.com/jadynpark/wiki/tree/main/imgs/fNIRS_viz_digpts.png" width="400">
</p>

`nz`, `ar`, `al`, `dz`, `iz` refer to the anatomical landmarks (typically found in the first 5 rows of your digpts.txt file) that we will use as reference points. The coordinates in the .txt file are in the device's native space, and we'll eventually have to convert these to MNI coordinates (more on this below). The rows below them (`s1`, `s2`, ...) correspond to the coordinates of your sources and detectors, also in the device's native space.  

2. Make sure you have the helper function `getMNIcoords.m`  

This is a function that transforms the native coordinates into MNI space. It takes in 2 files: (1) the `digpts.txt` file, for detecting the coordinates in the native space, (2) the SD file, for detecting the number of sources and detectors. The SD file is zipped in the subject's .snirf file. It spits out a table of MNI coordinates (`mni_ch_table`), where each row corresponds to the channel number.   

### About `getMNIcoords.m`:  

There are several versions of this script, and it's possible that the one you have is an outdated one.  

For posterity, the old (original) version of the script `getMNIcoords.m` can be found [here](https://github.com/jadynpark/wiki/tree/main/code/getMNIcoords.m)  
The updated version of the script `getMNIcoords_v2.m` can be found [here](https://github.com/jadynpark/wiki/tree/main/code/getMNIcoords_v2.m). 

**Read below and update yours accordingly**  

The function uses MNI coordinates of anatomical landmarks to compute a transformation matrix that converts the coordinates from native space to MNI space. These landmarks are used as reference points for the transformation.  As of now, there is a lot of hard coding involved, so be cautious when using it. There are several things to look out for:  

(1) The MNI coordinates of the landmarks are hard-coded in the script.  

<p align="center">
<img src="https://github.com/jadynpark/wiki/tree/main/imgs/fNIRS_viz_MNIcoords.png" width="600">
</p>

These coordinates are from Dr. Shannon Burns, who also took it from a probablistic conversion atlas. These coordinates can be found [here](https://github.com/jadynpark/wiki/tree/main/code/AP1005_anterior.xlsx).  

(2) The script assumes that the rows of the `digpts.txt` file are sorted in a particular way. Typically, you will find that the first 5 rows correspond to the landmarks, followed by sources and detectors. If your `digpts.txt` file is sorted differently, you'll need to update the script. In particular:  

<p align="center">
<img src="https://github.com/jadynpark/wiki/tree/main/imgs/fNIRS_viz_ref.png" width="600">
</p>

<p align="center">
<img src="https://github.com/jadynpark/wiki/tree/main/imgs/fNIRS_viz_SD.png" width="600">
</p>

(3) An example of MNI coordinates from a 20-channel prefrontal montage (8 sources, 7 detectors). .mat file found [here](https://github.com/jadynpark/wiki/tree/main/code/MNI_coord.mat)

<p align="center">
<img src="https://github.com/jadynpark/wiki/tree/main/imgs/fNIRS_viz_tbl.png" width="250">
</p>

## Visualizing ROIs on the brain:  

[Here](https://github.com/jadynpark/wiki/tree/main/code/create_brain_fig.py) is a custom script for visualizing ROIs on the brain using nilearn. Again, the ROI coordinates are hard-coded so be cautious. 




