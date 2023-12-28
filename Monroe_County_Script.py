# Monroe_County_Script

# Created by: Ugochukwu Udonna Okonkwo
# Created on: 2/18/2023

print ("Importing modules...")
import sys, arcpy, traceback
try:
    arcpy.env.workspace = r'C:\Geog_432\Chapter_5\MonroeCountyData.gdb'
    # SELECT BY ATTRIBUTE SOILS THAT ARE TYPE W
    soils = 'soils_partial'
    parcels = 'ALL_PARCELS'
    print('start geoprocessing')
    # MUSYM = 'W'
    q = """MUSYM = 'W'"""
    print(q)

    # arcpy.management.SelectLayerByAttribute(in_layer_or_view, {selection_type},
    # {where_clause}, {invert_where_clause})
    soils_fl = arcpy.SelectLayerByAttribute_management(soils, 'NEW_SELECTION', q)
    theCount = int(arcpy.GetCount_management(soils_fl).getOutput(0))
    print('number of soils that are type W ' + str(theCount))

    # SELECT PARCELS THAT ARE NOT WITHIN 1500 FEET
    # arcpy.management.SelectLayerByLocation(in_layer, {overlap_type}, {select_features},
    # {search_distance}, {selection_type}, {invert_spatial_relationship})
    parcels_fl = arcpy.management.SelectLayerByLocation(parcels, "WITHIN_A_DISTANCE", soils_fl, "1500 Feet", "NEW_SELECTION", "INVERT")
    theCount = int(arcpy.GetCount_management(parcels_fl).getOutput(0))
    print('number of parcels that are not within 1500 feet ' + str(theCount))

    # EXPORT SELECTION TO A FEATURE CLASS
    if theCount > 0:
        # arcpy.management.CopyFeatures(in_features, out_feature_class, {config_keyword},
        # {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})
        output = r"c:\temp\parcels.shp"
        if arcpy.Exists(output):
            arcpy.Delete_management(output)
        arcpy.management.CopyFeatures(parcels_fl, output)
        print('output features are located at ' + output)
    else:
        print('no parcels were selected')
    print('end geoprocessing')







except:

    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n     " + str(sys.exc_info()[1])

    msgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(2) + "\n"

    arcpy.AddError(msgs)
    arcpy.AddError(pymsg)

    print (msgs)
    print (pymsg)

    arcpy.AddMessage(arcpy.GetMessages(1))
    print (arcpy.GetMessages(1))
