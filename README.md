# Stable Baselines3 - Half Cheetah working

Still need to test the following:
- It is on Mac
- It is on Linux

### Install Mujoco
For Linux:

`wget https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz`

or for Mac:

`https://mujoco.org/download/mujoco210-macos-x86_64.tar.gz`

Extract:
```
mkdir ~/.mujoco/
tar -xvf mujoco210-linux-x86_64.tar.gz -C ~/.mujoco
```

Export (may add to `.bashrc`):
```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/did1tv/.mujoco/mujoco210/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia
```

`apt install`s needed:
```
sudo apt install libglew-dev
sudo apt-get install patchelf

```

Adding on Linux to `.bashrc`:
```
export LD_LIBRARY_PATH=/home/did1tv/.mujoco/mujoco210/bin:/usr/lib/nvidia
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libGLEW.so
```

### How to run from command line (from main project folder):
`venv/bin/python -m src.run_half_cheetah`

### How to make a venv
`~/pythons/miniconda_397/bin/python -m venv ./venv`

### How to install requirements
``