from cx_Freeze import setup, Executable

# Include the name of all folder or files in your project folder that are nessesary for the project excluding your main flask file.
# If there are multiple files, you can add them into a folder and then specify the folder name.

includefiles = [ 'templates', 'static', 'Inputs', 'Outputs', 'Writingteam', 'LICENSE', 'README.md', 'requirements.txt']
includes = [ 'jinja2' , 'jinja2.ext'] 
excludes = ['Tkinter']

setup(
    name='WGPT: Basic Web Server Edition',
    version = '0.1',
    description = 'WGPT',
    options = {'build_exe':   {'excludes':excludes,'include_files':includefiles, 'includes':includes}},
    executables = [Executable('app.py')]
)
