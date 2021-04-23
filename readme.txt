# create conda environment with dependencies:

conda env create -f environment.yml

# activate environment:

conda activate monitor

# add conda environment to jupyter lab:

ipython kernel install --user --name=monitor_kernel

# run notebook:

conda run jupyter-lab .
