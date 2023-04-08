# Path to your data.
# For example:
#   - data
#       - control_g1
#           - fly1.csv
#           - fly2.csv
#           - ...
#       - control_g2
#       - substance_g1
#       - substance_g2
DATA_PATH = r"C:\Users\milos\Downloads\data"

# Population name should be the prefix of the folder name (see example above).
POPULATION_1_PREFIX = "control"
POPULATION_2_PREFIX = "substance"

EXPERIMENT_DURATION = 60 #experiment duration time must be in seconds
FPS = 60
WINDOW_SIZE = 3

# Distance between flies in pixels which defines existance of social interaction.
DISTANCE_BETWEEN_FLIES = 18 # px distance, arena is 120mm wide, 1000x1000 on x,y axis
                            # 17px is equal to 2 body distances between flies
TOUCH_DURATION_SEC = 0.6

# If False the plots will be saved as images, but not shown during execution
SHOW_PLOTS = False