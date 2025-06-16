[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SdXSjEmH)
# EV-HW3: PhysGaussian

This homework is based on the recent CVPR 2024 paper [PhysGaussian](https://github.com/XPandora/PhysGaussian/tree/main), which introduces a novel framework that integrates physical constraints into 3D Gaussian representations for modeling generative dynamics.

You are **not required** to implement training from scratch. Instead, your task is to set up the environment as specified in the official repository and run the simulation scripts to observe and analyze the results.


## Getting the Code from the Official PhysGaussian GitHub Repository
Download the official codebase using the following command:
```
git clone https://github.com/XPandora/PhysGaussian.git
```


## Environment Setup
Navigate to the "PhysGaussian" directory and follow the instructions under the "Python Environment" section in the official README to set up the environment.


## Running the Simulation
Follow the "Quick Start" section and execute the simulation scripts as instructed. Make sure to verify your outputs and understand the role of physics constraints in the generated dynamics.


## Homework Instructions
Please complete Part 1–2 as described in the [Google Slides](https://docs.google.com/presentation/d/13JcQC12pI8Wb9ZuaVV400HVZr9eUeZvf7gB7Le8FRV4/edit?usp=sharing).


# Reference
```bibtex
@inproceedings{xie2024physgaussian,
    title     = {Physgaussian: Physics-integrated 3d gaussians for generative dynamics},
    author    = {Xie, Tianyi and Zong, Zeshun and Qiu, Yuxing and Li, Xuan and Feng, Yutao and Yang, Yin and Jiang, Chenfanfu},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    year      = {2024}
}
```

***

# Report

## Part 1 Video

Please check part1/ directory.

## Part 2

**PSNR**

| Adjustment | PSNR (dB) |
| ---------- | ---- |
| grid_v_damping_scale 0.9999 -> 1.9999| 20.01 |
| substep_dt 1e-4 -> 6e-5 | 22.61 |
| n_grid 100 -> 10 | 21.73 |
| softening 0.1 -> 100 | 76.51 |

**Observation**

1. Increasing grid_v_damping_scale make the tree accelerate more than before.
2. Lowering substep_dt improves simulation stability and accuracy, though visual changes are minor.
3. Decreasing n_grid coarsens the grid, which reduces lateral motion. In this case, the tree stopped swaying side to side, likely due to reduced spatial resolution. 
4. Although I've tried various settings, the resulting videos seem almost the same to the original one. Increasing softening value should make the tree looks stiff, but it is not very effective in this case.

**Video Link**
Please check part2/ directory.

**Bonus**

Design a machine learning model that takes as input a video of an object undergoing physical interactions and predicts the corresponding material parameters of that object. To train the model, we can use a dataset of objects with known ground-truth parameters and simulated videos. This supervised setting allows the model to learn the relationship between observed dynamics and underlying physical properties.

To further improve learning, we can provide the model with input from a physics simulator, where the simulation parameters (e.g., Young’s modulus, damping coefficients, softening, etc.) are well-defined and controllable. By generating synthetic videos with varied but known parameters, we make the mapping from visual dynamics to material properties more learnable and robust. This hybrid data-driven and simulation-based setup enables the model to generalize to real-world videos of previously unseen materials.