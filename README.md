# NaN

A simple, Unix-style terminal

## Setup and Installing

```sh
git clone https://github.com/Nanomotion/nan
cd nan
/bin/bash setup.sh
```

## Creating your own Commands

 - Create a `.py` file in the `ext_commands/` directory
 - Edit the code in your favorite exit editor

### Example

```py
if len(prompt) > 0:
    print("The command name is " + prompt[0])
    print("Arguments: ".format(' '.join(prompt[1:])))
```

### Reference

 - `prompt` - The command entered and its arguments (list)
 - `utils.ext_cmds` - External commands found in `ext_commands/` (list)
 - `utils.cmdhelp` - The default help message (str)
 - `utils.license` - The project license (str)
 - `utils.prompt` - The default input prompt (str)
 - `spinner` - The default `Halo` spinner (`Halo`)
  - `spinner.start(text="Loading")` - Start the spinner
  - `spinner.stop()` - Stop the spinner
