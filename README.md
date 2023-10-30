# project_example

An example for a science project hosted on github. 

It is useful to define a master path in your environment for your project. When working on the project with multiple people all can set their individual paths in their environment and then use absolute paths in the project internally to generate, modify and/or analyse the data. To add the project master path to your terminal environment using Mac OS add the following line to your environment profil (e.g., .zshrc)
    
    export project_example_PATH="/Users/jtschindler/Projects/Project_Example/project_example_PATH"


### Subfolders hold the important files:
- *code* holds your calculations
- *figures* hold the files generating the figures
- *data* holds all the input data for your code
- *products* hold all the data that your code produces