import sublime, sublime_plugin, os

class TitaniumHotkeyOpenJsCommand(sublime_plugin.WindowCommand):
    def run(self):
    	self.active_view = sublime.active_window().active_view()
    	self.path, self.file_name = os.path.split(self.window.active_view().file_name())
    	self.path = os.path.split(self.path)[0]
    	self.file_name_without_extension = os.path.splitext(self.file_name)[0]
    	sublime.active_window().open_file(self.path+"/controllers/"+self.file_name_without_extension+".js")

class TitaniumHotkeyOpenTssCommand(sublime_plugin.WindowCommand):
    def run(self):
    	self.active_view = sublime.active_window().active_view()
    	self.path, self.file_name = os.path.split(self.window.active_view().file_name())
    	self.path = os.path.split(self.path)[0]
    	self.file_name_without_extension = os.path.splitext(self.file_name)[0]
    	sublime.active_window().open_file(self.path+"/styles/"+self.file_name_without_extension+".tss")

class TitaniumHotkeyOpenXmlCommand(sublime_plugin.WindowCommand):
    def run(self):
    	self.active_view = sublime.active_window().active_view()
    	self.path, self.file_name = os.path.split(self.window.active_view().file_name())
    	self.path = os.path.split(self.path)[0]
    	self.file_name_without_extension = os.path.splitext(self.file_name)[0]
    	sublime.active_window().open_file(self.path+"/views/"+self.file_name_without_extension+".xml")