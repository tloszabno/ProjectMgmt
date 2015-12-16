import CommandParser


def resolve_final_bash_command(command):
    """
        TODO test it !!!!!!!!!!!!!!!!!!!!!!!!!!!
    :param command:
    :return:
    """
    cmds = {
        'clean-install': 'echo \'Invoking mvn clean install\'',
        'get-new-code': 'echo \'Invoking git reset\'',
    }

    return cmds[command.action] + " " + " ".join(command.arguments) + " " + " ".join(command.target_modules)
