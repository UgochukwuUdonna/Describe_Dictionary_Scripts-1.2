# Demo 1

# Created by: Ugochukwu Okonkwo
# Created on: 2\06\2023

print ("Importing modules...")
import sys, arcpy, traceback
try:
    # Select by attribute
    fc = r"C:\EsriPress\Python\Data\Austin-TX\facilities.shp"
    # arcpy.management.SelectLayerByAttribute(in_layer_or_view, {selection_type}, {where_clause},
        # {invert_where_clause})
    query = """FACILITY = 'RECREATION CENTER'"""
    print (query)
    print ('Select Recreation Centers...')
    # arcpy.management.SelectLayerByAttribute = "NEW_SELECTION"
    query = """FACILITY = 'RECREATION CENTER'"""
    print (query)
    fl = arcpy.management.SelectLayerByAttribute(fc, "NEW SELECTION", query)

    theCount = int(arcpy.GetCount_management(fl)[0]

    print (f'Number of Features Selected: {theCount}')

    # If select count is greater than zero:
    if theCount > 0:
        # Then we enter the data to the table
        out_table = r"C:\temp\demo1_python.dbf"
        if arcpy.Exists(out_table):
            arcpy.Delete_management (out_table)
        # arcpy.management.CopyRows(in_rows, out_table, {config_keyword})
        print ('Creating output table...')
        arcpy.management.CopyRows(fc, out_table)

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
