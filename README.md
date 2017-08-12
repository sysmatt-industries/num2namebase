# Convert integers to/from numeric bases generated from english common names
# Also, Generate random passwords based on above


(tested on python 2.6+) 

```
cd /tmp
git clone https://github.com/sysmatt-industries/num2namebase.git

cd num2namebase

$ ./randomNameBasePassword.py  -h
usage: randomNameBasePassword.py [-h] [-v] [-c] [-d] [-b BITS] [-n {3,4,5}]
                                 [-q QUANTITY]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Enable Verbose Messages
  -c, --case            Enable name case randomization
  -d, --delim           Enable delimiter randomization
  -b BITS, --bits BITS  Specify number of bits in password to be generated,
                        default=40
  -n {3,4,5}, --names {3,4,5}
                        Specify name set to use by letter count, default=4
  -q QUANTITY, --quantity QUANTITY
                        Specify quantity of passwords to generate, default=1


$ ./randomNameBasePassword.py -q 5 
ZENA-SHAD-DORA-LYLA-JILL
COLE-STAR-NILA-LILI-XUAN
TARA-LYLA-STAN-DYAN-LINA
TESS-CHIN-MACY-NOAH-RAYE
DONA-OLGA-ZINA-MONA-SANG

$ ./randomNameBasePassword.py --quantity 5 --case 
neda-dena-rona-evan-kala
Doug-Abby-Luis-Shad-Lean
jeff-dona-odis-cary-mose
Maia-Zita-Kira-Paul-Meta
Stan-Kaye-Tara-Luke-Rana

$ ./randomNameBasePassword.py --quantity 5 --case --delim
DONA,ASHA,KIRK,KARA,LOMA
rudy.debi.loan.dara.vida
Neda$Otha$Brad$Else$Jeri
kory=robt=eden=neal=todd
tara,lynn,fran,sang,viva

$ ./randomNameBasePassword.py  --verbose --names 5
     args.bits[40]
    args.names[5]
       myDelim[-]
        myCase[upper]
passwdBitsFrom[1099511627776]
  passwdBitsTo[2199023255551]
     myRandInt[1805799705936]
AIMEE-LAYNE-BORIS-BENNY-DONYA


$ ./randomNameBasePassword.py --quantity 5 --case --delim --bits 20
ZORA-ELLA-JACK
ZANE+GWEN+BARB
lady,bret,omer
LADY$DAVE$LEIA
zora,zola,dino

$ ./randomNameBasePassword.py --quantity 5 --case --delim --bits 90
ZORA.ROSY.ABEL.CHAD.DANA.GINO.LUCY.ALAN.EMIL.NORA.LUKE
zora;miki;isis;lora;deon;stan;lily;hugh;mica;loni;nora
ZANE^DANE^LONI^PETE^EMIL^KALA^HERB^ELZA^YONG^GALE^MISS
JADE.RINA.NEAL.OMER.NANA.GENA.KAYE.ZULA.EVIE.REID.COLE
Jade,Dino,Bell,Andy,Nery,Drew,Eliz,Lura,Risa,Zane,Tyra

```

For instance:

"Your password is a series of names, all lower case, separated by commas, tara lynn with two "n"s fran sang viva"

"tara,lynn,fran,sang,viva"


Internally, this is using a class i wrote that converts integers into numeric bases generated from english names

```
$ ./int2nameBase.py 82479384792
BURT-YUKO-LUIS-TRAN-ROMA

$ ./nameBase2int.py BURT-YUKO-LUIS-TRAN-ROMA
82479384792
```

