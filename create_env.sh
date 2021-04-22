%%writefile make_conda_env.sh
#!/usr/bin/env bash
# author: github.com/ruxi
# reproducibly create conda env

read -p "Create new conda env (y/n)?" CONT

if [ "$CONT" == "n" ]; then
  echo "exit";
else
# user chooses to create conda env
# prompt user for conda env name
  echo "Creating new conda environment, choose name"
  read input_variable
  echo "Name $input_variable was chosen";

  # Create environment.yml or not
  read -p "Create 'enviroment.yml', will overwrite if exist (y/n)?"
    if [ "$CONT" == "y" ]; then
      # yes: create enviroment.yml
      echo "# BASH: conda env create
# source activate phd
name: $input_variable
dependencies:
- python=3.6
- pip
- jupyterlab
- notebook 
- numpy
- pandas 
- scipy 
- numpy 
- scikit-learn 
- seaborn
- pymongo 
- pip:
  - plotly">environment.yml    
    
  #list name of packages
  conda env create
    else
        echo "installing base packages"
        conda create --name $input_variable\
        python=3 jupyter notebook numpy rpy2\
        pandas scipy numpy scikit-learn seaborn 
    fi
  echo "to exit: source deactivate"
fi
