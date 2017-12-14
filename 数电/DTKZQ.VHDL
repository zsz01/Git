-- 输入端口:
-- CLKIN:基准时钟信号，为系统提供2Hz的时钟脉冲，上升沿有效；
-- UPIN:电梯上升请求键。由用户向电梯控制器发出上升请求。高电平有效；
-- DOWNIN:电梯下降请求键，由用户向电梯控制器发出下降请求。高电平有效；
-- ST_CH[2..0]:楼层选择键入键，结合DIRECT完成楼层选择的键入，高电平有效；
-- CLOSE:提前关门输入键。可实现无等待时间的提前关门操作，高电平有效；
-- DELAY:延迟关门输入键。可实现有等待时间的延迟关门操作，高电平有效；
-- RUN_STOP:电梯运行或停止开关键。可实现由管理员控制电梯的运行或停止，高电平有效。

-- 输出端口：
-- LAMP:电梯运行或等待指示键，指示电梯的运行或等待状况。高电平有效；
-- RUN_WAIT:电梯运行或等待时间指示键，指示电梯运行状况或等待时间的长短，高电平有效；
-- ST_OUT:电梯所在楼层指示数码管，指示电梯当前所在的楼层数。即1~5层，高电平有效；
-- DIRECT:楼层选择指示数码管，指示用户所要选择的楼层数，高电平有效。



--DTKZQ.VHD                                          --显示电路
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_UNSIGNED.ALL;

ENTITY LED IS
PORT(
LEDIN: IN STD_LOGIC_VECTOR(2 DOWNTO 0);              --输入信号
LEDOUT: OUT STD_LOGIC_VECTOR(6 DOWNTO 0));           --输出信号
END LED;

ARCHITECTURE ART OF LED IS                           --结构体
BEGIN
  PROCESS(LEDIN)
  BEGIN
  CASE LEDIN IS                                      --共阴极LED显示译码 g f e d c b a
  WHEN"0000"=>ledout<="0111111";--0
  WHEN"0001"=>ledout<="0000110";--1
  WHEN"0010"=>ledout<="1011011";--2
  WHEN"0011"=>ledout<="1001111";--3
  WHEN"0100"=>ledout<="1100110";--4
  WHEN"0101"=>ledout<="1101101";--5
  WHEN"0110"=>ledout<="1111101";--6
  WHEN"0111"=>ledout<="0000111";--7
  WHEN"1000"=>ledout<="1111111";--8
  WHEN"1001"=>ledout<="1101111";--9
  WHEN"1010"=>ledout<="1110111";--10
  WHEN"1011"=>ledout<="1111100";--11
  WHEN"1100"=>ledout<="0111001";--12
  WHEN"1101"=>ledout<="1011110";--13
  WHEN"1110"=>ledout<="1111001";--14
  WHEN"1111"=>ledout<="1110001";--15
  WHEN OTHERS=>ledout<="0000000";                    --其他情况时灯灭
  END CASE;
  END PROCESS;
END ART;

LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.STD_LOGIC_UNSIGNED.ALL;
USE IEEE.STD_LOGIC_ARITH.ALL;

ENTITY DTKZQ IS
PORT(  CLK:IN STD_LOGIC;                             --2 Hz时钟输入信号
       UPIN:IN STD_LOGIC;                       	 --楼层上升请求键
       DOWNIN:IN STD_LOGIC;                    	     --楼层下降请求键
       ST_CH:IN STD_LOGIC;                           --结合DIRECT完成楼层选择的键入
       CLOSE:IN STD_LOGIC;                      	 --提前关门输入键
       DELAY:IN STD_LOGIC;   	                     --延迟关门输入键
       RUN_STOP:IN STD_LOGIC;						 --电梯运行的开关键
       
       LAMP:OUT STD_LOGIC;  					     --电梯运行或停止指示键
       RUN_WAIT:OUT STD_LOGIC_VECTOR(3 DOWNTO 0);    --结合LAMP指示电梯运行或等待时间
       ST_OUT:OUT STD_LOGIC_VECTOR(3 DOWNTO 0);      --电梯所在楼层指示数码管
       DIRECT:OUT STD_LOGIC_VECTOR(3 DOWNTO 0)); 	 --楼层选择指示数码管
END ENTITY DTKZQ;


ARCHITECTURE ART OF DTKZQ IS
SIGNAL UR,DR:STD_LOGIC_VECTOR(16 DOWNTO 1);      	 --上升或下降楼层请求寄存器
SIGNAL DIR,LIFTOR: INTEGER RANGE 0 TO 15;  	         --楼选指示及楼层数计数器
SIGNAL WAI_T:STD_LOGIC_VECTOR(2 DOWNTO 0);           --运行或等待计数器
SIGNAL DIVID,HAND,CLKIN:STD_LOGIC;   	             --时钟2分频和楼选复位变量以及时钟
SIGNAL LADD:STD_LOGIC_VECTOR(1 DOWNTO 0);            --电梯运行状态变量
SIGNAL CLOSEX,DELAYX:STD_LOGIC;                      --提前关门及延迟变量 

BEGIN                                                --内部信号值的输出
DIRECT<= CONV_STD_LOGIC_VECTOR(DIR,4)+1;              
ST_OUT<= CONV_STD_LOGIC_VECTOR(LIFTOR,4)+1;
RUN_WAIT<='0'&WAI_T;
LAMP<=LADD(1);                                       --LADD={00:等待; 10:下降; 11:上升}
HAND<=WAI_T(2)AND(NOT WAI_T(1)AND WAI_T(0));         --WAI_T[]=101时，楼选复位激活
CLOSEX<=CLOSE AND(NOT LADD(1));                      --电梯不在运行的情况下且按下了关闭键，关闭激活
DELAYX<=DELAY AND(NOT LADD(1));                      --电梯不在运行的情况下且按下了延迟键，延迟激活


--分频进程
P0:PROCESS(CLK) 
BEGIN
    IF (CLK'EVENT AND CLK='1') THEN         --CLK=1且位于上升沿时，CLKIN变反
        CLKIN<=NOT CLKIN;
    END IF;
END PROCESS P0;


--分频及楼选信号产生进程
P1:PROCESS(CLKIN)
BEGIN
IF (CLKIN'EVENT AND CLKIN='1') THEN         --CLKIN=1且位于上升沿时，DIVID变反
    DIVID<=NOT DIVID;
    IF (DIR="1111") THEN DIR<="0000";                 
    ELSE DIR<=DIR+1;                       
    END IF;
END IF;
END PROCESS P1;


--楼层请求寄存器的置位与复位进程
P2:PROCESS(UR, DR, DIR, UPIN, DOWNIN, ST_CH, LIFTOR, WAI_T, RUN_STOP, HAND)
VARIABLE NUM,T:INTEGER RANGE 0 TO 16 ;
BEGIN
   NUM:=LIFTOR+1;
   T:=DIR+1;
   IF (RUN_STOP='1') THEN                             
    IF (((T>NUM)AND (ST_CH='1'))OR (UPIN='1'))THEN  --电梯运行时选择楼层大于当前楼层或者有上升请求
        CASE T IS
        WHEN 1  => UR(1)<='1';
        WHEN 2  => UR(2)<='1';
        WHEN 3  => UR(3)<='1';
        WHEN 4  => UR(4)<='1';
        WHEN 5  => UR(5)<='1';
        WHEN 6  => UR(6)<='1';
        WHEN 7  => UR(7)<='1';
        WHEN 8  => UR(8)<='1';
        WHEN 9  => UR(9)<='1';
        WHEN 10 => UR(10)<='1';
        WHEN 11 => UR(11)<='1';
        WHEN 12 => UR(12)<='1';
        WHEN 13 => UR(13)<='1';
        WHEN 14 => UR(14)<='1';
        WHEN 15 => UR(15)<='1';
        WHEN 16 => UR(16)<='1';
        WHEN OTHERS=>NULL;
    END CASE;
--电梯运行时间到
    ELSIF (HAND='1')THEN 
        CASE NUM IS
        WHEN 1  => UR(1)<='0';
        WHEN 2  => UR(2)<='0';
        WHEN 3  => UR(3)<='0';
        WHEN 4  => UR(4)<='0';
        WHEN 5  => UR(5)<='0';
        WHEN 6  => UR(6)<='0';
        WHEN 7  => UR(7)<='0';
        WHEN 8  => UR(8)<='0';
        WHEN 9  => UR(9)<='0';
        WHEN 10 => UR(10)<='0';
        WHEN 11 => UR(11)<='0';
        WHEN 12 => UR(12)<='0';
        WHEN 13 => UR(13)<='0';
        WHEN 14 => UR(14)<='0';
        WHEN 15 => UR(15)<='0';
        WHEN 16 => UR(16)<='0';
        WHEN OTHERS=>NULL;
        END CASE;
    END IF;

--选择楼层小于当前楼层或者有下降请求
    IF (((T<NUM)AND (ST_CH='1'))OR(DOWNIN='1')) THEN
        CASE T IS
        WHEN 1  => DR(1)<='1';
        WHEN 2  => DR(2)<='1';
        WHEN 3  => DR(3)<='1';
        WHEN 4  => DR(4)<='1';
        WHEN 5  => DR(5)<='1';
        WHEN 6  => DR(6)<='1';
        WHEN 7  => DR(7)<='1';
        WHEN 8  => DR(8)<='1';
        WHEN 9  => DR(9)<='1';
        WHEN 10 => DR(10)<='1';
        WHEN 11 => DR(11)<='1';
        WHEN 12 => DR(12)<='1';
        WHEN 13 => DR(13)<='1';
        WHEN 14 => DR(14)<='1';
        WHEN 15 => DR(15)<='1';
        WHEN 16 => DR(16)<='1';
        WHEN OTHERS=>NULL;
        END CASE;
--电梯运行时间到
    ELSIF (HAND='1') THEN 
        CASE NUM IS
        WHEN 1  => DR(1)<='0';
        WHEN 2  => DR(2)<='0';
        WHEN 3  => DR(3)<='0';
        WHEN 4  => DR(4)<='0';
        WHEN 5  => DR(5)<='0';
        WHEN 6  => DR(6)<='0';
        WHEN 7  => DR(7)<='0';
        WHEN 8  => DR(8)<='0';
        WHEN 9  => DR(9)<='0';
        WHEN 10 => DR(10)<='0';
        WHEN 11 => DR(11)<='0';
        WHEN 12 => DR(12)<='0';
        WHEN 13 => DR(13)<='0';
        WHEN 14 => DR(14)<='0';
        WHEN 15 => DR(15)<='0';
        WHEN 16 => DR(16)<='0';
        WHEN OTHERS=>NULL;
        END CASE;
    END IF;
    ELSE 
      UR<="0000000000000000";
      DR<="0000000000000000";
    END IF;
END PROCESS P2;

--电梯运行次态的控制进程
P3:PROCESS(UR,DR,DIR,LIFTOR,LADD,WAI_T,RUN_STOP)
BEGIN
  IF (RUN_STOP='1') THEN          --电梯运行时
     IF (WAI_T="110") THEN
        IF ((UR OR DR)="0000000000000000") THEN 
          LADD(1)<='0';           --初始状态
        ELSE
          CASE LIFTOR IS
--电梯在第一层
             WHEN 0=>IF ((UR(1)OR DR(1))>'0') THEN LADD(1)<='0';  --等待状态
                        ELSE LADD<="11"; 	 --上升状态
                        END IF;
--电梯在第二层
             WHEN 1=>IF ((UR(2)OR DR(2))>'0') THEN LADD(1)<='0'; --等待状态
                     ELSIF ((( LADD(0)='1')AND ((UR(16 DOWNTO 3)OR DR(16 DOWNTO 3))>"00000000000000"))OR((UR(1)OR DR(1))='0')) THEN 
                        LADD <="11"; 	--上升状态
                     ELSE LADD<="10";  	--下降状态
                     END IF;
--电梯在第三层
             WHEN 2=>IF ((UR(3) OR DR(3))>'0') THEN LADD(1)<='0';
                         ELSIF ((( LADD(0)='1')AND ((UR(16 DOWNTO 4)OR DR(16 DOWNTO 4))>"0000000000000"))OR((UR(2 DOWNTO 1) OR DR(2 DOWNTO 1))="00")) THEN 
                            LADD<="11";
                         ELSE LADD<="10";
                         END IF;
--电梯在第四层
             WHEN 3=>IF ((UR(4) OR DR(4))>'0') THEN LADD(1)<='0';
                         ELSIF (((LADD(0)='1')AND ((UR(16 DOWNTO 5)OR DR(16 DOWNTO 5))>"000000000000"))OR((UR(3 DOWNTO 1)OR DR(3 DOWNTO 1))="000")) THEN
                             LADD<="11";
                         ELSE LADD<="10";
                         END IF;
--电梯在第五层
             WHEN 4=>IF ((UR(5) OR DR(5))>'0') THEN LADD(1)<='0';
                         ELSIF (((LADD(0)='1')AND ((UR(16 DOWNTO 6)OR DR(16 DOWNTO 6))>"00000000000"))OR((UR(4 DOWNTO 1)OR DR(4 DOWNTO 1))="0000")) THEN 
                            LADD<="11";
                         ELSE LADD<="10";
                         END IF;
--电梯在第六层
             WHEN 5=>IF ((UR(6) OR DR(6))>'0') THEN LADD(1)<='0';
                         ELSIF (((LADD(0)='1')AND ((UR(16 DOWNTO 7)OR DR(16 DOWNTO 7))>"0000000000" ))OR((UR(5 DOWNTO 1)OR DR(5 DOWNTO 1))="00000")) THEN 
                            LADD<="11";
                         ELSE LADD<="10";
                         END IF;
--电梯在第七层
             WHEN 6=>IF ((UR(7) OR DR(7))>'0') THEN LADD(1)<='0';
                         ELSIF (((LADD(0)='1')AND ((UR(16 DOWNTO 8)OR DR(16 DOWNTO 8))>"000000000"))OR((UR(6 DOWNTO 1)OR DR(6 DOWNTO 1))="000000")) THEN
                             LADD<="11";
                         ELSE LADD<="10";
                         END IF;
--电梯在第八层
             WHEN 7=>IF ((UR(8) OR DR(8))>'0') THEN LADD(1)<='0';
                         ELSIF (((LADD(0)='1')AND ((UR(16 DOWNTO 9)OR DR(16 DOWNTO 9))>"00000000" ))OR((UR(7 DOWNTO 1)OR DR(7 DOWNTO 1))="0000000")) THEN 
                            LADD<="11";
                         ELSE LADD<="10";
                         END IF;
--电梯在第九层
             WHEN 8=>IF ((UR(9) OR DR(9))>'0') THEN LADD(1)<='0';
                         ELSIF ((( LADD(0)='1')AND ((UR(16 DOWNTO 10)OR DR(16 DOWNTO 10))>"0000000" ))OR((UR(8 DOWNTO 1)OR DR(8 DOWNTO 1))="00000000")) THEN 
                            LADD<="11";
                         ELSE LADD<="10";
                         END IF;
--电梯在第十层
             WHEN 9=>IF ((UR(10) OR DR(10))>'0') THEN LADD(1)<='0';
                        ELSIF ((( LADD(0)='1')AND ((UR(16 DOWNTO 11)OR DR(16 DOWNTO 11))>"000000" ))OR((UR(9 DOWNTO 1)OR DR(9 DOWNTO 1))="000000000"))    THEN 
                            LADD<="11";
                        ELSE LADD<="10";
                        END IF;
--电梯在第十一层
             WHEN 10=>IF ((UR(11) OR DR(11))>'0') THEN LADD(1)<='0';
                        ELSIF (((LADD(0)='1')AND ((UR(16 DOWNTO 12)OR DR(16 DOWNTO 12)) >"00000"))OR((UR(10 DOWNTO 1)OR DR(10 DOWNTO 1))="0000000000"))   THEN
                             LADD<="11";
                        ELSE LADD<="10";
                        END IF;
--电梯在第十二层
             WHEN 11=>IF ((UR(12) OR DR(12))>'0') THEN LADD(1)<='0';
                         ELSIF ((( LADD(0)='1')AND ((UR(16 DOWNTO 13)OR DR(16 DOWNTO 13))>"0000" ))OR((UR(11 DOWNTO 1)OR DR(11 DOWNTO 1))="00000000000"))    THEN 
                            LADD<="11";
                         ELSE LADD<="10";
                         END IF;
--电梯在第十三层
             WHEN 12=>IF ((UR(13) OR DR(13))>'0') THEN LADD(1)<='0';
                         ELSIF ((( LADD(0)='1')AND ((UR(16 DOWNTO 14)OR DR(16 DOWNTO 14))>"000" ))OR((UR(12 DOWNTO 1)OR DR(12 DOWNTO 1))="000000000000"))    THEN 
                            LADD<="11";
                         ELSE LADD<="10";
                         END IF;
--电梯在第十四层
             WHEN 13=>IF ((UR(14) OR DR(14))>'0') THEN LADD(1)<='0';
                         ELSIF ((( LADD(0)='1')AND ((UR(16 DOWNTO 15)OR DR(16 DOWNTO 15))>"00" ))OR((UR(13 DOWNTO 1)OR DR(13 DOWNTO 1))="0000000000000"))    THEN
                             LADD<="11";
                         ELSE LADD<="10";
                         END IF;
--电梯在第十五层
             WHEN 14=>IF ((UR(15)OR DR(15))>'0') THEN LADD(1)<='0';
                         ELSIF ((( LADD(0)='1')AND ((UR(16)OR DR(16))>'0'))OR ((UR(14 DOWNTO 1)OR DR(14 DOWNTO 1))="00000000000000"))  THEN 
                            LADD<="11";
                         ELSE LADD<="10";
                         END IF;
--电梯在第十六层
             WHEN 15=>IF ((UR(16) OR DR(16))>'0') THEN
                            LADD(1)<='0';
                         ELSE LADD<="10";
                         END IF;
--其他情况
             WHEN OTHERS=>NULL;

           END CASE;
         END IF;
       END IF;
       ELSE LADD<="00";
     END IF;
 END PROCESS P3;

--电梯运行楼层计数及提前/延迟关门控制进程
P4:PROCESS(DIVID,WAI_T,LADD,CLOSEX,DELAYX)
BEGIN
    IF (DIVID'EVENT AND DIVID='1') THEN           
--分频后的时钟上升沿
       IF (WAI_T="000" OR CLOSEX='1') THEN WAI_T<="110";
       ELSE
          IF (DELAYX='0')THEN WAI_T<=WAI_T-1;
          ELSE WAI_T<="010";
          END IF;
--电梯处于运行状态
    IF(WAI_T="110") THEN
       IF (LADD="11") THEN                
--电梯上升，楼层加1
         LIFTOR<=LIFTOR+1;
       ELSIF (LADD="10") THEN 
         LIFTOR<=LIFTOR-1;
       END IF;
    END IF;
   END IF;
  END IF;
 END PROCESS P4;
 END ART;
 