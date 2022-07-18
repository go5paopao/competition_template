

is_kaggle_competition_str = '{{ cookiecutter.is_kaggle}}'

if is_kaggle_competition_str == "Yes":
    dl_command_str = "#!/bin/bash"
    dl_command_str += "kaggle competitions download -c '{{ cookiecutter.competition_name }}'"
    dl_command_str += "unzip -q input/{{ cookiecutter.competition_name }}.zip -d input/{{ cookiecutter.competition_name }}"
    with open("script/download_data.sh", "w") as f:
        f.write(dl_command_str)
