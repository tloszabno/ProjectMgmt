import Config
import re

def resolve_final_bash_command(command):
    try:
        cmd = Config.actions[command.action][1]

        args_to_set_number = len(re.findall('{\d+}', cmd))
        if args_to_set_number > 0:
            #TODO: optimize
            if len(command.arguments) == 0:
                #use defualts
                cmd = cmd.format(*Config.actions[command.action][-1])
            else:
                cmd = cmd.format(*command.arguments)
            return cmd.rstrip()

        return (cmd + " " + " ".join(command.arguments)).rstrip()
    except:
        msg = "Action [%s] has no definition" % command.action
        raise Exception(msg)
