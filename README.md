# UraniumPacker

### Description
A macho/elf compression shell that can make multi-binary into one.

||Android|iOS|macOS|
|-|-|-|-|
|arm|Yes|No|No|
|arm64|Yes|Yes|Yes|
|x86|Yes|No|No|
|x86_64|Yes|No|Yes|


### License

UraniumPacker is developed by YunYoo(云铀子), all rights reserved.

 * A.Dynamic use (liburaniumpacker.dylib/liburaniumpacker.so) is free;
 * B.Static use (liburaniumpacker.a) should pay for a license;
 * 1.动态连接(liburaniumpacker.dylib/liburaniumpacker.so)免费；
 * 2.静态连接(liburaniumpacker.a)请购买授权；

Follow us for update or bug report:

|Platform|Account|
|-|-|
|Email|liubaijiang@yunyoo.cn|
|公众号|江哥说安全|
|头条抖音|刘柏江/江哥说安全|
|微博|刘柏江VM|
|码云|https://gitee.com/geekneo/|
|码云|https://gitee.com/yunyoo/|

### Instructions

```
$ ./mac-x64/upacker 
OVERVIEW: UraniumPacker v1.0.0 , A MachO/ELF Compress & Pack Tool.

USAGE: upacker [options] <input files>

OPTIONS:
  --help                   - Display available options (--help-hidden for more)
  --packer-input=<string>  - UraniumPacker input macho/elf file
  --packer-libdir=<string> - UraniumPacker library search directory
  --packer-output=<string> - UraniumPacker output result file
  --version                - Display the version of this program
```

### Version History
2021/8/30:
 * 发布V1.0.0[preview1];
 * 1.优化二进制分析模块;
 * 2.修复桩函数寄存器覆盖导致运行时崩溃的问题；
 * 3.修复某些iOS版本ObjC初始化错误的问题；

2021/4/30:
 * 发布V1.0.0[preview0];
 * 1.支持Android arm/arm64/x86/x86_64;
 * 2.支持macOS arm64/x86_64;
 * 3.支持iOS arm64;
