# Sample code snippet..
    def start(self, version):

        msbuild = os.getenv('MSBUILD_PATH', r"C:\Program Files\MSBuild\12.0\Bin\MSBuild.exe")
        project_output_dir = os.getenv('PROJECT_OUTPUT_DIR', r'c:\Build_distribute\')

        if not os.path.exists(msbuild):
            raise Exception('not found ' + msbuild)

        projects = [r"..\yoursolution.sln", r"..\yourproject\yourproject.vcxproj"]
        win32_targets = '/t:ProjectA:rebuild;ProjectB:rebuild;ProjectC:rebuild'
        x64_targets = '/t:ProjectA:rebuild;ProjectB:rebuild;ProjectC:rebuild'

        rebuild = '/t:Rebuild'
        debug = '/p:Configuration=Debug'
        release = '/p:Configuration=Release'
        x64 = '/p:Platform=x64'
        win32 = '/p:Platform=Win32'
        xp_toolset = '/p:PlatformToolset=v110/v100/v90'

        #msbuild %s.vcxproj /t:rebuild /p:configuration=VC90Release,platform=%s
        #msbuild myproject.vcxproj /p:PlatformToolset=v90 /t:rebuild
        #msbuild myproject.vcxproj /p:PlatformToolset=v110_xp /t:rebuild

        # making command line to run
        default = [msbuild]
        default.append('/m:1')  # https://msdn.microsoft.com/en-us/library/ms164311.aspx

        libs = default [:]
        libs.append(projects[0])    # append a project/solution name to build command-line

        if self.build_arch_target == 'x86':
            default.append(win32)
            # win32 targets
            default.append(win32_targets)

    def build(self, lib_to_build):
        build_result = False

        print ('Build Start ************************')
        print ('Target Platform: ' + self.build_arch_target)
        print('configuration: ' + self.build_type)

        process = subprocess.Popen(args = lib_to_build, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        while True:
            nextline = process.stdout.readline()
            if nextline == b'' and process.poll() != None:
                break
            sys.stdout.write(nextline.decode('cp949'))      # adjust the codepage for your console
            sys.stdout.flush()

        output = process.communicate()[0]
        exitCode = process.returncode

        if (exitCode == 0):
            build_result = True
            pass    #return output
        else:
            build_result = False
            #raise Exception(command, exitCode, output)
        print ('************************')
        print('build finished %d ' % process.returncode)

        return build_result