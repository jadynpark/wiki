from nilearn import plotting, datasets

# Interactive plot
# fsaverage = datasets.fetch_surf_fsaverage()

# MNI coordinate of the ROI
# coords = [(14, 64, 2)]
# fig = plotting.view_markers(
#    coords,
#    marker_color=['red'],
#    marker_size=20
#)
# fig.save_as_html('brain_with_marker.html')

# Pretty plot
from nilearn import plotting, datasets, surface
import nibabel as nib
import numpy as np

fsaverage = datasets.fetch_surf_fsaverage()

# Create a small sphere at MNI coordinate
# Code for transformation & hardcoded numbers generated via ChatGPT
coords = [(14, 64, 2)]

# From MNI to voxel location
affine = np.diag([2, 2, 2, 1])
affine[:3, 3] = [-90, -126, -72] # At voxel (0, 0, 0)
shape = (91, 109, 91)
data = np.zeros(shape)
vox = np.linalg.solve(affine, [*coords[0], 1])[:3].astype(int)

# Create blob around that voxel
data[vox[0]-3:vox[0]+3, vox[1]-3:vox[1]+3, vox[2]-3:vox[2]+3] = 5.0
marker_img = nib.Nifti1Image(data, affine)

# Project the marker volume onto the surface
texture = surface.vol_to_surf(marker_img, fsaverage['pial_right'])

plotting.plot_surf(
    surf_mesh=fsaverage['pial_right'],
    surf_map=texture,
    view='medial',
    hemi='right',
    bg_map=fsaverage['sulc_right'],
    bg_on_data=True,
    title='Medial View',
    cmap='Oranges',        
    threshold=0.1,     
    vmax=5,
)
plotting.show()