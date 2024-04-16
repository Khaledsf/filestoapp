import os

for folder_path, _, file_names in os.walk('/Users/khaledbouchama/Downloads/IND/Telangana'):
    for file_name in file_names:
        if file_name.lower().endswith('.shp'):
            # Construct the full path of the shapefile
            shapefile_path = os.path.join(folder_path, file_name)
            print(shapefile_path)
            iface.addVectorLayer(shapefile_path, '', 'ogr')