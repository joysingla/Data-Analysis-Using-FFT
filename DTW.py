from dtaidistance import dtw
import pandas as pd

data1 = pd.read_csv(First_File_Path)# Enter the First_File_Path and Second_File_Path accordingly in inverted commas . 
data2 = pd.read_csv(Second_File_Path)

merged_data = pd.merge(data1, data2, on='timestamp(ms)', suffixes=('_x', '_y'))

acceleration1 = merged_data[Name_of_Column_From_First_File_x].values # Add the suffixes after column name of firs and second file as mentioned above .
acceleration2 = merged_data[Name_of_Column_From_Second_File_y].values # Keep in mid to add '_x' after first column name and '_y' after second column name .

distance = dtw.distance(acceleration1, acceleration2)
print('DTW Distance: ',distance)
 