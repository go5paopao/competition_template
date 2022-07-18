

is_kaggle_competition_str = '{{ cookiecutter.is_kaggle}}'

if is_kaggle_competition_str.lower() == "yes":
    dl_command_str = "#!/bin/bash\n"
    dl_command_str += "kaggle competitions download -c '{{ cookiecutter.competition_name }}'\n"
    dl_command_str += "unzip -q input/{{ cookiecutter.competition_name }}.zip -d input/{{ cookiecutter.competition_name }}\n"
    with open("script/download_data.sh", "w") as f:
        f.write(dl_command_str)
