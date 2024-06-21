# Modules
import numpy as np
import pandas as pd
from brainrender import Scene, actors, cameras, settings
from brainrender.actors import Points, PointsDensity

# Function which converts a csv file to a numpy array
def csv_to_numpy_array(file_path):
    df = pd.read_csv(file_path)
    numpy_array = df.to_numpy()
    return numpy_array

# Function to simplify plotting CSV files containing cells
def plot_per_csv(file_name, color):
    numpy_coords_mm = csv_to_numpy_array(file_name)            # upload coordinates in millimeters
    numpy_coords_um = numpy_coords_mm * 1000                   # convert millimeters to micrometers
    scene.add(actors.Points(numpy_coords_um, colors=color))    # add cells
    #scene.add(PointsDensity(numpy_coords_um))
    #print(numpy_coords_um)
    return numpy_coords_um

# Set up brainrender scene
settings.SHADER_STYLE = "plastic"
settings.BACKGROUND_COLOR = "white"
settings.ROOT_ALPHA = 0.1
settings.SHOW_AXES = False
scene = Scene(atlas_name="allen_mouse_25um")

# Add contextual brain regions
scene.add_brain_region("GPi", "STRd", "GPe", alpha = 0.3)

# Plot
Trace6_03 = plot_per_csv("Trace6_03.csv", "red")
Trace6_05 = plot_per_csv("Trace6_05.csv", "red")
Trace6_07 = plot_per_csv("Trace6_07.csv", "red")

all_coords = np.concatenate((Trace6_03, Trace6_05, Trace6_07), axis=0)
scene.add(PointsDensity(all_coords))

scene.render()                                                                        # Render the scene
