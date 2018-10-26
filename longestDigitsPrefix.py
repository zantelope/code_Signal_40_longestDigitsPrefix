###import regular expression operations module to split string by digits and other characters
import re


def longestDigitsPrefix(inputString):
    ## split the string up
    ## '(\d+)' separates digit chunks
    splitString = re.split('(\d+)',inputString)

    ### filter empty values from splitString, assign result to splitString
    splitString = list(filter(None, splitString))

    ### check if first item in splitString is a digit, if so, return it
    if splitString[0].isdigit():
        return splitString[0]
        
    ### otherwise, return Empty
    return ""
