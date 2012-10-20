LinesToColumns (Sublime Text 2 Plugin)
======================================

Sublime Text 2 plugin to contract lines of text into delimited columns

# Description

Converts the selected text in the current window from lines to columns
based on the number returned from user prompt. For example, if the 
selected text is:

col1
col2
col3

... then you can run this command with argument "3 @" and get:

col1@col2@col3

This is useful as a quick and dirty hack for making columnar files for
raw data. The prompt asks for the number of columns, and optionally a delimiter 
to be used to separate the columns. 

If the default delimiter of '|' is acceptable, the reply should simply be
the number of columns required. For example:

  9     (result: number_of_columns=9, delimiter='|')

If a delimiter is supplied, the arguments must be provided as a 
space-separated list like so (one space only please):

  26 ~  (result: number_of_columns=26, delimiter='~')

If a space is the desired delimiter, you are out of luck!

# Notes

This plugin can be run from console with:

view.run_command('prompt_lines_to_columns')

This plugin was developed on Linux. While a feeble attempt has been made to 
account for CRLF line endings, this has not been tested. You have been warned!


# License

This plugin is provided 'as-is'; it is free to be copied, 
modified, used, bent, folded, and/or mutilated. The author 
takes no responsibility for any form of damages incurred 
as a result of its use. This includes, but is not limited to,
loss of data, loss of computer operation, or loss of hair. 

If any modification is made, please recognize that you are now 
the new plugin's author, and that you must change this header 
to take full credit (or to incur the emotional toll of legally 
toothless shame and blame).

If you have read this far into the license you probably have
better things to do with your time.
