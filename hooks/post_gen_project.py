

is_kaggle_competition_str = '{{ cookiecutter.module_name }}'

if is_kaggle_competition_str == "Yes":
    download_command_str = "#!/bin/bash\nkaggle competitions download -c '{{ cookiecutter.module_name }}'"
    with open("script/download_data.sh", "w") as f:
        f.write(download_command_str)
