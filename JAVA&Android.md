# JAVA&Android

安卓推荐：

尚硅谷 安卓教程

天哥在奔跑 安卓开发教程

程序猿拉大锯 安卓开发自定义组件

动脑学院 kotlin

longway777 jetpack



java基础：韩顺平

尚硅谷：安卓

天哥在奔跑：安卓

longway777： jetpack（主流的开发框架 谷歌出的套件）



安卓基础：activity service provider

学好基础再学kotlin

安卓基础：

尚硅谷Android视频教程《15天精讲精练_参悟Android核心技术—上》

https://www.bilibili.com/video/BV1hW411L7CH/?spm_id_from=333.999.0.0

尚硅谷Android视频教程《15天精讲精练_参悟Android核心技术-中》

https://www.bilibili.com/video/BV1BW411L7QW/?spm_id_from=333.999.0.0&vd_source=d31ec3e5b50ba0ea326786df2a78a612

尚硅谷Android视频教程《15天精讲精练_参悟Android核心技术-下》

https://www.bilibili.com/video/BV1BW411L7th/?spm_id_from=333.999.0.0&vd_source=d31ec3e5b50ba0ea326786df2a78a612

## JAVA



## Android

![image-20240305170242795](JAVA&Android.assets/image-20240305170242795.png)

应用层开发的就是最上面那层 两个方向 要么一直在应用层 要么往下

![image-20240306093110579](JAVA&Android.assets/image-20240306093110579.png)





更新JDK

本地的jdk版本比代码需要的高，下载个低版本的就行

解决方法：File -> Settings -> Build, Execution, Deployment -> Build Tools -> Gradle

![img](JAVA&Android.assets/企业微信截图_17097144902.png)

点ok之后 先同步工程

![image-20240306104445869](JAVA&Android.assets/image-20240306104445869.png)

再编译

![img](JAVA&Android.assets/企业微信截图_17097146385119.png)

Android Studio中布局文件（如activity_main.xml）设计视图&代码视图相互切换

第一个安卓应用

- File->New->New Project

- empty views activity

- ![image-20240306111404990](JAVA&Android.assets/image-20240306111404990.png)

mainactivity.java

![image-20240306111544353](JAVA&Android.assets/image-20240306111544353.png)

`MainActivity.java` 是在使用 Java 语言开发 Android 应用程序时常见的一个类文件。在 Android 应用的开发中，它通常扮演着应用程序的入口点角色。每当你启动一个 Android 应用时，`MainActivity` 是首个被加载和执行的活动（Activity），负责创建和显示应用程序的主界面。

具体而言，`MainActivity.java` 的作用包括但不限于：

1. **初始化界面：** 它负责加载应用的布局资源（定义在 XML 文件中），并将其显示给用户。这包括设置应用的布局、初始化界面元素等。
2. **处理用户交互：** `MainActivity` 接收并处理来自用户的各种事件，如点击、触摸、键盘输入等。它包含了处理这些用户交互所需的逻辑代码。
3. **生命周期管理：** 在 Android 中，每个 Activity 都有自己的生命周期，`MainActivity` 通过重写生命周期回调方法（如 `onCreate()`, `onStart()`, `onResume()`, `onPause()`, `onStop()`, `onDestroy()` 等）来管理其生命周期，以确保应用的正确运行和资源管理。
4. **导航和管理：** `MainActivity` 可以启动其他的活动（Activities），处理数据传递，以及管理应用内的导航。
5. **集成服务和功能：** 它也可以初始化和集成各种服务和应用功能，比如访问网络数据、使用本地数据库、集成第三方库或服务等。

按住ctrl+鼠标左键 点 activity_main会跳转到activity_main.xml 可以显示代码或图

![image-20240306111925622](JAVA&Android.assets/image-20240306111925622.png)

然后就可以在text里更改显示的文字

然后起一个虚拟机运行即可

![image-20240306112136796](JAVA&Android.assets/image-20240306112136796.png)
