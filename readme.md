# CodeSys

## Instructions:

Execute scripts within CodeSys software.

1. Menu execution
![run_script.png](screenshots/run_script.png)

`export.py`:

1. Select script
   ![sel_script_ex](screenshots/sel_script_ex.png)
2. Select the code (directory) to be exported, leave blank for the entire directory
   ![sel_files_dir](screenshots/sel_files_dir.png)
3. Select the folder (export to)
   ![sel_folder_ex](screenshots/sel_folder_ex.png)
4. If the folder is not empty, prompt whether to delete the files in it.
   ![tip_export](screenshots/tip_export.png)
5. Result information
   ![succ_export](screenshots/succ_export.png)

`load.py`:
1. Select script
   ![sel_script_im](screenshots/sel_script_im.png)
2. Select the folder (Import from)
   ![sel_folder_im](screenshots/sel_folder_im.png)
3. Result information
   ![succ_load](screenshots/succ_load.png)

## Script description:

`export.py`:

- [x] Back up the ST language text code and Global_var, Textlist and Task_Configuration, library in Codesys to the Save_Folder folder.
- [x] Back up the text codes in the specified folder to the Save_Folder folder. If not specified, it will be the text codes of all working conditions.
- [x] If the Save_Folder folder is not empty, you will be prompted to delete the files in it, excluding `.git` and `.svn` files.
- [ ] If there is a .git file in the folder, update the folder to HEAD.
  
`load.py`:
- [x] Import the text code in the above folder into the current project.
- [ ] Device folder/file import.
  
## question:

- Except for text in ST language, others such as: Visu, imagePool, VisuConfiguration, Project Settings, Project Infomation are not exported.
- GlobalTextList will lose the ID Column data.


## Acknowledgments:

- [`CODESYS Online Help`](https://help.codesys.com/webapp/System;product=ScriptEngine)
- [`18thCentury/CodeSys`](https://github.com/18thCentury/CodeSys)