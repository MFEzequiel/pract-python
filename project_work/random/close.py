import os

def close(pro):
    program = os.popen(f"{pro}").read().strip().split('\n')
    
    for process in program:
        while process:
            if process:
                pid = int(process.split()[1])
                os.kill(pid, signal.SIGTERM)


close('dllhost.exe')