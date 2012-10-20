import sublime, sublime_plugin

#-------------------------------------------------------------------------------
#
# Plugin:         LinesToColumns
#
# Compatibility:  Sublime Text 2, Version 2.0.1, Build 2217
#
# Last Modified:  20 October 2012
#
#-------------------------------------------------------------------------------

class PromptLinesToColumnsCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.show_input_panel("Lines per record <delimiter (optional, default='|')>:", 
            "", self.on_done, None, None)
 
    def on_done(self, text):
        try:
            if self.window.active_view():
                self.window.active_view().run_command("lines_to_columns", {"args": text} )
        except ValueError:
            pass


class LinesToColumnsCommand(sublime_plugin.TextCommand):

    def lines_to_cols(self, text, args):

        delimiter = '|'
        arg_delimiter = ' '
        error_status = False
        line_end = '\n'

        # feeble attempt to handle the oddball case of CRLF
        if self.view.line_endings().lower() == 'windows':
            line_end = '\r\n'

        try:

            if len(args.split(arg_delimiter)) > 1:
                delimiter = args.split(arg_delimiter)[1]
                if len(delimiter) == 0: delimiter = '|'
                number_of_columns = int(args.split(arg_delimiter)[0])
            else:
                number_of_columns = int(args)

        except:
            return ('', True)

        text_array = text.split(line_end)
        new_text = []
 
        lines = len(text_array)
        offset = 0

        while offset + number_of_columns <= lines:
            sub_array = text_array[offset:offset + number_of_columns]
            new_text.append(delimiter.join(sub_array))
            offset += number_of_columns

        return (line_end.join(new_text), error_status)

    def run(self, edit, args):

        for region in self.view.sel():
            if not region.empty():
                s = self.view.substr(region)
                (new_text, error_status) = self.lines_to_cols(s, args)
                if not error_status:
                    self.view.replace(edit, region, new_text)
