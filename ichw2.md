**1.用你的语言描述图灵为什么要证明停机问题, 其证明方法和数学原理是什么**    
答：        
为什么要证明停机问题：因德国数学家家希尔伯特认为数学是可判定的，于是图灵用停机问题证明了他想法的错误。         
证明方法：反证法    
数学原理：设存在一个算法f对于任何程序及输入, 能够判定其会停机。
这时再构造一个程序g，使之当判断能够停机时输出不停机，判断不停机时输出停机，则当g（g）时，出现矛盾。   

**2.你在向中学生做科普，请向他们解释二进制补码的原理.**  
答：同学们好，今天就由我来向大家解释一下二进制补码的原理。  
    　　正数的补码仍是它本身，但负数的补码却不一样。在负数之中，补码与原码的和即为模。就如钟表一样，12便是它的模，
    顺时针调节9圈和逆时针调节3圈的结果是一样的，都会得到相同的时间。即是说9的补码是3,3的补码是9。补码的意义便在于它可以将减法变成加法。  
    　　当以计算机中的二进制为例时，码长为4,-3的原码为1011，反码为1100，那么它的补码便是反码再加1，即1101。
    那么为什么要加1呢？我们将-3的原码和反码相加会发现结果为1111，这时候再加1会得到10000,10000恰巧为它的模，
    所以反码加1便会得到补码。  
    　　那么补码是如何运算的呢？比如说设[x]是x的补码，它的运算规则便是[x+y]=[x]+[y],[x-y]=[x]+[-y]。其中超过码长的部分都是模的倍数，可以舍掉。
      就如时钟向前调9小时比向后调3小时早了12小时，但效果一样，可以舍去那12小时。
      例：码长为4，求5-3。5的补码为0101，-3的补码为1101，和为10010，把最高的1舍掉，得到0010，即是2。  
      
**3.浮点数**   
答：  
![](https://github.com/RQting/ichw/blob/master/%E6%8D%95%E8%8E%B7.PNG)
