
import os
import numpy as np
import pandas as pd
from astropy.cosmology import FlatLambdaCDM

def do_main_calculation(master_path):

    # Instantiate a cosmology
    cosmology = FlatLambdaCDM(70, 0.3)

    # Define a redshift array
    redshifts = np.arange(0, 20, 0.01)

    # Calculate the luminosity distance
    lum_dist = cosmology.luminosity_distance(redshifts)

    # Create a pandas dataframe with the data
    data_dict = {'redshift': redshifts,
                 'lum_dist': lum_dist}
    df = pd.DataFrame(data_dict)

    # Save data frame
    save_path = os.path.join(master_path, 'products', 'luminosity_distance.csv')
    df.to_csv(save_path, index=False)




if __name__ == '__main__':


    # Set the path variables
    """ It is useful to define a master path in your environment
    for your project. When working on the project with multiple 
    people all can set their individual paths in their environment
    and then use absolute paths in the project internally to generate,
    modify and/or analyse the data.
    To add the project master path to your terminal environment using
    Mac OS add the following line to your environment profil (e.g., .zshrc)
    
    export project_example_PATH="/Users/jtschindler/Projects/Project_Example/project_example_PATH"
    
          
    """
    master_path = os.getenv('project_example_PATH')


    # Execute main calculation
    do_main_calculation(master_path)