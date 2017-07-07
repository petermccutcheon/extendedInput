# -*- coding: utf-8 -*-
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#	THIS IS A FUNCTION DEFINITION MODULE.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#************************************************************************************************************************************************
#***** Author:		Peter McCutcheon
#***** Created:		6/10/2017
#***** Modified:
#*****
#------------------------------------------------------------------------------------------------------------------------------------------------
#***** Description:
#*****
#*****		This is a module that contains functions to assist in obtaining input from the user via the standard keyboard input.
#*****
#*************************************************************************************************************************************************

#=====================================================================================================
#==		Define input function here
#=====================================================================================================

def extendInput(msg, options, listrange, exitValue):

    inputValid = False
    dType = options['primary'][2]
    
    while not inputValid:
        #
        #   Input the value from the user.
        #
        inputValue = input(msg)
        if inputValue.upper() == exitValue.upper():
            inputValid = True
        else:
            #
            #   Force the input to match the datatype provided for validation.
            #
            if dType == "I":
                inputValue = int(inputValue)
            elif dType == "S":
                inputValue = str(inputValue)
            elif dType == "F":
                inputValue = float(inputValue)
            elif dType == "B":
                inputValue = bool(inputValue)
            else:
                print("Error--extendedInput-- Unknown datatype provided for validation test, please contact IT or developer.")
                return False
            #
            #   Validate the input.
            #
            inputValid = validateInput(inputValue, options, listrange)

    return inputValue

#=====================================================================================================
#==		Define validation function here
#=====================================================================================================

#
#   Validation is defined by two parameters. The validationOptions parameter is a dictionary
#   with this format {'primary': "", 'secondary': "", 'tertiary': ""}.  The 'primary' key is
#   always a data type check defined like this DTx - Datatype ([S]tring, [I]nteger, [F]loat, [B]oolean)
#   where the x is the first character as show above.
#   The 'secondary' key is for a list of values validation and can be one of the following,
#       1. LOS - List of string values.
#       2. LOI - List of integer values.
#       3. LON - List of float values
#       4. LOF - List of files
#   The 'tertiary' key is for a range of values.  These can be one of the following.
#       1. IR - Numeric range
#       2. FR - Float number range.
#       3. SR - String range.
#   If the secondary and/or tertiary keys are not going to be used then they should be null string "".
#   Please note that you can have no secondary and still have a tertiary.
#
#   The validationList parameter is a dictionary with two key entries.  The first key is 'list' with a
#   Python list and the second is 'range' also with a Python list.
#
#   Example1:
#       validationOptions = {'primary':'DTI', 'secondary':'LOI', 'tertiary':'IR'}
#       validationList = {'list':['1', '2', '3'], 'range':['10', '20']}
#
#       For this example there is a integer data type check and both a list of
#       integers and an integer range.  A valid integer must be either 1, 2, or 3 or 
#       between 10 and 20 inclusive.
#
#   Example2:
#       validationOptions = {'primary':'DTI', 'secondary':'LOI', 'tertiary': 'IR'}
#       validationList = {'list':[], 'range':['10', 'L']}
#  
#       For this example there must be a valid integer that is greater than or equal to 10.
#       Note: If the L and 10 were switched then the number would need to be less than or
#       equal to 10.
#
#
def validateInput(valueToCheck, validationOptions, validationList):

    #
    #   Set the return value to be false (invalid).  This will be
    #   changed to true (valid) if the validation passes.  If for
    #   some reason it does not get set later this value will indicate
    #   a failed validation.
    #
    returnValue = False

    #
    #   Get the validationOptions and load them into local variables.
    #   If they are not set up properly print an error and exit.
    #
    try:
        if validationOptions['primary'] != "":
            primary = validationOptions['primary']
        else:
            primary = ""
    except KeyError:
        print("Error--extendedInput-- Invalid parameters contact IT or developer.")
        return False
        
    try:
        if validationOptions['secondary'] != "":
            secondary = validationOptions['secondary']
        else:
            secondary = ""
    except KeyError:
        print("Error--extendedInput-- Invalid parameters contact IT or developer.")
        return False
    
    try:
        if validationOptions['tertiary'] != "":
            tertiary = validationOptions['tertiary']
        else:
            tertiary = ""
    except KeyError:
        print("Error--extendedInput-- Invalid parameters contact IT or developer.")
        return False

    #
    #   Check if a list of values or range is provided then load them into local variables.
    #
    if secondary != "":
        try:
            if len(validationList['list']) != 0:
                lov = validationList['list']
            else:
                print("Warning--extendedInput-- List of values specified, but no list provided.")
        except KeyError:
            print("Error--extendedInput-- Invalid parameters contact IT or developer.")
            return False
    else:
        lov = ""
        
    if tertiary != "":
        try:
            if len(validationList['range']) != 0:
                range = validationList['range']
            else:
                print("Warning--extendedInput-- Range specified, but no range provided.")
        except KeyError:
            print("Error--extendedInput-- Invalid parameters contact IT or developer.")
            return False
    else:
        range = ""
        
    #
    #   Check to makes sure the list of values and range, if present, datatypes match
    #   the value sent.
    #
    typeMatch = True
    typeValue = type(valueToCheck)
    if secondary != "":
        for element in validationList['list']:
            if typeValue is not type(element):
                 typeMatch = False
                 
    if not typeMatch:
        print("Error--extendedInput-- List of values provided does not match desired input datatye.")
        return False
        
    typeMatch = True
    if tertiary != "":
        for element in validationList['range']:
            if element != 'L':
                if typeValue is not type(element):
                    typeMatch = False
        
    if not typeMatch:
        print("Error--extendedInput-- Range provided does not match desired input datatype.")
        return False
        
    #
    #   Verify that the value sent is valid for the primary test.
    #
    if primary != "":
        if primary[2] == "S":
            if type(valueToCheck) is str:
                returnValue = True
            else:
                print("Invalid datatype, looking for string, received " + str(type(valueToCheck)))
                returnValue = False
        elif primary[2] == "I":
            if type(valueToCheck) is int:
                returnValue = True
            else:
                print("Invalid datatype, looking for integer, received " + str(type(valueToCheck)))
                returnValue = False
        elif primary[2] == "F":
            if type(valueToCheck) is float:
                returnValue = True
            else:
                print("Invalid datatype, looking for float, received " + str(type(valueToCheck)))
                returnValue = False
        elif primary[2] == "B":
            if type(valueToCheck) is bool:
                returnValue = True
            else:
                print("Invalid datatype, looking for boolean, received " + str(type(valueToCheck)))
                returnValue = False
        else:
            return False
    #
    #   Check the secondary validation.
    #
    secondaryCheck = False
    if secondary != "":
        if primary[2] == "S":
            valuelist = [vl.upper() for vl in validationList['list']]
            valueToCheck = valueToCheck.upper()
        else:
            valuelist = validationList['list']
        if valueToCheck in valuelist:
            secondaryCheck = True
            returnValue = True
        else:
            #
            #   If we did not find out data in the validation list, it might be found
            #   in our tertiary check which is a range.  If we don't have a tertiary
            #   check then we have invalid data.
            #
            if tertiary == "":
                print("Invalid data, expecting one of " + str(validationList['list']) + " received " + str(valueToCheck))
                returnValue = False
    #
    #   Check the tertiary validation
    #
    if tertiary != "" and not secondaryCheck:
        try:
            if str(range[0]) == "L":
                if valueToCheck <= range[1]:
                    returnValue = True
                else:
                    print("Invalid data, expecting value equal or less than " + str(range[1]) + " received " + str(valueToCheck))
                    returnValue = False
            elif str(range[1]) == "L":
                if valueToCheck >= range[0]:
                    returnValue = True
                else:
                    print("Invalid data, expecting value equal or greater than " + str(range[0]) + " received " + str(valueToCheck))
                    returnValue = False
            else:
                print("Checking range.")
                if valueToCheck >= range[0] and valueToCheck <= range[1]:
                    returnValue = True
                else:
                    print("Invalid data, expecting value equal or between " + str(range) + " received " + str(valueToCheck))
                    returnValue = False
        except:
            print("Error--extendedInput-- Unexpected error in tertiary validation, contact IT or developer.")
            return False

    #
    #   Validation complete return with True or False depending of if valid
    #
    return returnValue