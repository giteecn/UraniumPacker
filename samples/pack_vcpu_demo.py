import os
import sys
import platform

def file_dir():
    dir = os.path.dirname(__file__)
    if len(dir) == 0:
        dir = '/'
        return dir
    return dir

def upacker():
    sysname = platform.system()
    machine = platform.machine()
    if sysname == 'Darwin':
        if machine == 'x86_64':
            return file_dir() + '/../mac-x64/upacker'
        return file_dir() + '/../mac-arm64/upacker'
    else:
        return file_dir() + '/../win/upacker.exe'

def do_pack(inputs, output):
    cmd = upacker() + ' '
    for i in inputs:
        cmd += '--packer-input=' + i + ' '
    cmd += '--packer-output=' + output + ' '
    os.system(cmd)

def main():
    uvcpu_root = file_dir() + '/../../UraniumVCPU'
    if not os.path.exists(uvcpu_root):
        print('There is no UraniuvmVCPU repo(%s), you can git clone it at https://gitee.com/yunyoo/UraniumVCPU .' % (uvcpu_root))
        sys.exit(0)
        
    jni_archs = ['armeabi-v7a', 'arm64-v8a', 'x86', 'x86_64']
    for a in jni_archs:
        print('Packing Android %s...' % (a))
        do_pack([
          '%s/android/%s/liburaniumvm.so' % (uvcpu_root, a), 
          '%s/sample/libs/%s/uraniumvm_apitest' % (uvcpu_root, a)
        ], '%s/android_upacker_%s' % (file_dir(), a))

    print('Packing iOS arm64...')
    do_pack([
      '%s/ios/arm64/liburaniumvm.dylib' % (uvcpu_root),
      '%s/sample/ios/uraniumvm_apitest' % (uvcpu_root)
    ], '%s/ios_upacker_arm64' % (file_dir()))

    print('Packing macOS x86_64...')
    do_pack([
      '%s/mac/x64/liburaniumvm.dylib' % (uvcpu_root),
      '%s/sample/mac/uraniumvm_apitest_x64' % (uvcpu_root)
    ], '%s/mac_upacker_x86_64' % (file_dir()))

    print('Packing macOS arm64...')
    do_pack([
      '%s/mac/arm64/liburaniumvm.dylib' % (uvcpu_root),
      '%s/sample/mac/uraniumvm_apitest_arm64' % (uvcpu_root)
    ], '%s/mac_upacker_arm64' % (file_dir()))

main()
