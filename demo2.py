# Demo 2 Chapter 5 E

# Created by: Ugochukwu Okonkwo
# Created on: 2\8\2023

print ("Importing modules...")
import sys, arcpy, traceback
try:
    # Create Feature Class Variable
    folder = r"C:\EsriPress\Python\Data\Austin-TX"
    fac = folder + r"\facilities.shp"
    br = folder + r"\bike_routes.shp"


    # Select facilities within 100 feet of bike routes
    # arcpy.management.SelectLayerByLocation(in_layer, {overlap_type}, {select_features},
        # {search_distance}, {selection_type}, {invert_spatial_relationship})
    fac_layer = arcpy.management.SelectLayerByLocation(fac, "WITHIN_A_DISTANCE", br, "100 feet", "NEW_SELECTION")
    theCount = int(arcpy.GetCount_management(fac_layer).getOutput(0))
    print(theCount)
    # Select the facilities that are recreation centers
    # FACILITY = 'RECREATION CENTER'
    q = """FACILITY = 'RECREATION CENTER'"""
    # arcpy.management.SelectLayerByAttribute(in_layer_or_view, {selection_type}, {where_clause}, {invert_where_clause})
    arcpy.management.SelectLayerByAttribute(fac_layer, "SUBSET_SELECTION", q)
    theCount = int(arcpy.GetCount_management(fac_layer).getOutput(0))
    print(theCount)

    if theCount > 0:
        out = r"C:\temp\demo2_chpExt_python.shp"
    if arcpy.Exists(out):
        arcpy.Delete_management(out)
        # arcpy.management.CopyFeatures(in_features, out_feature_class, {config_keyword},
        #   {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})
        arcpy.CopyFeatures_management(fac_layer, out)
    else:
        print('No feature was selected')


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
