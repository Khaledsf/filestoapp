import os
import geopandas as gpd
import psycopg2
from sqlalchemy import create_engine

db_user = '<username>'
db_password = '<password to access db>'
db_name = '<name of db>'
db_host = '<localhost or address to remote host>'
db_port = '<ex:5432>'
connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

# Create a SQLAlchemy engine
engine = create_engine(connection_string)

# Define the root folder containing shapefiles
root_folder = '<ex:/Users/johndoe/Desktop/mydirectory>'
# Loop through folders and process shapefiles
for folder_path, _, file_names in os.walk(root_folder):
    for file_name in file_names:
        if file_name.lower().endswith('.shp'):
            # Construct the full path of the shapefile
            shapefile_path = os.path.join(folder_path, file_name)
            
            # Read the shapefile into a GeoDataFrame
            gdf = gpd.read_file(shapefile_path)

            #################################################################
            # Optional: Alter the file name or skip
            # table_name = shapefile_path.replace('<undesired path>', '')
            # table_name = file_name.replace('.shp', '')
            # state_name = shapefile_path.split('/')[5].lower().replace(' ','')
            # table_name = table_name.replace('/','_')
            # new_name = state_name + '_' + table_name
            #################################################################
            schema = '<db Schema name>'
            # Write the GeoDataFrame to PostgreSQL
            gdf.to_postgis(new_name, engine, schema=schema)
            print(f'Table {schema}.{new_name} created successfully........')
# Close the connection
conn.close()