import numpy as np
import pandas as pd
from brainrender import Scene, actors, cameras
from brainrender.actors import Points
from brainrender import settings

def csv_to_numpy_array(file_path):
    # Use pandas to read the CSV file
    df = pd.read_csv(file_path)
    # Convert the DataFrame to a NumPy array
    numpy_array = df.to_numpy()
    return numpy_array

#Set up scene
settings.SHADER_STYLE = "plastic"
settings.BACKGROUND_COLOR = "white"
settings.ROOT_ALPHA = 0.1
settings.SHOW_AXES = False
scene = Scene(atlas_name="allen_mouse_25um")
STRd, GPi, GPe = scene.add_brain_region("STRd", "GPi", "GPe", alpha = 0.3)
int = scene.add_brain_region("int", alpha = .5, color="white")

#PV positive TdTomato Negative
pvpos_tdtomneg_file_path = 'PV+TdTom-.csv'  # Replace 'your_file.csv' with the path to your CSV file
pvpos_tdtomneg_numpy_array = csv_to_numpy_array(pvpos_tdtomneg_file_path) * 1000
pvpos_tdtomneg_cell_coordinates = np.array(pvpos_tdtomneg_numpy_array)
pvpos_tdtomneg_cells = actors.Points(pvpos_tdtomneg_cell_coordinates,  name="PV+TdTom-", colors="magenta")
scene.add(pvpos_tdtomneg_cells)

#PV negative TdTomato Positive
pvneg_tdtompos_file_path = 'PV-TdTom+.csv'  # Replace 'your_file.csv' with the path to your CSV file
pvneg_tdtompos_numpy_array = csv_to_numpy_array(pvneg_tdtompos_file_path) * 1000
pvneg_tdtompos_cell_coordinates = np.array(pvneg_tdtompos_numpy_array)
pvneg_tdtompos_cells = actors.Points(pvneg_tdtompos_cell_coordinates,  name="PV-TdTom+", colors="red")
scene.add(pvneg_tdtompos_cells)

scene.render()
