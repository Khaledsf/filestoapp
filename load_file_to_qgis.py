import os

dir_path = '<absolute path to dir with shapefiles>'
for folder_path, _, file_names in os.walk(dir_path):
    for file_name in file_names:
        if file_name.lower().endswith('.shp'):
            # Construct the full path of the shapefile
            shapefile_path = os.path.join(folder_path, file_name)
            print(shapefile_path)
            iface.addVectorLayer(shapefile_path, '', 'ogr')