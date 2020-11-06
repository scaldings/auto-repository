# auto-repository
This python script automatically creates a new repository
  
  
## How to automate this?  
1. [Create a token](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token)
2. Change the variable values in the ```secrets.py``` file **or** replace the values in ```new.py```
3. Create a new file with the name of your preference and the extension ```.bat```
      1. For the first line of the file, you have to navigate to the directory of your ```new.py``` script, so for  
      example in my case it is ```cd C:\Coding\my-repositories\auto-repository\```
      2. For the second line, you want to launch the python script. Ex.: ```python new.py```
4. Move your ```.bat``` file into the ```C:\Windows``` directory
5. You're done. Whenever you want to use it just type the name of your script in the command  
line. In my case it is ```auto```, so I just type ```auto```and it runs the script. *(Note, that  
you can run the command with or without the ```.bat``` extension)*
