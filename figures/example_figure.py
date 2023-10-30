
import os
import pandas as pd
import matplotlib.pyplot as plt


def lum_dist_vs_redsh(master_path, save_name='luminosity_distance.pdf',
                      save=False):

    # Load the data file
    path = os.path.join(master_path, 'products', 'luminosity_distance.csv')
    df = pd.read_csv(path)

    # Build the figure
    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(111)
    print(df)
    ax.plot(df.redshift, df.lum_dist, lw=2, label='Luminosity distance', color='k')

    ax.set_xlabel('Redshift', fontsize=17)
    ax.set_ylabel('Luminosity distance (Mpc)', fontsize=17)

    ax.legend(fontsize=15)
    ax.tick_params(axis='both', labelsize=15)

    plt.tight_layout()

    # if save and save_name is not None:
    #     plt.savefig(os.path.join(master_path, 'figures', 'pdf', save_name))
    # else:
    plt.show()




if __name__ == '__main__':

    # Define the master path
    master_path = os.getenv('project_example_PATH')

    # Define functions for the figures above and then call them here.

    # Make figure and show it.
    lum_dist_vs_redsh(master_path)

    # Make figure and save it
    lum_dist_vs_redsh(master_path, save=True)