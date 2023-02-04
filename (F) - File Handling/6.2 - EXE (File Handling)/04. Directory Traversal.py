import os
directory = input()
directory_list = os.listdir(directory)
extensions_dict = {}
for file in directory_list:
    file_list = file.split(".")
    extension = "." + file_list[-1]
    if extension not in extensions_dict.keys():
        extensions_dict[extension] = [file]
    else:
        extensions_dict[extension].append(file)
sorted_extensions_dict = dict(sorted(extensions_dict.items(), key=lambda x: x[0]))
report_list = []
for extension, files_list in sorted_extensions_dict.items():
    report_list.append(f"{extension}\n")
    sorted_files_list = sorted(files_list)
    for file in sorted_files_list:
        report_list.append(f"- - - {file}\n")
with open("report.txt", "w") as file:
    file.writelines(report_list)
