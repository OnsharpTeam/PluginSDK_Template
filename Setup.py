def setup():
    pluginName = input("Enter your Plugin's Name: ")
    replace_file(pluginName, './CMakeLists.txt')
    replace_file(pluginName, './src/CMakeLists.txt')
    replace_file(pluginName, './src/PluginInterface.cpp')
    print("Successfully setup!")

def replace_file(val, path):
    with open(path,'r') as file:
        filedata = file.read()
        filedata = filedata.replace('PluginSDK_Template', val)
    with open(path,'w') as file:
        file.write(filedata)

if __name__ == "__main__":
    setup()