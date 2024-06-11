# import the required packages
import numpy as np
import pandas as pd
from brainrender import Scene, actors, cameras
from brainrender.actors import Points
from brainrender import settings

# function which converts a csv file to a numpy array 
def csv_to_numpy_array(file_path):
    # Use pandas to read the CSV file into a dataframe
    df = pd.read_csv(file_path)
    # Convert the DataFrame to a NumPy array
    numpy_array = df.to_numpy()
    return numpy_array

#Set up brainrender scene
settings.SHADER_STYLE = "cartoon"
settings.BACKGROUND_COLOR = "white"
settings.ROOT_ALPHA = 0.1
settings.SHOW_AXES = False
scene = Scene(atlas_name="allen_mouse_25um")
STRd, GPi, GPe = scene.add_brain_region("STRd", "GPi", "GPe", alpha = 0.3)
int = scene.add_brain_region("int", alpha = .5, color="white")

#PV positive TdTomato Negative
file_path = 'some_cells.csv'  # Replace 'some_cells.csv' with the path to your CSV file if using your own data
numpy_array = csv_to_numpy_array(file_path) * 1000
cell_coordinates = np.array(pvpos_tdtomneg_numpy_array)
cells = actors.Points(pvpos_tdtomneg_cell_coordinates,  name="", colors="magenta")
scene.add(cells)

scene.render()
