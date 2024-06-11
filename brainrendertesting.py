# import the required packages
import numpy as np
import pandas as pd
from brainrender import Scene, actors, cameras, settings
from brainrender.actors import Points

# function which converts a csv file to a numpy array 
def csv_to_numpy_array(file_path):
    # Use pandas to read the CSV file into a dataframe
    df = pd.read_csv(file_path)
    # Convert the DataFrame to a NumPy array
    numpy_array = df.to_numpy()
    return numpy_array

#Set up brainrender scene
settings.SHADER_STYLE = "plastic"
settings.BACKGROUND_COLOR = "white"
settings.ROOT_ALPHA = 0.1
settings.SHOW_AXES = False
scene = Scene(atlas_name="allen_mouse_25um")
GPi = scene.add_brain_region("GPi", alpha = 0.3)

#Place cells in position given their coordinates
file_path = 'some_cells.csv'                                                          # Replace 'some_cells.csv' with the path to your CSV file if using your own data
cell_coordinates = np.array(csv_to_numpy_array(file_path) * 1000)                     # brainrender expects nm, but Qupath gives mm, so multiply by 1000
cells = actors.Points(cell_coordinates, colors="magenta")                             # Create points actors with those coordinates
scene.add(cells)                                                                      # Add th cells to the scene

scene.render()                                                                        # Render the scene 
