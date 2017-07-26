#

"""
Convert between base 10 integers and a alphanumberic base using 4-Letter common male and female first names
Name source is US Census data, selected from ~400 most common names, with problematic ones removed.
Order of names have been randomized.
"""

__version__ = '1.0'

class NameBaseConverter(object):
    DECIMAL_BASE_DIGITS = '0123456789'
    # Names taken from top four letter USA census names, Male+Female randomized
    NAME_BASE_DIGITS = tuple("NETA BURT GIGI JADE ZORA ZANE KACY LORE RONA LADY BART LONI JOSH LARA BURL LUCY KARY ASHA MACY ADAH SETH NONA MARX NERY TOYA KATI RAUL TESS BRAD ZENA YONG REED RUDY KORY IRMA JOHN NEDA MAIA JEFF COLE SONG DOUG TARA LINN STAN DORI HONG JONA DONA JERI WAVA MISS ERIC LEAH STAR TAMA ROSE TREY GAIL MAUD RICH SHAD ANYA DICK ZULA KAYE LINA ERIN KARA CHAS KALI EDDY TORY IVEY VIKI LALA ETTA JANE MACK ALVA LYLA TYRA ELVA MARA JANA YING ELKE ERYN ERIK DYAN VETA AIDA YOKO ISIS SHEA TERA LYLE CHAD EMMY NEVA MARK LING TODD THUY FRAN GALE ZACK ERMA BRET OLIN ARLA LIEN EDEN LYNN LONA LEON EVAN NEIL ALEC NORA PURA LACI DANE TINA REBA KERI CHIN HUEY GREG GINO MARY WADE LOLA SARI OLGA MUOI RYAN BIBI CORA HUGO ASIA VERN CARI ANNE NANA ETHA SCOT ILDA ELIZ NOEL VIDA BREE FAYE KRIS RETA AMOS AIDE HYON ELMO DIAN KACI MARC MIKA JUNE RUSS KERA CARY SOOK OMER GLEN DEON BONG HYUN ELDA ZONA DARA DONG NOLA DUNG CLEO LINO MILO OREN ALDO NITA HUNG BELL KURT RORY SENA REID MIKI HOPE VITA SHON LERA RUTH YANG HANS DREW LULA NOVA AURA DALE DAWN BARB PAUL LUNA JERE ELLY YUNG ZINA GENE CHUN THAD CURT TONA LANE KATE LILI TARI PETE RANA RENA EDDA BUCK WARD LILY JUAN ADAM ABEL TUAN EMMA ARIE JOSE LUPE JOEL HANK BILL VITO TAMI TOBY META NYLA NICK JESS NENA CRUZ ELSA OTTO ANNA LURA JANN ANDY ELSE KYLA IONA SUNG DELL JAYE RISA SKYE RUBY JACK HERB ECHO XUAN LUCI EVON ROSY HEDY MYRA DEBI ADAN ESTA RUBI OWEN GINA JAME ODIS ALIX ALLA LACY ROLF RITA KYRA MATT MOSE EUNA LEIA AVIS TRAN JOAN RENE GENA MANA BESS EMIL MIMI JAMI LORA ALMA LUIS BEAU VADA SEAN KARL DION EDNA CHAN EZRA JUDE CARA LOYD ELNA ROXY OTIS BERT EDIE ZITA MILA REDA ALAN CORY CODY LENA ALIA JOYE NIKI MINA TOMI PHIL JENE NEAL LIDA HANA SUZY RICK RINA JUDY NELL GERI LEIF JOEY MONA NADA DAVE SUZI FAWN EVIE CHET FERN LANA ROSS WILL TENA ELMA NGOC LULU LUKE LOAN JILL NOAH NIDA SOON TINY YUKO SANG JAKE ENID LIZA LYDA TROY OTHA BOYD CHAU JADA CHER SHAY DINA YURI ROMA KALA JODY CLAY RAYE NOMA SARA CARL BETH MAYE ROSA OPAL HANG LISA LEAN TANA MERI VIVA GARY EARL JONE REVA KING EXIE JEAN HOYT MING HANH ZOLA DINO JINA NINA KYLE JUNG KENA ARON TOBI ALEX IRIS SIMA ELLA VENA ROBT SAUL LOMA DENA NILA KENT TONY ELOY LEDA MICA RONI JENI VERA KIRK PAGE DANA IVAN LORY LEVI LONG SHAE LISE JULE LOIS INES THEO ABBY GWYN MIKE FRED RICO RIVA MAYA OLEN DEAN ALDA VEDA ELZA DORA HUGH KATY KIRA GWEN JENA DIRK OMAR".split())


    def __init__(self):
        return

    def _convert2nameBase(self, numberIn, to_digits):
        # make an abs integer out of the numberIn
        x = abs(numberIn) 

        # create the result in base 'len(to_digits)'
        outList = list()
        if x == 0:
            outList.append(to_digits[0])
        else:
            while x > 0:
                digit = x % len(to_digits)
                outList.insert(0,to_digits[digit])
                x = int(x // len(to_digits))
        return "-".join(outList)

    def _convert2decimalBase(self, numberIn, from_digits, to_digits):
        # split on dashes
        x = 0
        #print "DBUG: numberIn[{0}]".format(numberIn)
        for digit in numberIn.split("-"):
            #print "DBUG: digit[{0}]".format(digit)
            try:
                x = x * len(from_digits) + from_digits.index(digit)
            except ValueError:
                raise ValueError('invalid digit "%s"' % digit)

        # create the result in base 'len(to_digits)'
        if x == 0:
            res = to_digits[0]
        else:
            res = ''
            while x > 0:
                digit = x % len(to_digits)
                res = to_digits[digit] + res
                x = int(x // len(to_digits))
        return res

    def encode(self, numberIn):
        return(self._convert2nameBase(abs(numberIn), self.NAME_BASE_DIGITS))

    def decode(self, nameBaseIn):
        return(self._convert2decimalBase(nameBaseIn, self.NAME_BASE_DIGITS, self.DECIMAL_BASE_DIGITS))



