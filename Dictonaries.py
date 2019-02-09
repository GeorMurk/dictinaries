#!/usr/bin/python

#!Using Python Dictionary

month_convert = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec" : "December",
}

print(month_convert["Apr"])
print(month_convert.get("Jul"))
print(month_convert.get("SAT", "Not Valid")) #!Gives out a default response.


#!Go ahead and Test it out!!!!
