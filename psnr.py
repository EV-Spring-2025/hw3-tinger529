import cv2
import os
import numpy as np
from skimage.metrics import peak_signal_noise_ratio as compute_psnr

# Set your paths
generated_dir = "PhysGaussian/output"
reference_dir = "PhysGaussian/plastic_gt"  # <-- replace with actual path

frame_range = range(124)  # total frames rendered

psnr_list = []

for frame in frame_range:
    fname = f"{frame:04d}.png"
    print(f"Processing frame: {fname}")
    try:
        rendered = cv2.imread(os.path.join(generated_dir, fname))
        ground_truth = cv2.imread(os.path.join(reference_dir, fname))
    except Exception as e:
        print(f"Error reading files for frame {frame}: {e}")
        continue

    if rendered is None or ground_truth is None:
        print(f"Warning: Missing file {fname}")
        continue

    rendered = cv2.resize(rendered, (ground_truth.shape[1], ground_truth.shape[0]))
    psnr = compute_psnr(ground_truth, rendered, data_range=255)
    psnr_list.append(psnr)

print(f"Average PSNR over {len(psnr_list)} frames: {np.mean(psnr_list):.2f} dB")
