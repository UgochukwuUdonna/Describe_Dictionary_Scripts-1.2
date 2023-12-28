# SECOND DEMO CHAP 5 EXT

# Created by: Ugochukwu Udonna Okonkwo
# Created on: 2-8-2023

print ("Importing modules...")
import sys, arcpy, traceback
try:
    # CREATE FEATURE CLASS VARIABLES
    folder = r'C:\EsriPress\Python\Data\Austin-TX'
    fac = folder + r'\facilities.shp'
    br = folder + r'\bike_routes.shp'
    # SELECT FACILITIES WITHIN 100 FEET OF BIKE ROUTES. 62
    # arcpy.management.SelectLayerByLocation(in_layer, {overlap_type}, {select_features},
        # {search_distance}, {selection_type}, {invert_spatial_relationship})
    fac_layer = arcpy.management.SelectLayerByLocation(fac, 'INTERSECT', br, '100 FEET', "NEW_SELECTION")
    theCount = int(arcpy.GetCount_management(fac_layer).getOutput(0))
    print (theCount)
    # FROM SELECTED FACILITIES SELECT THE RECREATION CENTERS. 7
    # FACILITY = 'RECREATION CENTER'
    q = """FACILITY = 'RECREATION CENTER'"""
    # arcpy.management.SelectLayerByAttribute(in_layer_or_view, {selection_type}, {where_clause}, {invert_where_clause})
    arcpy.management.SelectLayerByAttribute(fac_layer, 'SUBSET_SELECTION', q)
    theCount = int(arcpy.GetCount_management(fac_layer).getOutput(0))
    print (theCount)

    if theCount > 0:
        # EXPORT SELECTED FEATURES TO A NEW FEATURE CLASS
        out = r'c:\temp\demo2_chp5ext_python.shp'
        if arcpy.Exists(out):
            arcpy.Delete_management(out)
        # arcpy.management.CopyFeatures(in_features, out_feature_class, {config_keyword},
        #   {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})
        arcpy.CopyFeatures_management(fac_layer, out)
    else:
        print ('No features were selected.')
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
