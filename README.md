# Obtain Cell Detection Coordinates

Follow the examples described in https://github.com/davisreinaguerra/Wallace-Lab-Brain-Registration-Workflow to obtain a CSV file which contains Allen CCFv3 X, Y, and Z coordinates (* in millimeters) for all cells of a given class in a given brain.  Or if you would like, use the practice data ('some_cells.csv').  

# (if you havent already...) Install Brainrender

In an anaconda terminal, navigate to whatever directory your python file is in, then create an environment for brainrender

```
(base) >conda create brainrenderenvironment
```

Activate your environment with:
```
(base) >conda activate brainrenderenvironment
```

Once the environment is active, install brainrender with:

```
(brainrenderenvironment) >pip install brainrender
```

Now all you need to do is run your python code

```
(brainrenderenvironment) >python brainrendertest.py
```
